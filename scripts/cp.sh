#!/usr/bin/env bash
# Roda um checkpoint .py de uma skill, sem depender de caminho absoluto.
# Uso: scripts/cp.sh <skill> <checkpoint.py> [args...]
# Ex.:  scripts/cp.sh hapvida-article-builder-v7 checkpoint_fase0.py \
#           artigos/recife/PESQUISA_recife_COMPLETO.md city
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
skill="${1:-}"; script="${2:-}"
if [ -z "$skill" ] || [ -z "$script" ]; then
  echo "uso: $0 <skill> <checkpoint.py> [args...]" >&2
  exit 2
fi
shift 2

dir="$("$here/skill-path.sh" "$skill")"
target="$dir/$script"

if [ ! -f "$target" ]; then
  echo "checkpoint '$script' não existe em $dir" >&2
  echo "disponíveis:" >&2
  ls "$dir"/checkpoint_*.py 2>/dev/null | xargs -r -n1 basename >&2
  exit 1
fi

PYTHONUTF8=1 exec python3 "$target" "$@"
