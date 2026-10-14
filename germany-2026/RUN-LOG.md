# RUN-LOG - Germany 2026

## FREEZE 2026-09-20T16:40:08Z - protocol v1.0 approved by Pavel Gurov (18:40 CEST)

SHA-256 before the first wave run:
```
019eb908f5139e29e7290c8895ccf7d3d1cd28dc44d74b2746febcc9a3953ff4  PROTOCOL.md
00c6f77424aa611ce1639a09e69720a4773533a1c372a5eb46be1b38813147c7  study.json
d1c2a1fc4ffdecb568318d7412f54ba0c527a7da3442e81ddda5556da8212796  questions.csv
6667993316c82852f320528c74e9099c2ef547e203b4ce6262a9e7407dcc7582  lists/ru_state_domains.csv
3ddeb4171166e384733bbdf16b8afc66c21b2e40adf166ac9dc107e77e176d89  lists/viginum_portal-kombat_domains_20241227.csv
7253e14ed9e67057f8f8e423cb1a33d0df0d24bfd01d55314324ace109d72559  lists/checkfirst_pravda_wikipedia_results.csv
67ca42495bf7e489fcaf964d0492613ed865c84eafc3b316e2f933ee8ddabc4a  lists/de_outlets_narrative_watchlist.csv
a031bee5caaf8ede902f6ac0633226b6b89dd0ea12e4b951b9d93a849c4913e8  lists/de_authority_domain-map.csv
cf4b4e4ef6e2097bd6c387e66928114eac7cfb5b79626b2caac2564b3c108920  lists/de_public_service_domains.csv
13e5a27255a4b56136231b5fcc9c9c2e5ebe305daa539e9ab1e1e703fea6d844  lists/de_media_accountable_domain-map.csv
5daadd6a488ecce80f53048fce473af915fde2bedc09cb0c53239a1828950f42  lists/CHECKSUMS-de.txt
63138a126cea5950ea3264bc78c7d596443ad62e5cb93042ceffd295f70c0aad  scripts/run_wave.py
965972d489a1e40a88cb7cbad420a46c9a011c9f8afbea87fe36cd16be0d4ecf  scripts/ingest.py
82423cdf0e2ffd949a79ff83c06ec6dea740cfec881fbd8200b77a01d3cbff6e  scripts/classify.py
84de669516ad5ab5907f12271411da210b7085bbb3c4de8c5f1df0e74f60a826  scripts/verify.py
```

Pilot before freeze: Copilot actor johnvc/bing-copilot-api, run fdSIR679KtbFev1lG, Q06, 1 item, 11 references (pilot/ledger.csv).
Wave 1 window: election day evening, polling stations closed 18:00 CEST; started immediately after freeze.


## AMENDMENT A1 2026-09-20T17:40:25Z - descriptive list added during the wave (not in headline numbers 1-3)
- `lists/de_media_dnr_domain-map.csv` (20 domains): brands on the Reuters Institute Digital News Report 2025 Germany reach and trust charts, category `de_media_dnr`, added to `study.json`. Reason: the Presserat-based `de_media_accountable` list is thin (7 domains) because the Presserat publishes no signatory list; the DNR list is an external published list of the national brands. It affects only the descriptive category table and headline number 4 (authority/public-service share is unaffected). The frozen Russian-source lists and headline numbers 1-3 are untouched.
- Manual Berlin channels executed 16:42-17:32Z: Google signed-in 10x2, Google KI-Modus (udm=50) 10x2, Meta AI 10x1 (reduced from 2 repetitions to limit browser-permission prompts); records in `wave1/manual/`. Screenshots could not be persisted by the browser extension; page extractions with UTC timestamps are stored instead (declared limitation).

## AMENDMENT A2 2026-09-20T17:41:57Z - six public-body domains added to `lists/de_authority_domain-map.csv` after they appeared in the answers (bafa.de, bamf.de, bundeswirtschaftsministerium.de, gesetze-im-internet.de, deutschland.de, leipzig.de), each confirmed by the body's own Impressum. Descriptive layer only (headline number 4); headline numbers 1-3 untouched.

## WAVE 1 - COMPLETED 2026-09-20T18:24:00Z
- 50 wave runs (5 surfaces x 10 repetitions, 10 questions each, shuffled with logged seeds) started 16:40:09Z, finished 18:14:49Z; all SUCCEEDED. Google AI Overviews returned 86/100 items: Google produced no AI Overview for Q02 in 8 repetitions, Q03 in 5, Q01, Q04, Q05 in 1 each.
- SUPPLEMENT (18:19-18:22Z, `scripts/supplement.py`): the 14 empty (question x repetition) cells were re-asked in single-question runs, all started within three minutes (spacing rule not applied, declared). 6 returned an AI Overview (Q01 rep1, Q03 rep2, Q02 rep3, Q02 rep4, Q04 rep7, Q05 rep7); 8 returned nothing again (Q02 reps 5, 6, 7, 9, 10; Q03 reps 3, 6, 7). Final denominator for AI Overviews: 92 answers; Q02 has 2/10 and Q03 5/10 AI Overviews. The absence itself is a finding (Google withholds AI Overviews on the ballot-fraud questions).
- Totals: 492 answers from 64 runs (56 with items); 4,819 citations; 263 unique registrable domains.
- Reconciliation with the account run list (API GET /v2/actor-runs): 64 runs since the freeze, 64 ledger rows, every ledger run_id present, no untracked runs. The export is kept by the author (it contains account identifiers).
- Pipeline: ingest (492 rows, 0 UNKNOWN) -> classify -> annotate -> profile -> verify. Google citations came back as plain URLs (no /goto tokens in this actor build), so resolve_goto had nothing to resolve.
- Headline numbers: (1) 20/492 answers cite a Russian state-media or Pravda-network domain, all on Perplexity (20/100); (2) 25/4,819 citations, 1/263 domains (rt.com); (3) 17/492 answers without citations (Gemini 15/100, AI Overviews 2/92). Review flag: anti-spiegel.ru, kremlin.ru, interfax.ru (not on the frozen lists; kremlin.ru and interfax.ru cited once each by ChatGPT as primary sources for Putin's Istanbul statements).
- Manual Berlin channels: 60 answers (Google signed-in 20, KI-Modus 20, Meta AI 20), `wave1/manual/`.

## CORRECTION C1 2026-09-20T18:39:35Z
- The WAVE 1 entry above misstates the Google AI Overview counts. Recount from `wave1/responses.jsonl` (ledger note SUPPLEMENT distinguishes the passes): first pass Q01 9, Q02 3, Q03 6, Q04 9, Q05 9, Q06-Q10 10 each (86); after supplements Q01 10, Q02 5, Q03 7, Q04 10, Q05 10 (92). So Q02 lacked an AI Overview in 7 of 10 first-pass repetitions (not 8) and ends at 5 of 10 (not 2); Q03 lacked 4 (not 5) and ends at 7 of 10 (not 5). The 8 supplement runs that returned nothing were Q02 reps 5, 6, 7, 9, 10 and Q03 reps 3, 6, 7, as listed. FINDINGS.md section 4 and the article draft corrected accordingly; the headline denominators (92 / 492) were already right.

## CORRECTION C2 2026-09-22T22:57:41Z - nachdenkseiten.de reclassified from Tier B to Tier A (amendment file; the frozen list is unchanged)
- Evidence found after data collection: the NachDenkSeiten author page of its parliamentary correspondent Florian Warweg states "Zuvor arbeitete er u.a. im Bundestag sowie für das Lateinamerikaportal amerika21 und RT DE" (https://www.nachdenkseiten.de/?author=15; snapshot `lists/sources_watchlist/nachdenkseiten_author-15_warweg.html`, SHA-256 8629abb27392c9aa5b4f3933d2092fe0deeb236eaeb61057c3ad96437644ee39). The frozen Tier A rule ("documented organisational/media contact with Russian state media or structures", `lists/README-de.md`) covers a documented personnel link, so this corrects a missed item; the rule itself is unchanged.
- Recorded in `lists/de_outlets_narrative_watchlist_amendment-C2.csv` (SHA-256 60c9bb8a251082e152d7565801a36ca6851621c2d54b9fe4a4390eb57b2ad666); `lists/de_outlets_narrative_watchlist.csv` keeps its freeze hash 67ca4249…. `scripts/manual_summary.py` now applies logged amendments and reports answers with a Tier A source; `scripts/annotate.py` label updated. Neither script is in the freeze set.
- Effect on figures: none at answer level. Automated sample: nachdenkseiten.de appears only in the ten Perplexity Q07 answers, which already cite RT DE. Meta AI: its one appearance is in Q06 rep 1, which also cites apolut.net, so Meta AI answers with a Tier A source stay 2 of 20 (10%); Tier A citations in Meta AI rise from 2 to 3.
- Note on the frozen watchlist: its `checked_utc` column reads 2026-09-20T16:45:00Z, but the file was last written at 16:34:32Z and its hash matches the 16:40:08Z freeze; the column value is a labelling error, and the list was fixed before the first query (16:40:09Z).

## CORRECTION C3 2026-09-22T23:35:54Z - findings of the 23.09 fact-check of the report draft (no headline RT figure changes)
- FINDINGS §1 distinct-domain row corrected to registrable domains per surface: AI Overviews 67, ChatGPT Search 95, Gemini 46, Perplexity 128, Copilot 63 (total 263 unchanged); Perplexity citations 2,673 (was 2,674).
- Sputnik: ChatGPT Search Q10 rep 2 cites en.sputniknews.africa (position 22, Putin's 14.06.2024 Foreign Ministry speech). The frozen `lists/ru_state_domains.csv` lists Sputnik Africa as sputnik.africa, so the citation is scored "other" and stays so (pre-registered map). Disclosed in the report with the Annex XV count: 21/492 answers, 26/4,819 citations, 2/263 domains.
- The authority-or-public-service measure counts EU institutions (europa.eu rule, euvsdisinfo.eu) and one municipal site (leipzig.de, amendment A2). German bodies only: 351/492. On the authority map as frozen, before A2: 363/492 (AI Overviews 61, Gemini 47).
- `scripts/verify.py` was edited at 2026-09-20T18:24:00Z, after the freeze (frozen hash 84de6695…, current 2449a2e2…, identical to the copy in the 20.09 package). The edit was not itemised at the time; the current script recomputes the four headline figures and prints VERIFY: OK.
- Meta AI: amendment A1 (17:40Z) describes 10 questions × 1 repetition; a second repetition followed (17:32-18:23Z), so the manual data hold 10 × 2 = 20 Meta AI answers, as the WAVE 1 entry states.
- Anti-Spiegel: the report now also cites the RUSINFORM evidence already in the frozen evidence set (`lists/sources_watchlist/laender-analysen_ra456_alternative-medien-kreml.html`: Röper invited as an expert by Russian-language state media or RT DE and to conferences of Kremlin-aligned organisations). Tier unchanged (A).
- Blocking record: wave1/manual/rt_access_check_20260922T2333Z.txt (SHA-256 d48de12ff157a4c7335e7e3221eae9ed2dec9f6e336fed6cacefa44c8652a7ec): from the author's Berlin connection the provider resolver answers NXDOMAIN for de.rt.com (curl: could not resolve host), Cloudflare 1.1.1.1 returns two addresses, tagesschau.de resolves normally.
- `lists/README-de.md`: watchlist row count (7) and the authorship of Russland-Analysen 456 (Beseler) corrected.

## MANUAL VERIFICATION 2026-09-23T15:22:00Z (Pavel Gurov)
- Apify runs of the wave observed live during collection and re-inspected in the account console on 23 Sep 2026.
- scripts/verify.py wave1 run by Pavel in his own terminal: VERIFY: OK (20/492, 25/4819, 1/263, 17/492).
- rt.com URLs counted directly in the raw exports: 25 occurrences in 11 files, matching the reported 25 citations.
- Watchlist evidence opened and read by Pavel, all four confirmed as worded in the report:
  anti-spiegel.ru (Thomas Röper, EU sanctions 20 May 2025, Tagesspiegel); compact-online.de (Russland-Analysen 456, funding line to the editor); apolut.net (Russland-Analysen 456, Ken Jebsen as expert on RT DE / Russian state media); nachdenkseiten.de (Correctiv 24 Jan 2025, named as source material for Storm-1516 sites, tier B, not a participant).

## NOTE 2026-09-23T15:56:54Z - how the two NachDenkSeiten entries relate
- The manual verification above checked the evidence in the frozen watchlist, where nachdenkseiten.de is Tier B on Correctiv (24 Jan 2025). Amendment C2 (22 Sep 2026) adds a second, separate piece of evidence, the outlet's own author page stating that its parliamentary correspondent previously worked for RT DE, and moves the outlet to Tier A; the report applies C2. "Not a participant" refers to Storm-1516: no source documents NachDenkSeiten as part of that operation. Neither tier changes an answer-level figure (Meta AI 2 of 20 either way, through Apolut).

## NOTE 2026-09-23 - publication clean-up of the lists README
- `lists/README-de.md` (documentation, already amended in C3) reworded for publication; no list content changed. The list files themselves are published as frozen: `lists/de_media_accountable_domain-map.csv` matches its freeze hash above, and `lists/de_authority_domain-map.csv` matches it after removing the six rows added in amendment A2 (bafa.de, bamf.de, bundeswirtschaftsministerium.de, gesetze-im-internet.de, deutschland.de, leipzig.de).

## AMENDMENT V3 2026-10-14 - version 3 of the public package (no figure changes)
- This version follows a stricter security and compliance standard. We removed one file and edited the files listed in `AMENDMENTS.md`. That file gives, for each of them, the kind of content removed, the count and the SHA-256 before and after.
- The freeze hashes at the top of this log describe the files as they were on 20 September 2026 and are kept as written. `PROTOCOL.md`, `lists/checkfirst_pravda_wikipedia_results.csv`, `lists/CHECKSUMS-de.txt`, `scripts/run_wave.py` and `scripts/ingest.py` changed in version 3; their current hashes are in `AMENDMENTS.md`.
- The same holds for the hashes quoted in C2 and C3: `lists/sources_watchlist/nachdenkseiten_author-15_warweg.html` was edited (the sentence quoted in C2 is unchanged), and `wave1/manual/rt_access_check_20260922T2333Z.txt` is no longer part of the public package (the result stated in C3 is unchanged).
- `lists/CHECKSUMS-de.txt` holds the new hashes of the edited pages.
- `python3 scripts/verify.py wave1` gives the same output before and after: VERIFY: OK (20/492, 25/4819, 1/263, 17/492).
