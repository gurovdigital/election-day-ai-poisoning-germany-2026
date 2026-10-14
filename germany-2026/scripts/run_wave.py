#!/usr/bin/env python3
"""run_wave.py - start one wave through the Apify API and keep the provenance ledger.

Usage: python3 scripts/run_wave.py wave1            # 10 repetitions x 5 surfaces, resumable
       python3 scripts/run_wave.py wave1 --reps 3   # fewer repetitions (pilot/partial)
       python3 scripts/run_wave.py pilot --surface copilot --question Q06   # one single-question run

One run = one surface x one repetition, holding the 10 different questions (shuffled per run, seed logged).
Repetitions of the same surface start >= SPACING_MIN minutes apart. Every run: run_id, dataset_id, actor build,
timestamps, raw dataset saved untouched to <wave>/raw/<run_id>.json.
Nothing is written that did not come back from the API. Token is read from the file named in the environment variable STUDY_TOKEN_FILE.
"""
import sys, os, json, csv, time, random, pathlib, datetime, argparse, urllib.request, urllib.error

ROOT = pathlib.Path(__file__).resolve().parent.parent
STUDY = json.loads((ROOT / "study.json").read_text(encoding="utf-8"))
SPACING_MIN = STUDY.get("spacing_minutes", 10)
def _builder(cfg):
    def build(qs):
        inp = {"queries": list(qs) if cfg["input"] == "list" else "\n".join(qs)}
        inp.update(cfg.get("extra_input", {})); return inp
    return build
SURFACES = {k: (v["actor_id"], v["actor_name"], _builder(v), v.get("price_note", "")) for k, v in STUDY["surfaces"].items()}
ORDER = list(STUDY["surfaces"].keys())

def token():
    path = os.environ.get("STUDY_TOKEN_FILE")
    if not path: raise SystemExit("set the environment variable STUDY_TOKEN_FILE to the path of the file that holds the token")
    for line in open(os.path.expanduser(path)):
        line = line.strip()
        if line.startswith("APIFY_TOKEN=") or line.startswith("APIFY_API_TOKEN="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("no APIFY token in the token file")
TOKEN = token()

def api(path, data=None, method=None):
    req = urllib.request.Request("https://api.apify.com/v2" + path, headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"},
                                 data=json.dumps(data).encode() if data is not None else None, method=method or ("POST" if data is not None else "GET"))
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r: return json.load(r)
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:300]
            if e.code in (429, 500, 502, 503) and attempt < 4: time.sleep(5 * (attempt + 1)); continue
            raise SystemExit(f"API {e.code} on {path}: {body}")
        except urllib.error.URLError:
            if attempt < 4: time.sleep(5 * (attempt + 1)); continue
            raise

def utc(): return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def log(msg): print(utc(), msg, flush=True)

QUESTIONS = list(csv.DictReader(open(ROOT / "questions.csv", encoding="utf-8")))
QTEXT = {q["id"]: q[STUDY["question_column"]] for q in QUESTIONS}
LEDGER_COLS = ["wave", "surface", "rep", "run_id", "dataset_id", "actor_console_id", "actor_name", "build", "seed", "question_order",
               "started_utc", "finished_utc", "duration_s", "status", "items", "note"]

def ledger_path(wave): return ROOT / wave / "ledger.csv"
def read_ledger(wave):
    p = ledger_path(wave)
    return list(csv.DictReader(open(p, encoding="utf-8"))) if p.exists() else []
def append_ledger(wave, row):
    p = ledger_path(wave); new = not p.exists()
    with open(p, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=LEDGER_COLS); 
        if new: w.writeheader()
        w.writerow({k: row.get(k, "") for k in LEDGER_COLS})

def write_live(wave, state):
    state["updated_utc"] = utc()
    (ROOT / wave / "live.json").write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")

def start_run(surface, qs):
    actor_id, name, build_input, _ = SURFACES[surface]
    inp = build_input(qs)
    r = api(f"/acts/{actor_id}/runs", inp)["data"]
    return r["id"], r["defaultDatasetId"], r.get("buildNumber"), r["startedAt"]

def wait_run(run_id, poll=15, max_wait=1800):
    t0 = time.time()
    while True:
        d = api(f"/actor-runs/{run_id}")["data"]
        if d["status"] in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"): return d
        if time.time() - t0 > max_wait: return d
        time.sleep(poll)

def fetch_items(dataset_id):
    return api(f"/datasets/{dataset_id}/items?clean=true&limit=1000")

def count_citations(items, surface):
    n = 0
    for it in items:
        for k in ("sources", "citations", "references", "links"):
            if isinstance(it.get(k), list): n += len(it[k]); break
    return n

def finish_run(wave, surface, rep, run_id, dataset_id, build, seed, order, started, state, note=""):
    d = wait_run(run_id)
    items = fetch_items(dataset_id) if d["status"] == "SUCCEEDED" else []
    raw = ROOT / wave / "raw" / f"{run_id}.json"
    raw.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
    fin = d.get("finishedAt") or utc()
    dur = (datetime.datetime.fromisoformat(fin.replace("Z", "+00:00")) - datetime.datetime.fromisoformat(started.replace("Z", "+00:00"))).total_seconds()
    row = dict(wave=wave, surface=surface, rep=rep, run_id=run_id, dataset_id=dataset_id, actor_console_id=SURFACES[surface][0], actor_name=SURFACES[surface][1],
               build=build or d.get("buildNumber", ""), seed=seed, question_order=" ".join(order), started_utc=started, finished_utc=fin, duration_s=int(dur),
               status=d["status"], items=len(items), note=note)
    append_ledger(wave, row)
    cell = state["runs"][surface][str(rep)]
    cell.update(status=d["status"], finished_utc=fin, items=len(items), citations=count_citations(items, surface))
    state["totals"]["answers"] = sum(c.get("items", 0) for s in state["runs"].values() for c in s.values())
    state["totals"]["runs_done"] = sum(1 for s in state["runs"].values() for c in s.values() if c.get("status") in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"))
    write_live(wave, state)
    log(f"{surface} rep {rep}: {d['status']} items={len(items)}")
    return row

def run_pilot(surface, qid):
    wave = "pilot"; (ROOT / wave / "raw").mkdir(parents=True, exist_ok=True)
    state = {"wave": wave, "runs": {surface: {}}, "totals": {}}
    order = [qid]; run_id, ds, build, started = start_run(surface, [QTEXT[qid]])
    state["runs"][surface]["1"] = {"run_id": run_id, "dataset_id": ds, "status": "RUNNING", "started_utc": started}
    log(f"pilot {surface} {qid}: started {run_id}")
    finish_run(wave, surface, 1, run_id, ds, build, "-", order, started, state, note=f"pilot single question {qid}")

def run_wave(wave, reps, surfaces):
    (ROOT / wave / "raw").mkdir(parents=True, exist_ok=True)
    done = {(r["surface"], int(r["rep"])) for r in read_ledger(wave) if r["status"] == "SUCCEEDED"}
    live_p = ROOT / wave / "live.json"
    state = json.loads(live_p.read_text()) if live_p.exists() else {"wave": wave, "design": f"{len(surfaces)} surfaces x 10 questions x {reps} repetitions", "surfaces": surfaces,
                                                                    "questions": [{"id": q["id"], "text": q[STUDY["question_column"]], "en": q.get("en", "")} for q in QUESTIONS],
                                                                    "started_utc": utc(), "runs": {s: {} for s in surfaces}, "totals": {"answers": 0, "runs_done": 0, "runs_planned": len(surfaces) * reps}}
    for s in surfaces: state["runs"].setdefault(s, {})
    write_live(wave, state)
    for rep in range(1, reps + 1):
        rep_t0 = time.time(); pending = []
        for surface in surfaces:
            if (surface, rep) in done: log(f"{surface} rep {rep}: already SUCCEEDED, skip"); continue
            seed = f"{wave}-{surface}-rep{rep}"; rng = random.Random(seed)
            order = [q["id"] for q in QUESTIONS]; rng.shuffle(order)
            run_id, ds, build, started = start_run(surface, [QTEXT[q] for q in order])
            state["runs"][surface][str(rep)] = {"run_id": run_id, "dataset_id": ds, "status": "RUNNING", "started_utc": started, "seed": seed}
            write_live(wave, state); log(f"{surface} rep {rep}: started {run_id} seed={seed}")
            pending.append((surface, rep, run_id, ds, build, seed, order, started))
            time.sleep(2)
        for args in pending: finish_run(wave, *args, state)
        if rep < reps:
            wait = SPACING_MIN * 60 - (time.time() - rep_t0)
            if wait > 0: log(f"spacing: waiting {int(wait)} s before rep {rep + 1}"); time.sleep(wait)
    state["finished_utc"] = utc(); write_live(wave, state)
    # account-side run list for the wave window (provenance package)
    runs = api("/actor-runs?limit=200&desc=true")["data"]["items"]
    ids = {r["run_id"] for r in read_ledger(wave)}
    (ROOT / wave / "apify-runs-export.json").write_text(json.dumps([r for r in runs if r["id"] in ids], indent=1), encoding="utf-8")
    log(f"wave {wave} finished: {state['totals']}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("wave"); ap.add_argument("--reps", type=int, default=10)
    ap.add_argument("--surface", default=None); ap.add_argument("--question", default="Q06"); ap.add_argument("--surfaces", default=",".join(ORDER))
    a = ap.parse_args()
    if a.wave == "pilot": run_pilot(a.surface or "copilot", a.question)
    else: run_wave(a.wave, a.reps, a.surfaces.split(","))
