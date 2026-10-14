#!/usr/bin/env python3
"""annotate.py - descriptive researcher annotation of 'other' domains (not list-based; never used in headline numbers).
Usage: python3 scripts/annotate.py wave1 -> <wave>/domains_annotated.csv ; prints unannotated 'other' domains with >=3 citations."""
import csv, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent; wave = sys.argv[1] if len(sys.argv) > 1 else "wave1"
A = {
 # fact-checkers and news agencies
 "correctiv.org": ("factcheck", "CORRECTIV, non-profit investigative newsroom and fact-checker (Essen)"),
 "dpa-factchecking.com": ("factcheck", "dpa fact-check (German press agency)"), "afp.com": ("factcheck", "AFP Faktencheck"),
 "mimikama.org": ("factcheck", "Mimikama, Austrian fact-checking association"), "gadmo.eu": ("factcheck", "GADMO, German-Austrian EDMO hub"),
 "reuters.com": ("intl_media", "Reuters"), "euronews.com": ("intl_media", "Euronews"), "apnews.com": ("intl_media", "Associated Press"),
 "theguardian.com": ("intl_media", "The Guardian"), "bbc.com": ("intl_media", "BBC"), "nytimes.com": ("intl_media", "New York Times"),
 "politico.eu": ("intl_media", "Politico Europe"), "cnn.com": ("intl_media", "CNN"), "derstandard.at": ("intl_media", "Der Standard (Austria)"),
 "journal21.ch": ("intl_media", "Journal21, Swiss online journal (former Swiss editors)"), "bazonline.ch": ("intl_media", "Basler Zeitung (Switzerland)"),
 "srf.ch": ("intl_media", "SRF, Swiss public broadcaster"), "orf.at": ("intl_media", "ORF, Austrian public broadcaster"),
 # German media not on the accountable/DNR lists
 "taz.de": ("de_media_other", "taz, die tageszeitung (Berlin daily)"), "n-tv.de": ("de_media_other", "n-tv (RTL group news channel)"),
 "berliner-zeitung.de": ("de_media_other", "Berliner Zeitung"), "fr.de": ("de_media_other", "Frankfurter Rundschau"),
 "tagesspiegel.de": ("de_media_other", "Der Tagesspiegel (Berlin)"), "rnd.de": ("de_media_other", "RedaktionsNetzwerk Deutschland (Madsack)"),
 "web.de": ("de_media_other", "web.de news portal (United Internet, dpa-based)"), "t-online.de": ("de_media_other", "t-online (Ströer news portal)"),
 "merkur.de": ("de_media_other", "Münchner Merkur"), "morgenpost.de": ("de_media_other", "Berliner Morgenpost"), "bz-berlin.de": ("de_media_other", "B.Z. (Berlin tabloid)"),
 "nordkurier.de": ("de_media_other", "Nordkurier (Mecklenburg-Vorpommern regional daily)"), "svz.de": ("de_media_other", "Schweriner Volkszeitung"),
 "mz.de": ("de_media_other", "Mitteldeutsche Zeitung"), "lto.de": ("de_media_other", "Legal Tribune Online (legal news)"), "capital.de": ("de_media_other", "Capital (business magazine, RTL group)"),
 "telepolis.de": ("de_media_other", "Telepolis (Heise online magazine, opinion-heavy)"), "wirtschaftsdienst.eu": ("academic", "Wirtschaftsdienst (ZBW economics journal)"),
 "swp-berlin.org": ("academic", "Stiftung Wissenschaft und Politik (German Institute for International and Security Affairs)"),
 "lpb-bw.de": ("de_public_info", "Landeszentrale für politische Bildung Baden-Württemberg"), "iwkoeln.de": ("academic", "Institut der deutschen Wirtschaft"),
 "diw.de": ("academic", "DIW Berlin"), "ifw-kiel.de": ("academic", "Kiel Institute for the World Economy"), "statista.com": ("business", "Statista"),
 "abgeordnetenwatch.de": ("ngo", "abgeordnetenwatch.de (parliamentary transparency NGO)"), "vorwaerts.de": ("party_media", "vorwärts (SPD party paper)"),
 "afdbundestag.de": ("party_media", "AfD parliamentary group"), "afd.de": ("party_media", "AfD"), "kommunistischepartei.de": ("party_media", "Kommunistische Partei (KPD) site"),
 "politeknik.de": ("blog", "Politeknik (German-Turkish political magazine)"), "makroskop.eu": ("de_altmedia", "Makroskop (heterodox economics magazine)"),
 "overton-magazin.de": ("de_altmedia", "Overton Magazin (Telepolis founders' successor; not on watchlist, no documented Kremlin link found)"),
 "freitag.de": ("de_media_other", "der Freitag (weekly)"), "welttrends.de": ("academic", "WeltTrends (Potsdam foreign-policy journal)"),
 "friedenskooperative.de": ("ngo", "Netzwerk Friedenskooperative (peace movement)"), "gea-waldviertler.at": ("blog", "GEA Waldviertler company blog (Austria)"),
 "wikipedia.org": ("reference", "Wikipedia"), "youtube.com": ("social_platform", "YouTube"), "facebook.com": ("social_platform", "Facebook"),
 "instagram.com": ("social_platform", "Instagram"), "tiktok.com": ("social_platform", "TikTok"), "reddit.com": ("social_platform", "Reddit"),
 "x.com": ("social_platform", "X"), "linkedin.com": ("social_platform", "LinkedIn"), "medium.com": ("social_platform", "Medium"), "substack.com": ("social_platform", "Substack"),
 "gutefrage.net": ("social_platform", "gutefrage.net Q&A"), "1und1.de": ("de_media_other", "1&1 news portal (United Internet, dpa-based)"),
 # watchlist and flagged (descriptive here; tiers live in lists/de_outlets_narrative_watchlist.csv)
 "nachdenkseiten.de": ("de_altmedia", "NachDenkSeiten - watchlist Tier A by amendment C2 (personnel link to RT DE; Tier B in the frozen list)"), "anti-spiegel.ru": ("ru_flag", "Anti-Spiegel (Thomas Röper, EU-sanctioned) - watchlist Tier A, .ru TLD"),
 "compact-online.de": ("de_altmedia", "COMPACT magazine - watchlist Tier A"), "apolut.net": ("de_altmedia", "Apolut - watchlist Tier A"),
 "kremlin.ru": ("ru_flag", "kremlin.ru, official site of the Russian president (not on Annex XV; .ru flag)"), "interfax.ru": ("ru_flag", "Interfax news agency (.ru flag)"),
 "tkp.at": ("de_altmedia", "tkp.at (Austrian alternative blog)"), "kofner.de": ("blog", "Kofner, economist's site arguing for normalisation with Russia"),
 "te.legra.ph": ("social_platform", "Telegraph (Telegram's anonymous publishing tool)"), "alethonews.com": ("altmedia_intl", "Aletho News (conspiracy aggregator)"),
 "earthpressnews.com": ("aggregator", "earthpressnews.com (anonymous aggregator)"), "neueste-nachrichten.eu": ("aggregator", "anonymous German news aggregator"),
 "weltweite-news.de": ("aggregator", "anonymous German news aggregator"), "europesays.com": ("aggregator", "anonymous aggregator"),
 "rathausnachrichten.de": ("aggregator", "anonymous local-news aggregator"), "shuffleschau.de": ("aggregator", "anonymous aggregator"),
 "operanewsapp.com": ("aggregator", "Opera News aggregator"), "thedailydigest.com": ("aggregator", "The Daily Digest (content farm)"),
 "watson.ch": ("intl_media", "watson.ch (Swiss news portal)"), "nzz.ch": ("intl_media", "Neue Zürcher Zeitung"), "kurier.at": ("intl_media", "Kurier (Austria)"),
 "france24.com": ("intl_media", "France 24"), "washingtonpost.com": ("intl_media", "Washington Post"), "foreignaffairs.com": ("intl_media", "Foreign Affairs"),
 "foreignpolicy.com": ("intl_media", "Foreign Policy"), "novinky.cz": ("intl_media", "Novinky.cz (Czech)"), "monde-diplomatique.de": ("de_media_other", "Le Monde diplomatique, German edition (taz)"),
 "csis.org": ("think_tank", "CSIS (Washington)"), "cfr.org": ("think_tank", "Council on Foreign Relations"), "lawfaremedia.org": ("think_tank", "Lawfare"),
 "ifo.de": ("academic", "ifo Institute"), "kielinstitut.de": ("academic", "Kiel Institute"), "econstor.eu": ("academic", "EconStor (ZBW)"), "idw-online.de": ("academic", "Informationsdienst Wissenschaft"),
 "uni-stuttgart.de": ("academic", "University of Stuttgart"), "uni-frankfurt.de": ("academic", "Goethe University Frankfurt"), "zeithistorische-forschungen.de": ("academic", "Zeithistorische Forschungen (ZZF Potsdam)"),
 "d-nb.info": ("academic", "Deutsche Nationalbibliothek catalogue"), "springerprofessional.de": ("academic", "Springer Professional"), "palquest.org": ("academic", "Interactive Encyclopedia of the Palestine Question"),
 "nato.int": ("intl_org", "NATO"), "un.org": ("intl_org", "United Nations"), "imf.org": ("intl_org", "IMF"), "president.gov.ua": ("foreign_gov", "Office of the President of Ukraine"),
 "investing.com": ("business", "Investing.com"), "ihk.de": ("business", "IHK (chambers of commerce)"), "kettner-edelmetalle.de": ("business", "Kettner Edelmetalle (precious-metals dealer blog, Kremlin-friendly framing)"),
 "kettner-edelmetalle.li": ("business", "Kettner Edelmetalle (Liechtenstein site)"), "swg-mobil.de": ("business", "SWG (company site)"),
 "tag24.de": ("de_media_other", "TAG24 (Dresden tabloid portal)"), "derwesten.de": ("de_media_other", "DerWesten (Funke)"), "ksta.de": ("de_media_other", "Kölner Stadt-Anzeiger"),
 "rhein-zeitung.de": ("de_media_other", "Rhein-Zeitung"), "suedkurier.de": ("de_media_other", "Südkurier"), "schwaebische.de": ("de_media_other", "Schwäbische Zeitung"),
 "rp-online.de": ("de_media_other", "Rheinische Post"), "mopo.de": ("de_media_other", "Hamburger Morgenpost"), "moz.de": ("de_media_other", "Märkische Oderzeitung"),
 "abendblatt.de": ("de_media_other", "Hamburger Abendblatt"), "express.de": ("de_media_other", "Express (Cologne tabloid)"), "shz.de": ("de_media_other", "sh:z (Schleswig-Holstein)"),
 "wa.de": ("de_media_other", "Westfälischer Anzeiger"), "hna.de": ("de_media_other", "HNA (Kassel)"), "regionalheute.de": ("de_media_other", "regionalHeute.de (Braunschweig)"),
 "antenne.de": ("de_media_other", "Antenne Bayern"), "radioeins.com": ("de_media_other", "radioeins (rbb)"), "gmx.ch": ("de_media_other", "GMX Switzerland news portal"),
 "nd-aktuell.de": ("de_media_other", "nd (neues deutschland, left daily)"), "blaetter.de": ("de_media_other", "Blätter für deutsche und internationale Politik"),
 "emma.de": ("de_media_other", "EMMA (feminist magazine)"), "juedische-allgemeine.de": ("de_media_other", "Jüdische Allgemeine"), "das-parlament.de": ("de_public_info", "Das Parlament (Bundestag weekly)"),
 "jungefreiheit.de": ("de_altmedia", "Junge Freiheit (right-wing weekly; not on watchlist, no documented Kremlin link)"), "jf-archiv.de": ("de_altmedia", "Junge Freiheit archive"),
 "tichyseinblick.de": ("de_altmedia", "Tichys Einblick (right-liberal; not on watchlist)"), "exxpress.at": ("de_altmedia", "exxpress (Austrian right-wing portal; not on watchlist)"),
 "nius.de": ("de_altmedia", "NIUS (Reichelt; not on watchlist)"), "unser-mitteleuropa.com": ("de_altmedia", "Unser Mitteleuropa (far-right network; no Russia-specific evidence found)"),
 "ansage.org": ("de_altmedia", "Ansage! (right-wing blog)"), "alexander-wallasch.de": ("de_altmedia", "Alexander Wallasch (right-wing blog)"), "oval.media": ("de_altmedia", "OVALmedia (conspiracy-adjacent media)"),
 "fakten-stammtisch.de": ("blog", "fakten-stammtisch.de (blog)"), "rabenspiegel.de": ("blog", "Rabenspiegel (blog)"), "ausserhalbdesoffiziellenprogramms.de": ("blog", "blog"),
 "netz-trends.de": ("blog", "netz-trends.de (blog)"), "infosperber.ch": ("altmedia_intl", "Infosperber (Swiss alternative site)"), "dasreich.com.tr": ("aggregator", "dasreich.com.tr (Turkish-hosted German content site)"),
 "aufstehen-steinlach-wiesaz.de": ("blog", "local Aufstehen movement group"), "weltoffen-bonn.de": ("ngo", "Weltoffen Bonn (local initiative)"), "nds-fluerat.org": ("ngo", "Flüchtlingsrat Niedersachsen"),
 "ippnw.de": ("ngo", "IPPNW Germany"), "humanistische-union.de": ("ngo", "Humanistische Union"), "rosalux.de": ("party_foundation", "Rosa-Luxemburg-Stiftung (Die Linke)"),
 "akweb.de": ("de_altmedia", "analyse & kritik (left monthly)"), "evangelisch.de": ("ngo", "evangelisch.de (Protestant church portal)"), "spektrum-islam.de": ("blog", "spektrum-islam.de"),
 "zenith.me": ("de_media_other", "zenith (Middle East magazine)"), "dbwv.de": ("ngo", "Deutscher BundeswehrVerband"), "leadstories.com": ("factcheck", "Lead Stories"),
 "paz.de": ("de_altmedia", "Preußische Allgemeine Zeitung (Landsmannschaft Ostpreußen)"), "jkn.co.kr": ("aggregator", "jkn.co.kr (Korean-hosted aggregator)"), "bild.de": ("de_media_other", "Bild"),
}
rows = list(csv.DictReader(open(ROOT / wave / "domains.csv", encoding="utf-8")))
out = []; missing = []
for r in rows:
    t, note = A.get(r["domain"], ("", ""))
    if r["category"] == "other" and not t and int(r["citations"]) >= 3: missing.append((r["domain"], r["citations"]))
    out.append({**r, "annotation_type": t, "annotation": note})
with open(ROOT / wave / "domains_annotated.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
print(f"annotated {sum(1 for o in out if o['annotation'])}/{len(out)} domains; unannotated 'other' with >=3 citations: {missing}")
