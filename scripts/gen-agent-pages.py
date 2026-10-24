#!/usr/bin/env python3
"""gen-agent-pages.py — gera content/<slug>/index.md a partir de data/agents.yaml.

Owner (2026-10-23): "todo agente experimental ou flagship merece página. por ora
põe todos o que achar, com tier correspondente no frontmatter. popula com mock
text e diagrams."

Flat: content/<slug>/index.md → /<slug>/. Nenhum subfolder de tipo.
Não sobrescreve página existente com conteúdo real (só gera/atualiza mock).
"""
import os, sys, re, textwrap

ROOT = os.path.expanduser("~/Documents/nonlinear")
DATA = os.path.join(ROOT, "data/agents.yaml")
CONTENT = os.path.join(ROOT, "content")

SLUGS_EXISTING = {"librarian", "kin", "mood", "substrate", "astrolabe"}

LOREM = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo."""


def parse_yaml(path):
    """Parser mínimo para o nosso formato (listas de dicts com 2-3 níveis)."""
    groups, cur_group, cur_item = {}, None, None
    for raw in open(path):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" ") and line.endswith(":"):
            cur_group = line[:-1]
            groups[cur_group] = []
            cur_item = None
            continue
        s = line.strip()
        if s.startswith("- "):
            cur_item = {}
            groups[cur_group].append(cur_item)
            s = s[2:]
        if ":" in s and cur_item is not None:
            k, v = s.split(":", 1)
            v = v.strip().strip('"')
            if v in ("true", "false"):
                cur_item[k.strip()] = v == "true"
            elif v:
                cur_item[k.strip()] = v
    return groups


def page(slug, name, tier, role="", slogan=""):
    body = textwrap.dedent(f"""\
        ---
        title: "{name}"
        tier: {tier}
        slogan: "{slogan or 'Lorem ipsum dolor sit amet.'}"
        description: "{role or 'Lorem ipsum — page in progress.'}"
        date: 2026-10-23
        ---

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua.

        ## What it is

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris.

        ## How it works

        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
        dolore eu fugiat nulla pariatur.
        """)
    return body


def main():
    dry = "--dry" in sys.argv
    groups = parse_yaml(DATA)
    written, kept = [], []
    for tier_default, key in (("experimental", "derived"), (None, "declared")):
        for item in groups.get(key, []):
            slug = item.get("slug")
            if not slug:
                continue
            tier = item.get("tier") or tier_default
            path = os.path.join(CONTENT, slug, "index.md")
            if os.path.isdir(os.path.join(CONTENT, slug)) and os.path.exists(path):
                kept.append(f"{slug} (existente, preservado)")
                continue
            if dry:
                written.append(f"{slug} [{tier}]")
                continue
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                f.write(page(slug, item.get("name", slug.title()), tier,
                             item.get("role", "")))
            written.append(f"{slug} [{tier}]")
    print("ESCREVENDO:" if not dry else "DRY RUN — escreveria:")
    for w in written:
        print("  +", w)
    print("PRESERVADO:")
    for k in kept:
        print("  =", k)
    print(f"\ntotal: {len(written)} pages")


if __name__ == "__main__":
    main()
