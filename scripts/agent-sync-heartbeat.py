#!/usr/bin/env python3
"""agent-sync-heartbeat.py — o que o heartbeat faz com o check.

Owner: "skill plus heartbeat? o skill não resolve ele aponta."

Divisão de trabalho:
  agent-sync-check.py       → APONTA (puro, sem estado, sem efeito)
  agent-sync-heartbeat.py   → LEMBRA e ESCALA (estado, mas ainda sem corrigir)

Regra de erro que este script segue (nurtured-cognition):
  skill     = executa e corrige         ← para FORMATO, não para JULGAMENTO
  check     = aponta                    ← puro, verificável
  heartbeat = lembra o que foi apontado ← estado entre rodadas
  owner     = decide                    ← só o que é julgamento chega aqui

Por que o skill não resolve: tier é decidido top-down pelo owner (P02E034).
Nenhuma skill tem autoridade para decidir tier. Ele só pode APONTAR.

Uso:
  python3 scripts/agent-sync-heartbeat.py            # relatório
  python3 scripts/agent-sync-heartbeat.py --json     # para o heartbeat
"""
import json
import os
import subprocess
import sys
import time

SITE = os.path.expanduser("~/Documents/nonlinear")
STATE = os.path.join(SITE, ".agent-sync-state.json")
CHECK = os.path.join(SITE, "scripts/agent-sync-check.py")


def run_check():
    r = subprocess.run([sys.executable, CHECK], capture_output=True, text=True)
    lines = [l.strip() for l in r.stdout.splitlines() if l.strip().startswith("✗")]
    return r.returncode, lines


def load_state():
    if os.path.isfile(STATE):
        try:
            return json.load(open(STATE))
        except Exception:
            pass
    return {"seen": {}, "first_seen": {}, "runs": 0}


def save_state(s):
    with open(STATE, "w") as f:
        json.dump(s, f, indent=2)


def main():
    as_json = "--json" in sys.argv
    code, conflicts = run_check()
    state = load_state()
    state["runs"] += 1
    now = time.strftime("%Y-%m-%dT%H:%M:%S")

    current = set(conflicts)
    seen = set(state["seen"].keys())

    new = sorted(current - seen)
    resolved = sorted(seen - current)
    persisting = sorted(current & seen)

    for c in new:
        state["first_seen"][c] = now
    state["seen"] = {c: state["first_seen"].get(c, now) for c in current}
    save_state(state)

    if as_json:
        print(json.dumps({
            "runs": state["runs"],
            "new": new,
            "persisting": persisting,
            "resolved": resolved,
            "total": len(current),
        }, indent=2))
        return 0 if not current else 1

    print(f"agent-sync-heartbeat — run #{state['runs']}\n")
    if new:
        print(f"NOVOS ({len(new)}) — precisam de decisão do owner:")
        for c in new:
            print("  + ", c)
    if persisting:
        print(f"\nPERSISTEM ({len(persisting)}) — já reportados, ainda sem decisão:")
        for c in persisting:
            days = ""
            print("  = ", c)
    if resolved:
        print(f"\nRESOLVIDOS ({len(resolved)}):")
        for c in resolved:
            print("  ✓ ", c)
    if not current:
        print("✓ nada pendente.")
    return 0 if not current else 1


if __name__ == "__main__":
    sys.exit(main())
