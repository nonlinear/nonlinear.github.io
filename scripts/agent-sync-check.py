#!/usr/bin/env python3
"""agent-sync-check.py — APONTA divergência. Não corrige nada.

Owner (2026-10-23 14:26):
    "tieras follow identity. names follow identity. precisamos de um mecanismo
     que roda o source of truth e não mexe right away. mas sugere conflitos.
     skill plus heartbeat? o skill não resolve ele aponta."

A fonte de verdade é o agente:
    ~/.openclaw/agents/<agent>/workspace/IDENTITY.md   → campo `tier:` + `title:`

O site é espelho:
    ~/Documents/nonlinear/data/agents.yaml             → registro
    ~/Documents/nonlinear/content/<slug>/index.md      → página (frontmatter)

Este script NÃO escreve em nada. Só emite conflitos e sai com código != 0
quando há divergência — para o heartbeat decidir o que fazer.

Códigos de saída:
  0 = tudo coerente
  1 = divergências (lista abaixo)
"""
import os
import re
import sys

AGENTS = os.path.expanduser("~/.openclaw/agents")
SITE = os.path.expanduser("~/Documents/nonlinear")

# Tiers — exatamente DOIS têm página pública (owner, 2026-10-23 14:33):
#   "não são cinco, são dois tiers. dois."
#
# `collab` continua sendo um tier na taxonomia (P02E034), mas NÃO é página
# pública: privacidade/contrato. Tier ≠ página — eu tinha misturado.
# `article` não é tier (é gênero editorial). `writing` não existe.
VALID_TIERS = {"flagship", "experimental", "collab"}
PUBLIC_TIERS = {"flagship", "experimental"}
NON_PUBLIC_TIERS = {"collab"}

# slugs de página que NÃO representam agente (conteúdo do site)
NON_AGENT_SLUGS = {
    "styleguide", "tiers", "probe-default", "index2",
    "sed-do-eiusmod", "lorem-ipsum-dolor", "consectetur-adipiscing",
    "ut-enim-ad-minim", "source-highlights", "delay-tolerant-ai",
}


def read_identity(agent):
    """Retorna (tier, name) do IDENTITY.md, ou (None, None)."""
    for rel in ("workspace/IDENTITY.md", "IDENTITY.md"):
        p = os.path.join(AGENTS, agent, rel)
        if not os.path.isfile(p):
            continue
        txt = open(p, encoding="utf-8", errors="replace").read()
        m = re.search(r"^\s*tier:\s*([a-zA-Z-]+)", txt, re.M)
        tier = m.group(1).lower() if m else None
        n = re.search(r"^title:\s*(.+)$", txt, re.M)
        name = n.group(1).strip().strip('"').strip("'") if n else None
        return tier, name
    return None, None


def read_frontmatter(path):
    """Parser mínimo de YAML frontmatter — só o que importa."""
    if not os.path.isfile(path):
        return None
    txt = open(path, encoding="utf-8", errors="replace").read()
    if not txt.startswith("---"):
        return {}
    end = txt.find("\n---", 3)
    if end == -1:
        return {}
    out = {}
    for line in txt[3:end].splitlines():
        m = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if m:
            k, v = m.group(1), m.group(2).strip().strip('"').strip("'")
            out[k] = v
    return out


def read_agents_yaml_registry():
    """Lê data/agents.yaml → {slug: tier} (declarado ou derivado)."""
    path = os.path.join(SITE, "data/agents.yaml")
    reg, current = {}, None
    if not os.path.isfile(path):
        return reg
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        if re.match(r"^(declared|derived|defaults):", line):
            current = line.split(":")[0]
            continue
        m = re.match(r"^\s*-\s*slug:\s*(\S+)", line)
        if m:
            reg[m.group(1)] = {"group": current, "tier": None}
            continue
        m = re.match(r"^\s+tier:\s*(\S+)", line)
        if m and reg:
            last = list(reg)[-1]
            reg[last]["tier"] = m.group(1)
    return reg


def main():
    conflicts = []
    notes = []

    registry = read_agents_yaml_registry()

    # --- 1. agentes vs IDENTITY (fonte) ---
    for agent in sorted(os.listdir(AGENTS)):
        if not os.path.isdir(os.path.join(AGENTS, agent)):
            continue
        if agent in ("_archived-2026-07-26", "main", "openclaw"):
            continue
        tier, name = read_identity(agent)
        if tier is None:
            continue  # agente sem tier escrito: não é conflito, é indefinição
        if tier not in VALID_TIERS:
            conflicts.append(
                f"TIER INVÁLIDO  {agent}: IDENTITY diz `{tier}` "
                f"(válidos: {', '.join(sorted(VALID_TIERS))})"
            )
        reg = registry.get(agent)
        if reg and reg["tier"] and reg["tier"] != tier:
            conflicts.append(
                f"TIER DIVERGE   {agent}: IDENTITY=`{tier}` vs agents.yaml=`{reg['tier']}`"
            )
        # collab não publica página — verificação abaixo (seção 3)

    # --- 2. páginas do site vs IDENTITY (fonte) ---
    content = os.path.join(SITE, "content")
    for slug in sorted(os.listdir(content)):
        d = os.path.join(content, slug)
        if not os.path.isdir(d) or slug in NON_AGENT_SLUGS:
            continue
        fm = read_frontmatter(os.path.join(d, "index.md"))
        if fm is None:
            conflicts.append(f"PÁGINA SEM MD  {slug}/ existe, sem index.md")
            continue
        site_tier = (fm.get("type") or fm.get("tier") or "").lower() or None
        site_name = fm.get("title")

        if site_tier and site_tier not in VALID_TIERS:
            conflicts.append(
                f"TIER INVÁLIDO  content/{slug}: `type: {site_tier}` "
                f"(válidos: {', '.join(sorted(VALID_TIERS))}) — artigo não é tier"
            )
        if site_tier in NON_PUBLIC_TIERS:
            conflicts.append(
                f"PUBLICA COLLAB content/{slug}: tier `{site_tier}` não tem página pública "
                f"(privacidade/contrato)"
            )

        ident_tier, ident_name = read_identity(slug)
        if ident_tier is None and ident_name is None:
            # página sem agente correspondente: pode ser conteúdo legítimo
            notes.append(f"SEM AGENTE     content/{slug} (nenhum IDENTITY.md)")
            continue

        if ident_tier and site_tier and ident_tier != site_tier:
            conflicts.append(
                f"TIER DIVERGE   {slug}: IDENTITY=`{ident_tier}` vs site=`{site_tier}`"
            )
        if ident_tier is None and site_tier:
            conflicts.append(
                f"TIER INVENTADO {slug}: site diz `{site_tier}`, IDENTITY não declara tier"
            )
        # nome: IDENTITY é a fonte (ignora emoji de acessório no título do agente)
        if ident_name and site_name:
            a = re.sub(r"[^\w\s-]", "", ident_name).strip().lower()
            b = re.sub(r"[^\w\s-]", "", site_name).strip().lower()
            if a != b:
                conflicts.append(
                    f"NOME DIVERGE   {slug}: IDENTITY=`{ident_name}` vs site=`{site_name}`"
                )

    # --- 3. agentes com tier PÚBLICO e sem página ---
    # collab NÃO conta: é tier, mas não é página (owner, 14:33).
    for agent in sorted(os.listdir(AGENTS)):
        if not os.path.isdir(os.path.join(AGENTS, agent)):
            continue
        tier, _ = read_identity(agent)
        if tier in PUBLIC_TIERS and not os.path.isdir(os.path.join(content, agent)):
            conflicts.append(
                f"SEM PÁGINA     {agent}: IDENTITY declara `{tier}`, site não tem content/{agent}/"
            )

    # --- saída ---
    print(f"agent-sync-check — fonte: IDENTITY.md · espelho: data/agents.yaml + content/\n")
    if notes:
        print("notas (não bloqueiam):")
        for n in notes:
            print("  ·", n)
        print()
    if conflicts:
        print(f"{len(conflicts)} conflito(s):\n")
        for c in conflicts:
            print("  ✗", c)
        print("\nNada foi alterado. Resolver é decisão do owner.")
        return 1
    print("✓ coerente. Nenhum conflito.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
