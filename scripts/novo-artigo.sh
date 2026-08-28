#!/usr/bin/env bash
# Cria a pasta de um artigo novo a partir do template.
# Uso: scripts/novo-artigo.sh <slug> [city|hospital|tr|pillar|cobertura]
set -euo pipefail

root="$(git rev-parse --show-toplevel)"
slug="${1:-}"
tipo="${2:-city}"

if [ -z "$slug" ]; then
  echo "uso: $0 <slug> [city|hospital|tr|pillar|cobertura]" >&2
  exit 2
fi

dest="$root/artigos/$slug"
if [ -e "$dest" ]; then
  echo "já existe: $dest" >&2
  echo "→ leia $dest/00-ESTADO.md e continue de onde parou." >&2
  exit 1
fi

cp -r "$root/artigos/_TEMPLATE" "$dest"
mv "$dest/PESQUISA_SLUG_COMPLETO.md" "$dest/PESQUISA_${slug}_COMPLETO.md"

hoje="$(date +%Y-%m-%d)"
for f in "$dest/00-ESTADO.md" "$dest/PESQUISA_${slug}_COMPLETO.md"; do
  sed -i "s/{{SLUG}}/$slug/g; s/{{TIPO}}/$tipo/g; s/{{DATA}}/$hoje/g" "$f"
done

echo "criado: artigos/$slug ($tipo)"
echo "próximo passo: FASE 0 — preencher PESQUISA_${slug}_COMPLETO.md e rodar"
echo "  scripts/cp.sh hapvida-article-builder-v7 checkpoint_fase0.py artigos/$slug/PESQUISA_${slug}_COMPLETO.md $tipo"
