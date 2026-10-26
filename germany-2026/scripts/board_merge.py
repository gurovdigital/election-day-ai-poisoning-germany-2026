#!/usr/bin/env python3
"""board_merge.py - merge <wave>/live.json (collection runs) and <wave>/manual/manual.json into one live.json for the run board."""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent; wave = sys.argv[1]; out = pathlib.Path(sys.argv[2])
d = json.loads((ROOT / wave / "live.json").read_text())
mp = ROOT / wave / "manual" / "manual.json"
d["manual_surfaces"] = ["google_signed_in", "google_ai_mode", "meta_ai"]
d["manual_labels"] = {"google_signed_in": "Google, signed in: AI Overview shown or not", "google_ai_mode": "Google KI-Modus", "meta_ai": "Meta AI"}
d["manual_design"] = "Berlin, signed-in Chrome · 10 questions × 2 repetitions per channel · reported separately"
d["manual"] = json.loads(mp.read_text()) if mp.exists() else {}
cells = [c for sf in d["runs"].values() for c in sf.values()]
d["totals"]["answers"] = sum(c.get("items", 0) for c in cells)
d["totals"]["runs_done"] = sum(1 for c in cells if c.get("status") == "SUCCEEDED")
d["totals"]["manual_planned"] = 60; d["totals"]["manual_done"] = sum(len(v) for ch in d["manual"].values() for v in ch.values())
out.write_text(json.dumps(d, ensure_ascii=False, indent=1)); print("board merged:", d["totals"])
