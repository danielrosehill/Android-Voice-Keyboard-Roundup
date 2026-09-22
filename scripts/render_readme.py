#!/usr/bin/env python3
"""Regenerate the tables in README.md from data/projects.json.

    python3 scripts/render_readme.py

projects.json is the source of truth. Everything between the BEGIN/END markers in
README.md is overwritten; prose outside them is left alone. Never hand-edit
inside the markers.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "projects.json"
README = ROOT / "README.md"

GLYPH = {"yes": "✅", "no": "—", "partial": "◐", "unknown": "?", "n/a": "·"}


def g(value):
    return GLYPH.get(value, "?")


def link(p):
    return f"[{p['name']}]({p['url']})"


def capability_table(keyboards):
    rows = [
        "| Project | Voice IME | Full keyboard | Floating button |",
        "| --- | :---: | :---: | :---: |",
    ]
    for p in keyboards:
        f = p["form"]
        rows.append(
            f"| {link(p)} | {g(f['voice_ime'])} | {g(f['full_keyboard'])} "
            f"| {g(f['floating_button'])} |"
        )
    return "\n".join(rows)


def recognition_table(keyboards):
    rows = [
        "| Project | Local | Cloud | Auto fallback | Whisper | NVIDIA | Moonshine | Other ASR |",
        "| --- | :---: | :---: | :---: | :---: | :---: | :---: | --- |",
    ]
    for p in keyboards:
        e, m = p["engine"], p["models"]
        other = ", ".join(m["other"]) if m["other"] else "—"
        rows.append(
            f"| {link(p)} | {g(e['local'])} | {g(e['cloud'])} | {g(e['fallback'])} "
            f"| {g(m['whisper'])} | {g(m['nvidia'])} | {g(m['moonshine'])} | {other} |"
        )
    return "\n".join(rows)


def postprocess_table(keyboards):
    rows = [
        "| Project | LLM cleanup (local) | LLM cleanup (cloud) | Runtime | Licence | ★ | Updated |",
        "| --- | :---: | :---: | --- | --- | ---: | --- |",
    ]
    for p in keyboards:
        l = p["llm_postprocess"]
        rows.append(
            f"| {link(p)} | {g(l['local'])} | {g(l['cloud'])} | {p['models']['runtime']} "
            f"| {p['license']} | {p['stars']} | {p['updated']} |"
        )
    return "\n".join(rows)


def notes_section(projects):
    out = []
    for p in projects:
        out.append(f"### {p['name']}\n")
        out.append(f"`{p['id']}` · <{p['url']}> · {p['license']} · {p['stars']}★ "
                   f"· last commit {p['updated']}\n")
        out.append(p["notes"] + "\n")
    return "\n".join(out)


def other_table(projects):
    rows = ["| Project | Kind | What it is |", "| --- | --- | --- |"]
    for p in projects:
        first = p["notes"].split(" — ")[0].split(". ")[0]
        rows.append(f"| {link(p)} | {p['category']} | {first} |")
    return "\n".join(rows)


def replace_block(text, name, body):
    # \n?…\n? so an empty block (the two markers on consecutive lines) still
    # matches — that is the state a freshly written README is in.
    pattern = re.compile(
        rf"(<!-- BEGIN {name} -->)\n?.*?\n?(<!-- END {name} -->)", re.S
    )
    if not pattern.search(text):
        sys.exit(f"marker pair for {name!r} not found in README.md")
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(2)}", text)


def main():
    doc = json.loads(DATA.read_text())
    projects = doc["projects"]
    keyboards = sorted((p for p in projects if p["category"] == "keyboard"),
                       key=lambda p: p["id"])
    others = sorted((p for p in projects if p["category"] != "keyboard"),
                    key=lambda p: p["id"])

    text = README.read_text()
    text = replace_block(text, "capability", capability_table(keyboards))
    text = replace_block(text, "recognition", recognition_table(keyboards))
    text = replace_block(text, "postprocess", postprocess_table(keyboards))
    text = replace_block(text, "other", other_table(others))
    text = replace_block(text, "notes", notes_section(keyboards + others))
    text = replace_block(text, "snapshot",
                         f"Data snapshot: **{doc['snapshot_date']}** · "
                         f"{len(keyboards)} keyboards, {len(others)} other entries.")
    README.write_text(text)
    print(f"rendered {len(keyboards)} keyboards + {len(others)} other into README.md")


if __name__ == "__main__":
    main()
