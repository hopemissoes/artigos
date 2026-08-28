# Como liberar a rede do ambiente (rota 1 da CI-1)

O bloqueio não é um defeito: é o **nível de acesso de rede** do ambiente onde a
sessão roda. O padrão é **Trusted** — libera registries de pacote, GitHub e SDKs
de nuvem, e nada mais. Por isso `hapvida.com.br`, `ans.gov.br`, `ibge.gov.br` e os
concorrentes voltam 403.

São quatro níveis: **None** (nada), **Trusted** (padrão), **Full** (qualquer
domínio) e **Custom** (a sua lista, opcionalmente somada à padrão).

## Passo a passo

1. Abra <https://claude.ai/code>.
2. Na **linha acima da caixa de mensagem**, clique no **ícone de nuvem** com o nome
   do ambiente atual (normalmente `Default`). Não existe página de configurações
   nem URL direta — é só por aí.
3. Passe o mouse sobre o ambiente e clique no **ícone de engrenagem** à direita
   (ou em **Add cloud environment**, para criar um novo só para artigos).
4. No campo **Network access**, escolha **Custom**.
5. Em **Allowed domains**, cole a lista abaixo — **um domínio por linha**.
6. ⚠️ **Marque a caixa "Also include default list of common package managers".**
   Sem ela, `pip install` para de funcionar e o hook de sessão quebra.
7. Salve.

## A mudança não vale para esta sessão

Sessões em andamento mantêm a configuração com que começaram. **Abra uma sessão
nova** depois de salvar. Mudar a lista de domínios também refaz o cache do
ambiente, então a primeira sessão nova demora um pouco mais.

## Lista para colar

```text
*.hapvida.com.br
hapvida.com.br
*.gndi.com.br
*.clinipam.com.br
*.notredameintermedica.com.br
*.gov.br
*.ans.gov.br
*.ibge.gov.br
*.datasus.gov.br
tabelaplanos.com.br
*.tabelaplanos.com.br
*.frame.claudeusercontent.com
```

`*.gov.br` cobre IBGE, DATASUS/CNES, ANS, Ministério da Saúde e prefeituras de
uma vez. `*.frame.claudeusercontent.com` só é preciso se a sessão for ler
artifacts — pode tirar se não usar.

**Concorrentes mudam de cidade para cidade.** Acrescente os que aparecerem na SERP
e voltarem sempre. Os que apareceram na busca de teste de Recife:

```text
*.virtuacorretora.com.br
*.meuplanohap.com.br
*.tabelasaude.com
*.planodesaudepe.com
*.busqueplanodesaude.com.br
```

## Se preferir não manter lista

**Full** libera qualquer domínio e acaba com o problema de uma vez. Em troca, a
sessão pode alcançar qualquer lugar da internet — decisão sua. Para produção de
artigo, **Custom com a lista acima é o suficiente** e mantém a contenção.

## O que NÃO precisa entrar na lista

- **Os conectores MCP** (BD, DataForSeo, n8n, WordPress, GSC/GA4, Drive): o
  tráfego deles passa pelos servidores da Anthropic, não pela rede da sessão.
  Funcionam mesmo em **None**.
- **GitHub**: usa um proxy separado, independente deste nível.

## Depois de liberar

```bash
scripts/testar-egress.sh
```

Deve imprimir `✅ egress livre`. Aí a CI-1 volta a rodar pela rota normal
(`WebFetch`) e as rotas 2 a 5 de `docs/CI1-SEM-EGRESS.md` viram contingência.

---

Fonte: [Configure cloud environments](https://code.claude.com/docs/en/cloud-environments)
— consultada em 2026-08-28.
