#!/usr/bin/env python3
"""publish_wave.py - build the public copy of a wave whose raw exports and run records stay with the author.

Usage: python3 scripts/publish_wave.py <private-wave-folder> [wave-name]
Reads  <private-wave-folder>/responses.jsonl, raw/*.json, CHECKSUMS.txt (and, if present, ledger.csv, RESULTS.md, domains.csv)
Writes <wave>/responses.jsonl       one row per answer, only the fields named in KEEP and KEEP_CITATION
       <wave>/RAW-CHECKSUMS.txt     SHA-256 of every raw export under a neutral name (one-surface wave: raw-01.json = repetition 1)
       <wave>/answers_classified.jsonl, <wave>/domains.csv, <wave>/RESULTS.md   written by scripts/classify.py from the public rows
       <wave>/CHECKSUMS.txt         SHA-256 of every other file in <wave>/ (a README.md written by hand is included)
Nothing else is copied: the raw exports, the ledger and every field that is not in KEEP stay in the private folder.
The script stops if a raw export differs from its private checksum, if a row differs from its raw export, if RESULTS.md or
domains.csv differ in content from the private copies, or if a withheld value turns up in a public file. No network."""
import sys, json, csv, hashlib, pathlib, subprocess
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from ingest import extract, citations_of, STUDY      # the rules that made the rows, used here to compare them with the raw exports

KEEP = ["wave", "surface", "rep", "row_index", "run_started_utc", "question_id", "query_text", "answer_text",
        "citations", "citation_count", "unique_domains"]
KEEP_CITATION = ["position", "title", "url", "domain"]

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def stop(msg): sys.exit("STOP: " + msg)
def lines(p): return sorted(p.read_text(encoding="utf-8").splitlines())
def same(cits): return [(c["position"], c["title"], c["url"], c["domain"]) for c in cits]

def main(private, wave):
    out = ROOT / wave; out.mkdir(exist_ok=True)
    rows = [json.loads(l) for l in open(private / "responses.jsonl", encoding="utf-8")]
    rows.sort(key=lambda r: (r["surface"], r["rep"], r["row_index"]))
    cell = {(r["surface"], r["rep"], r["row_index"]): r for r in rows}
    run = {r["run_id"]: (r["surface"], r["rep"]) for r in rows}                  # a raw export is named after its run
    raws = sorted((private / "raw").glob("*.json"), key=lambda p: run.get(p.stem, ("", 0)))
    sums = dict(reversed(l.split()) for l in (private / "CHECKSUMS.txt").read_text().splitlines() if l.strip())
    raw_sums, compared = [], 0
    for n, p in enumerate(raws, 1):
        if p.stem not in run: stop(f"raw export number {n} has no rows")
        if sums.get("raw/" + p.name) != sha(p): stop(f"raw export number {n} differs from its private checksum")
        surface, rep = run[p.stem]
        for idx, item in enumerate(json.load(open(p, encoding="utf-8")), 1):
            q, text, srcs = extract(item, surface, STUDY["surfaces"][surface].get("schema"))
            r = cell.get((surface, rep, idx))
            if r is None or r["query_text"] != q.strip() or r["answer_text"] != text or same(r["citations"]) != same(citations_of(srcs, surface)):
                stop(f"{surface} repetition {rep} item {idx} differs from its raw export")
            compared += 1
        raw_sums.append(f"{sha(p)}  raw-{n:02d}.json")
    if compared != len(rows): stop(f"{len(rows) - compared} rows have no raw export")

    public = []
    for r in rows:
        row = {k: r[k] for k in KEEP}
        row["run_started_utc"] = r["run_started_utc"][:19] + "Z"                 # whole seconds
        row["citations"] = [{k: c.get(k) for k in KEEP_CITATION} for c in r["citations"]]
        public.append(row)
    (out / "responses.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in public) + "\n", encoding="utf-8")
    (out / "RAW-CHECKSUMS.txt").write_text("\n".join(raw_sums) + "\n", encoding="utf-8")
    subprocess.run([sys.executable, "-B", str(ROOT / "scripts" / "classify.py"), wave], check=True, stdout=subprocess.DEVNULL)
    for name in ("RESULTS.md", "domains.csv"):                                  # same content; the order of ties can differ
        if (private / name).exists() and lines(private / name) != lines(out / name): stop(f"{name} differs from the private copy")

    withheld = {p.stem for p in raws}
    for r in rows: withheld |= {v for k, v in r.items() if k not in KEEP and isinstance(v, str) and len(v) >= 6}
    if (private / "ledger.csv").exists():
        for l in csv.DictReader(open(private / "ledger.csv", encoding="utf-8")):
            withheld |= {v for k, v in l.items() if k not in ("wave", "surface") and v and len(v) >= 6}
    files = sorted(p for p in out.iterdir() if p.is_file() and not p.name.startswith(".") and p.name != "CHECKSUMS.txt")
    for p in files:
        text = p.read_text(encoding="utf-8")
        if any(v in text for v in withheld): stop(f"a withheld value is in {p.name}; nothing was signed off")
    (out / "CHECKSUMS.txt").write_text("\n".join(f"{sha(p)}  {p.name}" for p in files) + "\n", encoding="utf-8")
    print(f"{wave}: {len(public)} rows compared with {len(raws)} raw exports and written; {len(files)} files listed in CHECKSUMS.txt")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__)
    src = pathlib.Path(sys.argv[1]).resolve()
    main(src, sys.argv[2] if len(sys.argv) > 2 else src.name)
