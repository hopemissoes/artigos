# CI-1 quando a rede bloqueia o concorrente

**Medido em 2026-08-28, neste ambiente (Claude Code na web):**

| Rota | Status | O que devolve |
|---|---|---|
| `curl` / `WebFetch` para site externo | ❌ **bloqueado** (403 no CONNECT, política de rede do ambiente) | nada |
| `WebSearch` | ✅ funciona | título, URL e trecho — **não** a página |
| MCP `DataForSeo` | ✅ funciona | SERP real, volume, dificuldade, PAA, keywords do concorrente |
| MCP `BD - *` (Supabase) | ✅ funciona | o dado proprietário de vocês |
| MCP `SEO - Hapvida` (n8n) | ✅ funciona | **roda `httpRequest` fora deste contêiner** |
| MCP `site_tabela_planos` (WordPress) | ✅ funciona | o próprio site |
| `pip install` | ✅ funciona | pypi está liberado |

O `checkpoint_ci1.py` pergunta uma coisa só: **o concorrente foi LIDO?** Trecho de
busca não é leitura. Em 27/08 a linha inteira rodou em cima de uma CI-1 que nunca
abriu um concorrente, e duas afirmações saíram falsas. Ver `docs/DECISOES.md`.

---

## A escada de rotas — tente em ordem, registre cada tentativa

**Rode antes de começar:** `scripts/testar-egress.sh`

### Rota 1 — liberar o domínio no ambiente (a solução de verdade)

O ambiente está no nível **Trusted**, que não libera site externo. Passando para
**Full**, o `WebFetch` volta a funcionar e a CI-1 roda como foi desenhada — sem
lista de domínios para manter, que é o ponto: concorrente muda a cada cidade.

**Passo a passo: `docs/LIBERAR-REDE.md`.**

**Esta é a rota preferida. As outras são contorno.**

### Rota 2 — n8n faz a leitura por você

A própria skill já traz a ferramenta, e ela nunca foi usada:
`assets/CI1-extrator-concorrentes.json` é um workflow n8n com os nós
`List URLs → Fetch Page → Extract Structure`. O n8n roda **no servidor**, fora
deste contêiner — o bloqueio de egress não o alcança.

```
mcp__SEO_-_Hapvida__create_workflow_from_code   ← a partir do JSON do asset
mcp__SEO_-_Hapvida__execute_workflow            ← com as URLs dos concorrentes
```

O que volta é a estrutura on-page real (H1/H2/H3, contagem, blocos) — o insumo
que a CI-1 pede. **Isto conta como concorrente lido.**

### Rota 3 — DataForSeo

`ranked_keywords` do domínio concorrente + `serp_local` + `related_keywords`
dão cobertura por keyword e a matriz de posições. Dá para medir **onde** o
concorrente é forte, não **como** ele escreve.
**Conta como leitura parcial** — registre a limitação na seção 5 do state file.

### Rota 4 — o usuário cola a página

Peça o HTML ou o texto e salve em `artigos/<slug>/fontes/concorrente-<dominio>.html`.
Trabalhoso, mas é leitura de verdade. Também vale o Google Drive (MCP disponível).

### Rota 5 — não há rota

**Pare e avise.** Não escreva "CI-1 degradada" em letra miúda e siga. A resposta
certa é dizer que a CI-1 não pôde ser feita e perguntar se o artigo espera a
liberação do domínio ou sai declaradamente sem desmontagem de concorrente.

---

## O que registrar no state file (seção 5)

```
- concorrente: [dominio] — url: https://... — lido_em: AAAA-MM-DD
  - rota: 1 | 2 | 3 | 4        # qual rota da escada funcionou
  - tentativas: rota 1 falhou (403 CONNECT); rota 2 OK via n8n
  - matriz de cobertura: ...
```

Sem o campo `rota:`, quem lê depois não sabe se a CI-1 leu a página ou o snippet.
