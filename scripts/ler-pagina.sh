#!/usr/bin/env bash
# Lê uma página inteira e salva em artigos/<slug>/fontes/ — rota 1b da CI-1,
# para quando o WebFetch está defasado. Avisa se o que voltou for desafio de bot.
# Uso: scripts/ler-pagina.sh <slug> <url>
set -uo pipefail

root="$(git rev-parse --show-toplevel)"
slug="${1:-}"; url="${2:-}"
if [ -z "$slug" ] || [ -z "$url" ]; then
  echo "uso: $0 <slug> <url>" >&2; exit 2
fi

dest="$root/artigos/$slug/fontes"
mkdir -p "$dest"
host=$(echo "$url" | sed 's|https\?://||; s|/.*||; s|^www\.||')
out="$dest/concorrente-$host-$(date +%Y%m%d).html"

curl -sL -m 30 \
  -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36' \
  "$url" -o "$out"

size=$(wc -c < "$out" 2>/dev/null || echo 0)
title=$(grep -o -i -m1 '<title>[^<]*</title>' "$out" 2>/dev/null | sed 's/<[^>]*>//g')
h2=$(grep -c -o -i '<h2' "$out" 2>/dev/null || echo 0)

echo "arquivo : ${out#$root/}"
echo "tamanho : $size bytes"
echo "title   : ${title:-—}"
echo "h2      : $h2"

if [ "$size" -lt 20000 ] || echo "$title" | grep -qi "just a moment\|attention required\|access denied\|cloudflare"; then
  cat <<'MSG'

⚠️  ISTO NÃO É A PÁGINA — parece desafio de bot (Cloudflare e afins).
    Medido: o IBGE responde assim ao curl. NÃO registre como concorrente lido.
    Tente, em ordem: WebFetch (se a sessão for nova), o extrator n8n
    (rota 2 de docs/CI1-SEM-EGRESS.md), ou peça a página ao usuário.
MSG
  exit 1
fi

echo
echo "✅ página inteira. Conta como concorrente LIDO — registre no state file:"
echo "   - concorrente: $host — url: $url — lido_em: $(date +%F) — rota: 1b"
