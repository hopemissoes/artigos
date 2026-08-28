#!/usr/bin/env bash
# Imprime o caminho absoluto de uma skill instalada, seja qual for o ambiente.
# Uso: scripts/skill-path.sh hapvida-article-builder-v7
set -euo pipefail

skill="${1:-}"
if [ -z "$skill" ]; then
  echo "uso: $0 <nome-da-skill>" >&2
  exit 2
fi

roots=(
  "${CLAUDE_SKILLS_DIR:-}"
  "$HOME/.claude/skills"
  "/root/.claude/skills"
  "/home/claude/.claude/skills"
  "/mnt/skills"
  "$HOME/.claude/plugins"
  "$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.claude/skills"
)

for root in "${roots[@]}"; do
  [ -n "$root" ] && [ -d "$root" ] || continue
  hit=$(find "$root" -maxdepth 4 -type d -name "$skill" 2>/dev/null | head -1)
  if [ -n "$hit" ] && [ -f "$hit/SKILL.md" ]; then
    echo "$hit"
    exit 0
  fi
done

echo "skill '$skill' não encontrada. Skills disponíveis:" >&2
for root in "${roots[@]}"; do
  [ -n "$root" ] && [ -d "$root" ] || continue
  find "$root" -maxdepth 4 -name SKILL.md 2>/dev/null \
    | sed 's|/SKILL.md$||' | xargs -r -n1 basename
done | sort -u >&2
exit 1
