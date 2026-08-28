#!/usr/bin/env bash
# Mede, ANTES da CI-1, o que este ambiente consegue alcançar.
# A escada de rotas se decide com este resultado — não no meio da coleta.
# Uso: scripts/testar-egress.sh [dominio-extra ...]
set -uo pipefail

alvos=(
  https://www.hapvida.com.br
  https://www.ans.gov.br
  https://www.ibge.gov.br
  https://cnes.datasus.gov.br
  https://tabelaplanos.com.br
  "$@"
)

echo "EGRESS — $(date +%F\ %T)"
echo "------------------------------------------------------------"
ok=0; falha=0
for u in "${alvos[@]}"; do
  code=$(curl -s -o /dev/null -w '%{http_code}' -m 12 -A 'Mozilla/5.0' "$u" 2>/dev/null)
  if [ "$code" = "000" ] || [ -z "$code" ]; then
    printf '  %-42s BLOQUEADO\n' "$u"; falha=$((falha+1))
  else
    printf '  %-42s %s\n' "$u" "$code"; ok=$((ok+1))
  fi
done
echo "------------------------------------------------------------"
echo "alcançáveis: $ok · bloqueados: $falha"
echo
if [ "$falha" -gt 0 ]; then
  cat <<'MSG'
⚠️  Há domínio bloqueado pela política de rede do ambiente.
    WebFetch e curl NÃO leem página de concorrente nesta sessão.
    Antes de rodar a CI-1, leia docs/CI1-SEM-EGRESS.md e registre no
    state file, na seção 5, qual rota foi usada para cada concorrente.
    Snippet de busca NÃO conta como "concorrente lido".
MSG
  exit 1
fi
cat <<'MSG'
✅ A REDE DO AMBIENTE ESTÁ LIBERADA — curl alcança todos os alvos.

⚠️  ISSO NÃO PROVA QUE O WebFetch FUNCIONA.
    O WebFetch carrega a política de rede do INÍCIO da sessão; o curl
    consulta o gateway a cada chamada. Numa sessão aberta ANTES da
    liberação, curl passa e WebFetch volta EGRESS_BLOCKED.

    Antes da CI-1, faça UMA chamada WebFetch a um alvo real.
      · funcionou  → CI-1 pela rota normal;
      · EGRESS_BLOCKED → use curl para ler a página (rota 1b de
        docs/CI1-SEM-EGRESS.md) ou abra uma sessão nova.
MSG
