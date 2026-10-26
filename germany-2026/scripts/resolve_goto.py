#!/usr/bin/env python3
"""resolve_goto.py - resolve Google AI Overviews '/goto?url=<token>' citation wrappers to real URLs.
Usage: python3 scripts/resolve_goto.py wave1
Reads  wave1/responses.jsonl ; writes wave1/goto_resolved.json (token -> {url, http_status, resolved_utc})
Method: HTTP GET https://www.google.com/goto?url=<token> without following redirects; take the Location header.
Only the redirect target is recorded; the target page itself is never fetched. Idempotent (cached)."""
import sys, json, pathlib, subprocess, datetime
wave = sys.argv[1] if len(sys.argv) > 1 else "wave1"
base = pathlib.Path(__file__).parent.parent / wave
cache_p = base / "goto_resolved.json"
cache = json.loads(cache_p.read_text()) if cache_p.exists() else {}
tokens = []
for line in open(base / "responses.jsonl", encoding="utf-8"):
    r = json.loads(line)
    for c in r["citations"]:
        t = c.get("goto_token")
        if t and t not in cache and t not in tokens: tokens.append(t)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0 Safari/537.36"
for i, t in enumerate(tokens, 1):
    out = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}\t%{redirect_url}", "--max-time", "20", "-A", UA,
                          "https://www.google.com/goto?url=" + t], capture_output=True, text=True).stdout
    code, loc = (out.split("\t") + [""])[:2]
    cache[t] = {"url": loc or None, "http_status": code, "resolved_utc": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}
    if i % 20 == 0: cache_p.write_text(json.dumps(cache, ensure_ascii=False, indent=1)); print(i, "/", len(tokens))
cache_p.write_text(json.dumps(cache, ensure_ascii=False, indent=1))
ok = sum(1 for v in cache.values() if v["url"]); print(f"{wave}: {len(cache)} tokens cached, {ok} resolved, {len(cache)-ok} unresolved")
