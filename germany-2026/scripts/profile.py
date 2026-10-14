#!/usr/bin/env python3
"""profile.py - per-question source profile and answer stability across repetitions. Reads answers_classified.jsonl + domains_annotated.csv."""
import json, csv, sys, collections, itertools
wave = sys.argv[1] if len(sys.argv) > 1 else "wave1"
rows = [json.loads(l) for l in open(f"{wave}/answers_classified.jsonl", encoding="utf-8")]
ann = {r["domain"]: r for r in csv.DictReader(open(f"{wave}/domains_annotated.csv", encoding="utf-8"))}
import json as _j; S = list(_j.load(open("study.json"))["surfaces"].keys())
short = {k: v["label"] for k, v in _j.load(open("study.json"))["surfaces"].items()}
qs = {r["id"]: r["en"] for r in csv.DictReader(open("questions.csv", encoding="utf-8"))}
out = ["# Per-question source profile (Wave 1)\n", "Label after a domain: list category (A = authority, PS = public service, M = Presserat-accountable media, D = Reuters DNR 2025 brand, RU = Russian state media, o = other) and, for 'other', the descriptive annotation type.\n"]
def lab(d):
    a = ann.get(d, {}); cat = a.get("category", "?")
    m = {"de_authority": "A", "de_public_service": "PS", "de_media_accountable": "M", "de_media_dnr": "D", "other": "o", "ru_state": "RU", "ru_network": "RUnet"}
    return m.get(cat, "?") + ("/" + a.get("annotation_type", "") if cat == "other" else "")
stab = []
for q in sorted(qs):
    out.append(f"\n## {q} - {qs[q]}\n")
    out.append("| surface | answers | mean cit. | distinct domains (10 reps) | domains in ≥8/10 answers | top domains (answers citing it) |")
    out.append("|---|---|---|---|---|---|")
    for s in S:
        rs = [r for r in rows if r["question_id"] == q and r["surface"] == s]
        if not rs: continue
        per_answer = [set(c["domain"] for c in r["citations"] if c.get("domain")) for r in rs]
        cnt = collections.Counter(d for ds in per_answer for d in ds)
        stable = [d for d, n in cnt.items() if n >= 0.8 * len(rs)]
        top = ", ".join(f"{d} [{lab(d)}] {n}" for d, n in cnt.most_common(6))
        jac = [len(a & b) / len(a | b) for a, b in itertools.combinations(per_answer, 2) if a | b]
        stab.append((q, s, sum(jac) / len(jac) if jac else 0))
        out.append(f"| {short[s]} | {len(rs)} | {sum(r['citation_count'] for r in rs)/len(rs):.1f} | {len(cnt)} | {len(stable)} | {top} |")
out.append("\n## Stability of citations across the 10 repetitions (mean pairwise Jaccard similarity of cited-domain sets; 1 = identical)\n")
out.append("| question | " + " | ".join(short[s] for s in S) + " |"); out.append("|---|" + "---|" * len(S))
for q in sorted(qs):
    out.append(f"| {q} | " + " | ".join(f"{next((j for qq, ss, j in stab if qq == q and ss == s), 0):.2f}" for s in S) + " |")
for s in S:
    vals = [j for qq, ss, j in stab if ss == s]; out.append(f"\nMean {short[s]}: {sum(vals)/len(vals):.2f}")
open(f"{wave}/PROFILE.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out[-12:]))
