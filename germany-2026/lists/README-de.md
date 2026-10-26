# Germany 2026 domain classification lists

Retrieval date: 2026-09-20 (Europe/Berlin). All three CSVs are UTF-8, comma-separated, with a header row. Every row cites the specific page it was confirmed against; the retrieved original of each cited page is saved next to this README (folders `sources_impressum/`, `sources_authority/`, `sources_media/`, plus `ard_die-ard.html`, `bva_domainverwaltung.html`, `presserat_selbstverpflichtung.html` at the top level) so it can be hashed — see `CHECKSUMS-de.txt`. No `.ru` sources and no Russian-language pages were used anywhere.

## 1. de_public_service_domains.csv (30 rows)

Germany's public-service broadcasters: ARD, its nine Landesrundfunkanstalten, ZDF, Deutschlandradio (and its three programmes), Deutsche Welle, and the ARD/ZDF joint offerings.

**Primary basis for most rows:** `https://www.ard.de/die-ard/` (saved as `ard_die-ard.html`) — ARD's own official page, which directly links every Landesrundfunkanstalt and every joint offering (tagesschau.de, sportschau.de, ardmediathek.de, ardsounds.de, kika.de, funk.net, phoenix.de, 3sat.de, arte.tv, zdf.de, deutschlandradio.de, dw.com) from its own markup. This single page is the strongest available basis: ARD's own list of its Landesrundfunkanstalten and Gemeinschaftseinrichtungen.

**Secondary basis, per row, where the domain isn't directly linked from ard.de:** the outlet's own Impressum or an HTTP redirect confirming it belongs to the broadcaster (rbb24.de, br24.de, hessenschau.de, butenunbinnen.de, zdfheute.de, daserste.de, ardsounds.de). These are saved in `sources_impressum/`.

Findings worth flagging:
- **ARD Audiothek is gone as a brand/domain.** `ardaudiothek.de` now issues an HTTP 301 redirect to `ardsounds.de`. The CSV lists `ardsounds.de` as the live domain and notes the redirect.
- **rbb's classic domain now redirects.** `rbb-online.de` (the domain ARD's own page links) redirects to `rbb24.de`. The CSV lists `rbb24.de`.
- **`daserste.de` and `br24.de` are now redirects, not independent sites** (to `ardmediathek.de/daserste` and `br.de/nachrichten/` respectively). Both still resolve and are still controlled by ARD/BR, so they are included with that noted.

### Not included (public-service list)
- `sr-online.de` — does not resolve (connection failure) as of 2026-09-20; SR's live domain is `sr.de`.
- `swraktuell.de` — does not resolve; SWR's regional news lives at `swr.de`, no standalone "SWR Aktuell" domain was found.
- `tagesschau24.de` — resolves but only as a redirect into a `tagesschau.de` livestream page; not treated as an independent offering worth a separate row (tagesschau.de is already listed).

## 2. de_authority_domain-map.csv (56 rows)

Columns: `domain,body,level,basis,source_url`. `level` is one of `federal`, `land`, `eu`, or `rule`.

**Federal rule row:** `bund.de` — basis is the Bundesverwaltungsamt's (BVA) own page (`sources_authority/bva_domainverwaltung.html`) stating it has administered subdomains of the second-level domain `*.bund.de` for the federal administration since April 2013 (its own example: `www.bva.bund.de`). Any `*.bund.de` hostname belongs to a federal body.

**EU rule row:** `europa.eu` — the shared portal domain of the EU institutions; every EU subdomain in this list (`ec.europa.eu`/`commission.europa.eu`, `europarl.europa.eu`, `consilium.europa.eu`, `eeas.europa.eu`) sits under it. Corroborated by Wikipedia's "Europa (web portal)" article (used only as a pointer to primary sources, not as a basis), saved as `sources_authority/wikipedia_europa_web_portal.html`.

**Federal bodies:** each row's basis is the body's own official website (self-evident from the domain plus the site itself, e.g. `bundestag.de`, `bundesbank.de`, `bundeswehr.de`). Several (`bnd.bund.de`, `bsi.bund.de`, `bmi.bund.de`) additionally fall under the `*.bund.de` rule above.

**Länder:** the 16 state government portals, each cited to its own official page. Two domain corrections versus the initial candidate list:
- `mv-regierung.de` does not resolve. Mecklenburg-Vorpommern's live portal is `regierung-mv.de` (and `mecklenburg-vorpommern.de` 301-redirects to it). The CSV uses `regierung-mv.de`.
- `bremen.de` returns HTTP 403 to automated fetches (bot protection) but is the established, widely-used official domain for the Freie Hansestadt Bremen; included with that caveat noted in `basis`.

**State election authorities / parliaments:** `wahlen-berlin.de`, `laiv-mv.de` (Mecklenburg-Vorpommern's Landeswahlleiter function), `wahlen.sachsen-anhalt.de`, `statistik.sachsen-anhalt.de` (Sachsen-Anhalt's Landeswahlleitung sits with the state statistical office), `parlament-berlin.de`, `landtag-mv.de`.

**State Verfassungsschutz domains:** found via the Bundesamt für Verfassungsschutz's own official page listing all 16 Landesbehörden (`sources_authority/verfassungsschutz_landesbehoerden.html`). Only the three that are genuinely separate registrable domains (not subdomains/paths of a Land portal already listed above) were added: `verfassungsschutz-bw.de` (Baden-Württemberg), `verfassungsschutz-mv.de` (Mecklenburg-Vorpommern), `im.nrw` (Ministerium des Innern NRW, which runs Verfassungsschutz NRW). The other 13 Länder run their Verfassungsschutz function as a subdomain or path of the Land portal already listed in this CSV (e.g. `lfv.hessen.de`, `verfassungsschutz.bayern.de`, `berlin.de/sen/inneres/verfassungsschutz`) and were not duplicated as separate rows.

### Not included / not verified (authority list)
- `mv-regierung.de`, `bmwk.de` — dead domains, see corrections above (`bmwe.de` used for the economy ministry instead; the ministry appears to have been renamed/re-domained under the current coalition).
- Separate Landeswahlleiter domains for Bavaria, Baden-Württemberg, NRW, Hessen and Niedersachsen were not added as extra rows: in each case the function is hosted as a subdomain or path of the Land's own portal domain already listed (e.g. `landeswahlleiter.niedersachsen.de` under `niedersachsen.de`, `wahlen.hessen.de` under `hessen.de`), except Bavaria's `statistik.bayern.de`, which is a genuinely separate registrable domain but was not independently confirmed as of the retrieval date and so is left out rather than guessed.
- `sr-online.de` (see List 1) is not an authority domain either; not relevant here.

## 3. de_media_accountable_domain-map.csv (7 rows)

Columns: `domain,outlet,basis,list_entry,source_url`.

**What we found on presserat.de:** the Deutscher Presserat does **not** publish a downloadable list of publishers/outlets that signed the Selbstverpflichtungserklärung. Its own page on the subject (`presserat_selbstverpflichtung.html`) explains that most German publishers commit via a written declaration and that many editorial offices simply note in their own Impressum that they follow the Pressekodex — there is no public roster to scrape or cite per-domain.

**Fallback source:** the BDZV (Bundesverband Digitalpublisher und Zeitungsverleger e.V.) runs a public, browsable member directory at `bdzv.de/der-bdzv/mitgliederverlage` (223 entries as of retrieval, saved as `sources_media/bdzv_mitgliederverlage.html`). Each member has its own detail page linking to its live website. Seven target outlets were confirmed this way, with the individual BDZV detail page saved for each in `sources_media/bdzv_entries/`:
Süddeutsche Zeitung → sueddeutsche.de, Frankfurter Allgemeine Zeitung → faz.net, Die Welt → welt.de, Handelsblatt → handelsblatt.com (its BDZV-listed domain `handelsblatt.de` redirects to `.com`), Ostsee-Zeitung → ostsee-zeitung.de, Volksstimme → volksstimme.de, Leipziger Volkszeitung → lvz.de.

**MVFP (Medienverband der freien Presse)** was also checked (its member directory is organised alphabetically by publishing-company name, saved partially as `sources_media/mvfp_S.html` and `sources_media/mvfp_F.html`), but it lists corporate names (e.g. "FUNKE Mediengruppe GmbH & Co. KGaA"), not the media brands/domains this list needs, and none of the target brand-to-company mappings could be confirmed reliably as of the retrieval date.

### Not included (media list)
The following requested outlets could **not** be matched to a specific list entry as of the retrieval date, so under the inclusion rule they are left out rather than assumed:
`spiegel.de, zeit.de, bild.de, tagesspiegel.de, stern.de, focus.de, t-online.de, n-tv.de, rtl.de, taz.de, fr.de, berliner-zeitung.de, morgenpost.de, bz-berlin.de, nordkurier.de, svz.de, mz.de`.

Reasons:
- Their own Impressum pages (fetched and saved in `sources_media/`) do not contain a machine-readable Presserat/Pressekodex statement — several of these sites are JavaScript-rendered single-page apps where the raw HTML fetch does not carry the full rendered legal text, and none of the ones that did return static HTML mentioned "Presserat" or "Pressekodex" in the fetched markup.
- BDZV's member directory has no bulk index or search endpoint reachable by simple HTTP fetch (its listing/pagination is JavaScript-driven); slugs were guessed for likely candidates (`bild`, `tagesspiegel`, `berliner-zeitung`, `frankfurter-rundschau`, `taz`, `stern`, `focus`, `mitteldeutsche-zeitung`, `nordkurier`, `schweriner-volkszeitung`, and variants) and all returned HTTP 404, meaning either they are not BDZV members under that slug or the slug pattern differs from the confirmed examples.
- Press coverage found during this research states the SV-Gruppe (publisher of Nordkurier and the Schweriner Volkszeitung, i.e. `svz.de`) has left the BDZV, so those two were not assumed to be current members even speculatively.
- Spiegel, Stern and Focus are magazine-style publishers whose natural association is MVFP rather than BDZV; MVFP's directory, as noted above, could not be mapped from company name to brand domain as of the retrieval date.

None of this means these outlets are not Presserat-bound in reality — most large German dailies are — it means no specific, citable list entry could be produced for them as of the retrieval date, and the inclusion rule is to leave such domains out rather than include them on general reputation.

## 4. de_outlets_narrative_watchlist.csv (7 rows, including anti-spiegel.ru at Tier A; amendment C2 in de_outlets_narrative_watchlist_amendment-C2.csv moves nachdenkseiten.de to Tier A)

Pre-registered evidence table of German-language outlets with **documented** pro-Kremlin-narrative evidence, for the source audit of the AI-answer-surface study (`PROTOCOL.md` §5: "outlets carrying a documented narrative with Tier A/B evidence"). Columns: `domain,outlet,tier,evidence,evidence_url,evidence_date,checked_utc`. Retrieved originals of every cited page are saved in `sources_watchlist/`; hashes appended to `CHECKSUMS-de.txt`. No `.ru` sources, no Russian-language pages.

**Tier A — documented organisational/media contact with Russian state media or structures:**
- `compact-online.de` (Compact) — Arista Beseler's RUSINFORM case study (Universität Passau/ERC; summary of Beseler & Toepfl's peer-reviewed article, published in the Bundeszentrale für politische Bildung's *Russland-Analysen* Nr. 456, 11.10.2024 — `laender-analysen_ra456_alternative-medien-kreml.html`): Compact cooperated with the Kremlin-linked think tank "Institut für Demokratie und Zusammenarbeit" (Institute for Democracy and Cooperation), with financial support flowing directly to editor-in-chief Jürgen Elsässer; Elsässer also cooperated with Russian-language state media/RT DE. (Separately, the BfV classified Compact as *gesichert rechtsextremistisch* and the BMI banned Compact-Magazin GmbH on 16.07.2024; the Bundesverwaltungsgericht lifted that ban on 24.06.2025 on press-freedom/proportionality grounds without disputing the anti-constitutional content finding — not used as the Tier A basis here since that ban was about domestic extremism, not the Russia link.)
- `anti-spiegel.ru` (Anti-Spiegel, Thomas Röper) - Council Decision (CFSP) 2025/966 of 20 May 2025 lists Röper for spreading disinformation supporting Russia's war; in July 2023 he co-launched "Anti-Spiegel TV" with RT DE staffer Dominik Reichert (*Russland-Analysen* Nr. 456). The `.ru` site itself was not opened; the evidence comes from German- and English-language sources.
- `apolut.net` (Apolut) — same RUSINFORM study: Ken Jebsen, Apolut's creative director, "wurde als Experte in russischsprachige Staatsmedien oder RT DE eingeladen und verweist ... in eigenen Artikeln" darauf; the study also documents his personal ties to RT DE's former editor-in-chief Ivan Rodionov.
- `weltwoche.ch` (Weltwoche) — `medienwoche.ch`, 24.02.2022 (`medienwoche_weltwoche-putins-nuetzliche-idioten.html`), corroborated by `de.wikipedia.org/wiki/Thomas_Fasbender` (`wikipedia_de_thomas-fasbender.html`): Thomas Fasbender hosted a weekly talk show on Russian state broadcaster RT DE (2019–2022, *Fasbenders Woche*), on which Weltwoche editor-in-chief Roger Köppel appeared as a guest; Fasbender also wrote for Weltwoche. (A March 2024 Bavarian Verfassungsschutz report separately named `weltwoche.de` among outlets whose articles a pro-Russian bot campaign redistributed, then walked that framing back after protest — not used as the Tier A basis here, since the revised report stopped short of alleging the outlet itself had Kremlin contact.)

**Tier B — content matches a catalogued disinformation case, no documented organisational link:**
- `nachdenkseiten.de` (NachDenkSeiten) and `philosophia-perennis.com` (Philosophia Perennis) — Correctiv, in cooperation with NewsGuard and the Gnida Project, 24.01.2025 (`correctiv_storm1516-german-election-en.html`): the Storm-1516 fake-news network's AI-paraphrased articles were sourced from "right-wing media outlets like Compact and Philosophia Perennis, or pro-Russian blogs like Nachdenkseiten and the German arm of Russia's state-controlled RT news channel."
- `report24.news` (Report24) — Correctiv, 23.09.2021 (`correctiv_report24-wochenblick-2021.html`): "Report24 schrieb im Juni ebenfalls aus russischer Sicht: „Will Großbritannien Krieg mit Russland provozieren? Vorfall im schwarzen Meer"" — Correctiv's own framing ("aus russischer Sicht") with no claimed organisational link ("Auch wenn es keine Verbindungen nach Russland geben sollte ..."). Corroborated by CeMAS's domain analysis of the ten largest German-language conspiracy-ideological Telegram channels during the first week of the 2022 invasion (`cemas_telegram-rt-ukraine.html`, published 18.03.2022): report24.news was the **second** most-shared news domain (2,229 links) after RT DE itself (5,772), ahead of welt.de and anti-spiegel.ru.

### Not included (narrative watchlist)

Checked and left out because no Tier A or Tier B evidence meeting the standard in `PROTOCOL.md` §5 could be found as of the retrieval date (content/editorial criticism alone, or presence in an unrelated far-right/disinformation network, is not sufficient):

- `journalistenwatch.com`, `pi-news.net` — the same RUSINFORM study (Beseler 2024, summarising Beseler & Toepfl 2024) explicitly found these two are **not** Kremlin-connected: it describes them as taking a "selbsterklärte proamerikanische Sichtweise" and notes Journalistenwatch is funded by the US-based Middle East Forum.
- `jungefreiheit.de`, `tichyseinblick.de` — the same study names these among the outlets whose editors-in-chief "haben sich ... entschieden vom Kreml distanziert" (explicitly distanced themselves from the Kremlin); no other Tier A/B evidence was found.
- `deutsche-wirtschafts-nachrichten.de` — widely described in press criticism (Vice.de and others) as having a "pro-Russian editorial bias," but no specific EUvsDisinfo case, BfV/Landesverfassungsschutz finding, sanction, or CeMAS/Correctiv/dpa-Faktencheck/Gnida/VIGINUM narrative-match citation could be located.
- `freiewelt.net`, `epochtimes.de`, `exxpress.at`, `nius.de`, `overton-magazin.de` — no documented Kremlin/pro-Russian-narrative case found. (`epochtimes.de` appears in the same CeMAS Telegram domain-sharing ranking as report24.news — 1,541 shared links, 6th place — but that reflects the same conspiracy-Telegram audience sharing it, not a documented pro-Kremlin content match; Epoch Times' own editorial line is anti-CCP, not pro-Kremlin, so it is excluded.)
- `unser-mitteleuropa.com` — Correctiv (21.09.2022) and netzpolitik.org document it as the hub of an anti-migration, anti-LGBT far-right media network with FPÖ/AfD/Fratelli d'Italia ties, but neither piece, read directly, documents a pro-Kremlin narrative match or Russia organisational link specific to this outlet.
- `multipolar-magazin.de` — BR24 (26.03.2024) reported ties between Multipolar and anti-spiegel.ru, the Querdenken network and Swiss Policy Research, and one Multipolar publication was co-authored with Compact's Jürgen Elsässer; not included because this is BR24's own reporting, not an EUvsDisinfo case or a CeMAS/Correctiv/dpa-Faktencheck/Gnida/VIGINUM documented narrative match, which the Tier B standard requires — flagged here rather than assumed.
- `wochenblick.at`, `auf1.tv`/AUF1, Info-Direkt — named alongside Report24 in the same 23.09.2021 Correctiv piece as part of the same Austrian disinformation cluster, but the specific disinformation examples Correctiv documents for them (e.g. a fabricated claim about Annalena Baerbock's university degree) are domestic-politics fakes, not pro-Kremlin narratives; left out for lack of a Russia-specific match, not re-verified for current live domains.
