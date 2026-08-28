#!/bin/bash
# SessionStart — prepara a sessão para produção de artigo.
# Idempotente e não-interativo.
set -uo pipefail

cd "${CLAUDE_PROJECT_DIR:-$(dirname "${BASH_SOURCE[0]}")/../..}" || exit 0

# 1. dependências python (só o que as skills importam de fato)
if ! python3 -c "import PIL" >/dev/null 2>&1; then
  pip install -q -r requirements.txt >/dev/null 2>&1 || true
fi

# 2. contexto que a sessão precisa ver antes de agir
echo "════════════════════════════════════════════════════════════════"
echo " REPOSITÓRIO DE ARTIGOS — leia CLAUDE.md antes de qualquer coisa"
echo "════════════════════════════════════════════════════════════════"
echo
echo "REGRA 1: escolher a skill (docs/ROTEAMENTO.md) ANTES de produzir."
echo "REGRA 2: nenhum HTML antes da FASE 0 aprovada (checkpoint + humano)."
echo "PADRÃO : artigo Hapvida = hapvida-article-builder-v7, sempre."
echo

# 3. egress: dizer AGORA se a leitura de concorrente está bloqueada
if command -v curl >/dev/null 2>&1; then
  if curl -s -o /dev/null -m 8 https://www.hapvida.com.br 2>/dev/null; then
    echo "REDE   : egress direto OK — CI-1 pode ler concorrente via WebFetch."
  else
    echo "REDE   : ⚠️  egress BLOQUEADO para sites externos."
    echo "         WebFetch e curl não leem concorrente. WebSearch e DataForSeo"
    echo "         funcionam. Antes da CI-1, leia docs/CI1-SEM-EGRESS.md."
  fi
fi
echo

# 4. o que está em produção
shopt -s nullglob
abertos=()
for f in artigos/*/00-ESTADO.md; do
  slug=$(basename "$(dirname "$f")")
  [ "$slug" = "_TEMPLATE" ] && continue
  fase=$(grep -m1 '^\- \*\*Fase:\*\*' "$f" | sed 's/.*\*\*Fase:\*\* //')
  abertos+=("  · $slug — ${fase:-fase não registrada}")
done
if [ ${#abertos[@]} -gt 0 ]; then
  echo "EM PRODUÇÃO:"
  printf '%s\n' "${abertos[@]}"
else
  echo "EM PRODUÇÃO: nenhum artigo aberto. Use /novo-artigo <slug> <tipo>."
fi
echo
echo "════════════════════════════════════════════════════════════════"
exit 0
