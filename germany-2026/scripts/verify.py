#!/usr/bin/env python3
"""verify.py - third-party recomputation of the published numbers from the stored rows and the frozen Russian-source lists only.
Usage: python3 scripts/verify.py wave1
Checks: (1) raw export hashes vs CHECKSUMS.txt; (2) run counts vs ledger; (3) recomputes headline numbers 1-3 from responses.jsonl
using ONLY lists/ru_* (independent minimal re-implementation); (4) prints RESULTS.md fractions for comparison."""
import sys, json, csv, hashlib, pathlib, re, collections
ROOT = pathlib.Path(__file__).resolve().parent.parent; wave = sys.argv[1] if len(sys.argv) > 1 else "wave1"; W = ROOT / wave
STUDY = json.loads((ROOT / "study.json").read_text(encoding="utf-8")); LC = STUDY["lists"]; L = ROOT / "lists"
ok = True
sums = dict(l.split()[::-1] for l in (W / "CHECKSUMS.txt").read_text().splitlines() if l.strip())
for rel, h in sums.items():
    p = W / rel
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != h: print("HASH MISMATCH", rel); ok = False
print(f"[1] {len(sums)} raw exports hash-verified: {'OK' if ok else 'FAIL'}")
ledger = list(csv.DictReader(open(W / "ledger.csv", encoding="utf-8")))
rows = [json.loads(l) for l in open(W / "responses.jsonl", encoding="utf-8")]
runs_in_rows = collections.Counter(r["run_id"] for r in rows)
print(f"[2] ledger runs: {len(ledger)} (SUCCEEDED {sum(1 for l in ledger if l['status']=='SUCCEEDED')}); runs in responses: {len(runs_in_rows)}; rows: {len(rows)}; "
      f"per surface: {dict(collections.Counter(r['surface'] for r in rows))}; runs with <10 items: {[k for k, v in runs_in_rows.items() if v < 10]}")
missing = [l["run_id"] for l in ledger if l["status"] == "SUCCEEDED" and int(l.get("items") or 0) > 0 and l["run_id"] not in runs_in_rows]
empty = [l["run_id"] for l in ledger if l["status"] == "SUCCEEDED" and int(l.get("items") or 0) == 0]
if empty: print(f"   runs that legitimately returned 0 items (no AI Overview on Google's side): {len(empty)}")
if missing: print("   SUCCEEDED ledger runs without rows:", missing); ok = False
def reg(host):
    host = host.lower()
    if host.startswith("www."): host = host[4:]
    p = host.split(".")
    if len(p) >= 3 and p[-2] in ("co", "com", "org", "gov", "ac", "net") and len(p[-1]) == 2: return ".".join(p[-3:])
    return ".".join(p[-2:]) if len(p) >= 2 else host
ru_state = {reg(r[LC["ru_state"]["domain_col"]]) for r in csv.DictReader(open(L / LC["ru_state"]["file"], encoding="utf-8"))}
ru_hosts = set()
for spec in LC["ru_network"]:
    for r in csv.DictReader(open(L / spec["file"], encoding=spec.get("encoding", "utf-8"))):
        h = r[spec["domain_col"]].lower().strip()
        if spec.get("unescape"): h = h.replace("[.]", ".")
        if h: ru_hosts.add(h)
ru_reg = {reg(h) for h in ru_hosts}
def is_ru(url):
    host = re.sub(r"^https?://", "", url).split("/")[0].lower()
    if host.startswith("www."): host = host[4:]
    return reg(host) in ru_state or host in ru_hosts or reg(host) in ru_reg
N = len(rows); C = sum(len(r["citations"]) for r in rows)
n1 = sum(1 for r in rows if any(c.get("url") and is_ru(c["url"]) for c in r["citations"]))
k2 = sum(1 for r in rows for c in r["citations"] if c.get("url") and is_ru(c["url"]))
doms = {reg(re.sub(r"^https?://", "", c["url"]).split("/")[0]) for r in rows for c in r["citations"] if c.get("url")}
d2 = sum(1 for d in doms if d in ru_state or d in ru_reg)
n3 = sum(1 for r in rows if len(r["citations"]) == 0)
tld = sorted(d for d in doms if d.endswith((".ru", ".su", ".by")))
print(f"[3] recomputed: (1) answers citing ru_state/ru_network = {n1}/{N}; (2) ru citations = {k2}/{C}, ru domains = {d2}/{len(doms)}; (3) zero-citation answers = {n3}/{N}; .ru/.su/.by flag = {tld or 'none'}")
res = (W / "RESULTS.md").read_text(encoding="utf-8") if (W / "RESULTS.md").exists() else ""
fractions = re.findall(r"\*\*(\d+)/(\d+) = ", res)[:4]              # outside the f-string: Python 3.9-3.11 reject backslashes there
print(f"[4] RESULTS.md headline fractions found: {fractions}")
print("VERIFY:", "OK" if ok else "FAIL")
