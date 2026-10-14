# AI answer-surface audit toolkit - Germany 2026 study

One folder = one study. Everything a new study needs is three inputs; the scripts never change.

## Inputs
1. `study.json` - language, question column, surfaces (Apify actor id, input shape, output schema), classification lists (files, columns, wildcard rules), spacing between repetitions.
2. `questions.csv` - `id`, the prompt column named in `study.json` (here `de`), plus reader columns (`en`, `ru`) and evidence columns.
3. `lists/` - the frozen Russian-source lists (EU Annex XV domain map, VIGINUM Portal Kombat, CheckFirst Pravda) and the country's descriptive lists (authorities, public service, accountable media, narrative watchlist with Tier A/B evidence).

## Run
```
python3 scripts/run_wave.py pilot --surface copilot --question Q06   # one single-question run
python3 scripts/run_wave.py wave1                                    # 10 repetitions x all surfaces, resumable
python3 scripts/ingest.py wave1          # raw exports -> responses.jsonl + CHECKSUMS.txt
python3 scripts/resolve_goto.py wave1    # Google /goto tokens -> URLs (302 Location only)
python3 scripts/ingest.py wave1          # re-run to merge resolved URLs
python3 scripts/classify.py wave1        # list-based categories, headline numbers -> RESULTS.md, domains.csv
python3 scripts/annotate.py wave1        # descriptive annotation of 'other' domains (never scored)
python3 scripts/profile.py wave1         # per-question profile, Jaccard stability -> PROFILE.md
python3 scripts/verify.py wave1          # third-party recomputation from raw rows + frozen lists; must print VERIFY: OK
python3 scripts/manual_summary.py wave1  # manual browser channels (if any) -> manual/RESULTS-manual.md
python3 scripts/board_merge.py wave1 OUT # live board data (Apify runs + manual channels)
```
Manual browser answers are recorded with `scripts/manual_record.py` (one call per answer: channel, question, repetition, text file, sources JSON).

## Provenance
`RUN-LOG.md` holds the freeze (SHA-256 of protocol, questions, study.json, lists, scripts, UTC time) and every amendment. Each wave: `ledger.csv` (one row per Apify run with run_id, dataset_id, build, seed), `raw/<run_id>.json` untouched, `CHECKSUMS.txt`, `apify-runs-export.json`, `live.json`, `board.html` (the run board).

## New country or topic
Copy this folder, replace `questions.csv`, edit `study.json` (question column, language, list files), build the country's lists in `lists/` with a source per row, write `PROTOCOL.md`, freeze, run. The Apify token is read from the file named in the environment variable `STUDY_TOKEN_FILE` (keep that file outside the folder).
