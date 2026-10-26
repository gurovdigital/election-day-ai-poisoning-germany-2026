#!/usr/bin/env python3
"""manual_record.py - record one manual answer (Berlin, signed-in Chrome) into <wave>/manual/.
Usage: python3 scripts/manual_record.py wave1 <channel> <Qnn> <rep> --text FILE --sources FILE(json list of urls) [--screenshot PNG] [--aio-shown yes|no] [--note ...]
Writes <wave>/manual/answers.jsonl (append), <wave>/manual/manual.json (board summary), <wave>/manual/CHECKSUMS.txt (screenshots).
"""
import sys, json, csv, hashlib, pathlib, argparse, datetime, shutil
from urllib.parse import urlparse
ROOT = pathlib.Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser(); ap.add_argument("wave"); ap.add_argument("channel"); ap.add_argument("qid"); ap.add_argument("rep", type=int)
ap.add_argument("--text", required=True); ap.add_argument("--sources", required=True); ap.add_argument("--screenshot"); ap.add_argument("--aio-shown", choices=["yes", "no"]); ap.add_argument("--note", default="")
a = ap.parse_args()
M = ROOT / a.wave / "manual"; (M / "screenshots").mkdir(parents=True, exist_ok=True)
q = {r["id"]: r for r in csv.DictReader(open(ROOT / "questions.csv", encoding="utf-8"))}[a.qid]
utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
rid = f"MANUAL-{a.channel.upper()}-BER-W{a.wave[-1]}-{a.qid}-R{a.rep}"
srcs = json.load(open(a.sources))
def reg(h):
    h = h.lower(); h = h[4:] if h.startswith("www.") else h; p = h.split(".")
    if len(p) >= 3 and p[-2] in ("co","com","org","gov","ac","net") and len(p[-1]) == 2: return ".".join(p[-3:])
    return ".".join(p[-2:]) if len(p) >= 2 else h
cits = [{"position": i, "url": u, "domain": reg(urlparse(u).netloc)} for i, u in enumerate(srcs, 1) if u]
shot = None
if a.screenshot:
    dst = M / "screenshots" / f"{rid}.png"; shutil.copy(a.screenshot, dst); shot = dst.name
    with open(M / "CHECKSUMS.txt", "a") as f: f.write(f"{hashlib.sha256(dst.read_bytes()).hexdigest()}  screenshots/{shot}\n")
row = {"id": rid, "wave": a.wave, "channel": a.channel, "question_id": a.qid, "rep": a.rep, "query_text": q["de"], "utc": utc,
       "aio_shown": None if a.aio_shown is None else a.aio_shown == "yes", "answer_text": open(a.text, encoding="utf-8").read().strip(),
       "citations": cits, "citation_count": len(cits), "unique_domains": sorted({c["domain"] for c in cits}), "screenshot": shot, "note": a.note}
with open(M / "answers.jsonl", "a", encoding="utf-8") as f: f.write(json.dumps(row, ensure_ascii=False) + "\n")
mp = M / "manual.json"; m = json.loads(mp.read_text()) if mp.exists() else {}
m.setdefault(a.channel, {}).setdefault(a.qid, []).append({"rep": a.rep, "utc": utc, "aio_shown": row["aio_shown"], "sources": len(cits)})
mp.write_text(json.dumps(m, ensure_ascii=False, indent=1))
print(rid, "recorded:", len(cits), "sources", "aio" if row["aio_shown"] else "")
