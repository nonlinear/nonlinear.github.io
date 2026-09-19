#!/usr/bin/env bash
# verify-publish.sh — check Nonlinear site deployed on GitHub Pages
#
# Usage:
#   ./scripts/verify-publish.sh [--timeout <seconds>]
#
# Exit:
#   0 = PASS (built + serving)
#   1 = FAIL (errored)
#   2 = timeout (still building)

set -euo pipefail

REPO="nonlinear/nonlinear.github.io"
URL="https://nonlinear.nyc/"
TIMEOUT="${1:-300}"
POLL_INTERVAL=15

sha="$(cd "$(dirname "$0")/.." && git rev-parse HEAD 2>/dev/null || echo "unknown")"

echo "── verify publish ──────────────────────────────"
echo "  repo  : $REPO"
echo "  sha   : $sha"
echo "  url   : $URL"
echo "  wait  : ${TIMEOUT}s max"
echo ""

start=$(date +%s)

# Phase 1 — Poll GitHub Pages API until status is "built" or "errored"
while true; do
  elapsed=$(($(date +%s) - start))
  [[ "$elapsed" -gt "$TIMEOUT" ]] && { echo "✗ timeout (${TIMEOUT}s) — build still queued/building"; exit 2; }

  status=$(gh api "repos/$REPO/pages" --jq '.status' 2>/dev/null || echo "null")

  case "$status" in
    "built")    echo "✓ Pages build: built"; break ;;
    "errored")  echo "✗ Pages build: errored"; exit 1 ;;
    "null")     echo "  status: null (no build recorded)"; sleep "$POLL_INTERVAL" ;;
    "queued"|*) echo "  status: ${status:-unknown} — waiting ${POLL_INTERVAL}s"; sleep "$POLL_INTERVAL" ;;
  esac
done

# Phase 2 — HTTP verify site is serving
echo "  verifying HTTP…"
http_code=$(curl -sI -o /dev/null -w "%{http_code}" "$URL" 2>/dev/null || echo "000")

if [[ "$http_code" =~ ^[23] ]]; then
  echo "✓ HTTP $http_code from $URL"
  echo "─────────────────────────────── ✓ PUBLISHED"
  echo "$URL"
  exit 0
else
  echo "✗ HTTP $http_code from $URL"
  exit 1
fi