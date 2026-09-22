#!/usr/bin/env python3
"""Re-read the GitHub stars list and diff it against data/projects.json.

    python3 scripts/refresh_list.py            # report only
    python3 scripts/refresh_list.py --write    # also refresh stars/updated/license

Additions are NOT written automatically: a new entry needs the annotation pass in
docs/evaluation-criteria.md, which means reading its README. This script tells you
which ones are outstanding and stubs them if you pass --write.

There is no GitHub API for stars lists, so the list itself is scraped from HTML.
Repo metadata comes from the REST API via `gh`.
"""

import argparse
import html
import json
import re
import subprocess
import sys
import urllib.request
from datetime import date
from pathlib import Path

LIST_URL = "https://github.com/stars/danielrosehill/lists/android-voice-keyboards"
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "projects.json"


def scrape_list(url=LIST_URL):
    """Return [{slug, desc, lang, stars, updated}] from the rendered list page.

    The list is paginated at 30 entries; ?page=N is honoured even past the end,
    so stop when a page yields nothing rather than trusting the count in the
    header.
    """
    out, seen = [], set()
    for page in range(1, 20):
        req = urllib.request.Request(
            f"{url}?page={page}", headers={"User-Agent": "android-voice-keyboard-roundup"}
        )
        body = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
        # Each entry opens with <h2 class="h3">; splitting on it is more robust
        # than matching the surrounding div, whose classes GitHub churns.
        chunks = re.split(r'<h2 class="h3">', body)[1:]
        if not chunks:
            break
        before = len(seen)
        for chunk in chunks:
            m = re.search(r'<a href="/([^"]+)">', chunk)
            if not m or m.group(1) in seen:
                continue
            seen.add(m.group(1))
            d = re.search(r'itemprop="description">\s*(.*?)\s*</p>', chunk, re.S)
            lang = re.search(r'itemprop="programmingLanguage">([^<]+)<', chunk)
            stars = re.search(r'/stargazers">.*?</svg>\s*([\d,]+)', chunk, re.S)
            upd = re.search(r'Updated\s*<relative-time[^>]*datetime="([^"]+)"', chunk)
            out.append(
                {
                    "slug": m.group(1),
                    "desc": html.unescape(re.sub(r"<[^>]+>", "", d.group(1)).strip()) if d else "",
                    "lang": lang.group(1) if lang else "unknown",
                    "stars": int(stars.group(1).replace(",", "")) if stars else 0,
                    "updated": upd.group(1)[:10] if upd else None,
                }
            )
        if len(seen) == before:
            break
    return out


def gh_meta(slug):
    """License SPDX id and archived flag, or None if `gh` cannot see the repo."""
    try:
        raw = subprocess.run(
            ["gh", "api", f"repos/{slug}", "--jq", "[.license.spdx_id, .archived] | @tsv"],
            capture_output=True, text=True, timeout=30, check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return None
    spdx, archived = (raw.split("\t") + ["", ""])[:2]
    return {"license": spdx or "NOASSERTION", "archived": archived == "true"}


def stub(entry):
    """A new row with every judgement left as `unknown`.

    Deliberately not guessed from the one-line description — see the voxboard
    entry for why a catalogue blurb is not evidence.
    """
    return {
        "id": entry["slug"].split("/")[-1].lower(),
        "name": entry["slug"].split("/")[-1],
        "slug": entry["slug"],
        "url": f"https://github.com/{entry['slug']}",
        "source": "stars-list",
        "category": "keyboard",
        "lang": entry["lang"],
        "license": "unknown",
        "stars": entry["stars"],
        "updated": entry["updated"],
        "form": {"voice_ime": "unknown", "full_keyboard": "unknown", "floating_button": "unknown"},
        "engine": {"local": "unknown", "cloud": "unknown", "fallback": "unknown",
                   "system_delegated": "unknown"},
        "models": {"whisper": "unknown", "moonshine": "unknown", "nvidia": "unknown",
                   "other": [], "runtime": "unknown"},
        "llm_postprocess": {"local": "unknown", "cloud": "unknown"},
        "notes": f"NOT YET ANNOTATED. List description: {entry['desc']}",
        "evidence": [],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true",
                    help="refresh metadata and append stubs for new entries")
    args = ap.parse_args()

    doc = json.loads(DATA.read_text())
    # Entries with no slug are not on GitHub at all (whisperian is Play-Store
    # only), so they can never appear in — or disappear from — the stars list.
    known = {p["slug"]: p for p in doc["projects"] if p.get("slug")}
    live = {e["slug"]: e for e in scrape_list()}

    added = sorted(set(live) - set(known))
    # Only a project that CAME from the stars list can be dropped from it.
    # Search-found entries were never in the list, so their absence is normal —
    # reporting those as DROPPED buries the real signal under 20 false alarms.
    removed = sorted(s for s in set(known) - set(live)
                     if known[s].get("source") == "stars-list")
    unstarred = sorted(s for s in set(known) - set(live)
                       if known[s].get("source") != "stars-list"
                       and known[s]["category"] == "keyboard")
    unannotated = sorted(s for s, p in known.items() if p["notes"].startswith("NOT YET ANNOTATED"))

    for slug in added:
        print(f"NEW       {slug}  —  {live[slug]['desc'][:70]}")
    for slug in removed:
        print(f"DROPPED   {slug}  (still in projects.json; delete by hand if intended)")
    if unstarred:
        print(f"UNSTARRED {len(unstarred)} search-found keyboards are not in the stars list "
              f"(fine; star them to bring them into the queue)")
    for slug in unannotated:
        print(f"TODO      {slug}  needs the annotation pass")
    if not (added or removed or unannotated):
        print("in sync")

    if not args.write:
        return 0

    for slug, entry in live.items():
        target = known.get(slug)
        if target is None:
            target = stub(entry)
            doc["projects"].append(target)
        target["stars"] = entry["stars"]
        target["updated"] = entry["updated"]
        if target["license"] in ("unknown", "", None):
            meta = gh_meta(slug)
            if meta:
                target["license"] = meta["license"]

    order = {"keyboard": 0, "service": 1, "app": 2, "library": 3, "resource": 4}
    doc["projects"].sort(key=lambda p: (order.get(p["category"], 9), p["id"]))
    doc["snapshot_date"] = date.today().isoformat()
    DATA.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwrote {DATA.relative_to(ROOT)} ({len(doc['projects'])} projects)")
    print("now run: python3 scripts/render_readme.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
