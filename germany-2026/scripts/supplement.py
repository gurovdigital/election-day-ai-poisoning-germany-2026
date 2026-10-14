#!/usr/bin/env python3
"""supplement.py - re-ask, in single-question runs, the (question x repetition) cells a surface left empty (e.g. Google returned no AI Overview).
Usage: python3 scripts/supplement.py wave1 google_ai_overviews "1:Q01,2:Q03,..."   Rows join the ledger with note SUPPLEMENT and the original rep number."""
import sys, json, time, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import run_wave as rw
wave, surface, spec = sys.argv[1], sys.argv[2], sys.argv[3]
cells = [(int(a), b) for a, b in (x.split(":") for x in spec.split(","))]
live = rw.ROOT / wave / "live.json"; state = json.loads(live.read_text())
state.setdefault("supplements", [])
pending = []
for rep, qid in cells:
    run_id, ds, build, started = rw.start_run(surface, [rw.QTEXT[qid]])
    state["supplements"].append({"surface": surface, "rep": rep, "question": qid, "run_id": run_id, "started_utc": started})
    rw.write_live(wave, state); rw.log(f"SUPPLEMENT {surface} rep {rep} {qid}: started {run_id}")
    pending.append((rep, qid, run_id, ds, build, started)); time.sleep(2)
for rep, qid, run_id, ds, build, started in pending:
    state["runs"].setdefault(surface, {}).setdefault(str(rep), {})
    cell_backup = dict(state["runs"][surface][str(rep)])
    rw.finish_run(wave, surface, rep, run_id, ds, build, "-", [qid], started, state, note=f"SUPPLEMENT single question {qid} for rep {rep}")
    state["runs"][surface][str(rep)] = cell_backup; rw.write_live(wave, state)
rw.log("supplements done")
