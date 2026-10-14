#!/usr/bin/env python3
"""ingest.py - turn raw Apify dataset exports into responses.jsonl (study-agnostic; settings in study.json).

Usage: python3 scripts/ingest.py wave1
Reads  study.json, questions.csv, <wave>/ledger.csv, <wave>/raw/<run_id>.json (untouched API output)
Writes <wave>/responses.jsonl (one row per answer; run_id + row index = provenance anchor), <wave>/CHECKSUMS.txt
No network, no classification. A raw file whose run_id is not in the ledger is rejected.
Schemas: apify_official (query/text/sources[url,title]) ; johnvc_copilot (query/markdown/references[link,title]).
"""
import sys, json, csv, hashlib, re, pathlib
from urllib.parse import urlparse, parse_qs, unquote

ROOT = pathlib.Path(__file__).resolve().parent.parent
STUDY = json.loads((ROOT / "study.json").read_text(encoding="utf-8"))
QCOL = STUDY["question_column"]
QUESTIONS = {r[QCOL].strip(): r["id"] for r in csv.DictReader(open(ROOT / "questions.csv", encoding="utf-8"))}

GOOGLE_UI_MARKERS = [
    ("en", r"AI responses may include mistakes|AI can make mistakes"), ("nl", r"AI-reacties kunnen fouten bevatten"),
    ("es", r"la IA puede cometer errores|respuestas de la IA pueden incluir errores"), ("fr", r"l'IA peut faire des erreurs|réponses de l'IA peuvent"),
    ("pl", r"AI może popełniać błędy|Odpowiedzi wygenerowane przez AI mogą|Odpowiedzi AI mogą"), ("vi", r"AI có thể mắc lỗi"),
    ("tr", r"yapay zeka hata yapabilir"), ("zh-TW", r"AI 可能會出錯"), ("ja", r"AI は不正確な情報|AI の回答には"), ("hi", r"एआई गलत जानकारी"),
    ("de", r"KI-Antworten können Fehler enthalten"), ("it", r"risposte dell'IA potrebbero contenere errori"), ("pt", r"respostas da IA podem conter erros"),
    ("share:en", r"\s{3,}Share(?=[A-Z])"), ("share:nl", r"\s{3,}Delen"), ("share:es", r"\s{3,}Compartir"), ("share:fr", r"\s{3,}Partager"),
    ("share:pl", r"\s{3,}Udostępnij"), ("share:vi", r"\s{3,}Chia sẻ"), ("share:tr", r"\s{3,}Paylaş"), ("share:zh-TW", r"\s{3,}分享"),
    ("share:ja", r"\s{3,}共有"), ("share:hi", r"\s{3,}शेयर"), ("share:de", r"\s{3,}Teilen"), ("share:?", r"Facebook\s*Gmail\s*X\s*Reddit\s*WhatsApp"),
]
def strip_google_ui(text):
    best = None
    for lang, pat in GOOGLE_UI_MARKERS:
        m = re.search(pat, text, re.I)
        if m and (best is None or m.start() < best[1]): best = (lang, m.start())
    if not best: return text, None
    lang = best[0].split(":")[-1]
    return text[:best[1]].rstrip(), (lang if lang != "?" else "unknown")

def registrable(host):
    host = host.lower()
    if host.startswith("www."): host = host[4:]
    parts = host.split(".")
    if len(parts) >= 3 and parts[-2] in ("co", "com", "org", "gov", "ac", "net") and len(parts[-1]) == 2: return ".".join(parts[-3:])
    return ".".join(parts[-2:]) if len(parts) >= 2 else host

def norm_url(u):
    if not u: return None, None
    u = u.split("#")[0]
    p = urlparse(u)
    q = {k: v for k, v in parse_qs(p.query).items() if not k.startswith("utm_")}
    clean = p._replace(query="&".join(f"{k}={v[0]}" for k, v in q.items())).geturl()
    return clean, registrable(p.netloc) if p.netloc else None

def extract(item, surface, schema):
    """Return (query, answer_text, [source dicts with url/title/...])."""
    if schema == "johnvc_copilot":
        srcs = [{"url": s.get("link") or s.get("url") or "", "title": s.get("title"), "snippet": s.get("snippet")} for s in item.get("references") or []]
        return (item.get("query") or ""), (item.get("markdown") or item.get("summary") or ""), srcs
    return (item.get("query") or ""), (item.get("text") or ""), list(item.get("sources") or [])

def citations_of(srcs, surface):
    out = []
    for i, s in enumerate(srcs, 1):
        url = s.get("url") or ""
        c = {"position": i, "title": s.get("title"), "section": s.get("section"), "url_raw": url}
        if surface == "google_ai_overviews" and url.startswith("/goto?url="):
            c["goto_token"] = unquote(url.split("=", 1)[1]); c["url"] = None; c["domain"] = None
        else:
            c["url"], c["domain"] = norm_url(url)
        for k in ("snippet", "description", "date", "lastUpdated"):
            if s.get(k): c[k] = s[k]
        out.append(c)
    return out

def main(wave):
    base = ROOT / wave
    ledger = {r["run_id"]: r for r in csv.DictReader(open(base / "ledger.csv", encoding="utf-8"))}
    rows, sums = [], []
    for raw in sorted((base / "raw").glob("*.json")):
        run_id = raw.stem
        if run_id not in ledger: print("REJECT (not in ledger):", raw.name); continue
        meta = ledger[run_id]; surface = meta["surface"]; schema = STUDY["surfaces"][surface].get("schema", "apify_official")
        data = json.load(open(raw, encoding="utf-8"))
        sums.append(f"{hashlib.sha256(raw.read_bytes()).hexdigest()}  raw/{raw.name}")
        for idx, item in enumerate(data, 1):
            q, text, srcs = extract(item, surface, schema)
            q = q.strip(); ui_locale = None
            if surface == "google_ai_overviews": text, ui_locale = strip_google_ui(text)
            cits = citations_of(srcs, surface)
            rows.append({
                "wave": meta["wave"], "surface": surface, "rep": int(meta["rep"]), "run_id": run_id, "row_index": idx,
                "dataset_id": meta.get("dataset_id", ""), "actor_console_id": meta["actor_console_id"], "actor_name": meta.get("actor_name", ""),
                "run_started_utc": meta["started_utc"], "run_status": meta["status"],
                "question_id": QUESTIONS.get(q, "UNKNOWN"), "query_text": q, "answer_text": text, "ui_locale_evidence": ui_locale,
                "citations": cits, "citation_count": len(cits), "unique_domains": sorted({c["domain"] for c in cits if c.get("domain")}),
                "refusal_flag": False,
            })
    gp = base / "goto_resolved.json"
    if gp.exists():
        goto = json.loads(gp.read_text(encoding="utf-8"))
        for r in rows:
            for c in r["citations"]:
                t = c.get("goto_token")
                if t and goto.get(t, {}).get("url"):
                    c["url"], c["domain"] = norm_url(goto[t]["url"]); c["url_resolved_via"] = "google.com/goto 302 Location"
            r["unique_domains"] = sorted({c["domain"] for c in r["citations"] if c.get("domain")})
    (base / "responses.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")
    (base / "CHECKSUMS.txt").write_text("\n".join(sums) + "\n", encoding="utf-8")
    unk = [r for r in rows if r["question_id"] == "UNKNOWN"]
    print(f"{wave}: {len(rows)} rows from {len(sums)} raw exports; UNKNOWN question ids: {len(unk)}" + (f" e.g. {unk[0]['query_text'][:80]!r}" if unk else ""))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "wave1")
