# DECISÕES E LIÇÕES

Registro corrido. Uma entrada por decisão que a próxima sessão não deve reabrir,
e por erro que não deve se repetir. **Acrescente ao fim; não reescreva o passado.**

---

## 2026-08-28 — Este repositório passa a ser a mesa de trabalho

**Problema:** artigos vinham sendo produzidos dentro de um repositório sem relação
com a produção de conteúdo, e a skill certa nem sempre era acionada. Resultado:
trabalho perdido entre sessões, pesquisa refeita e decisões contraditórias.

**Decisão:** todo artefato de artigo vive em `artigos/<slug>/` deste repositório,
com `00-ESTADO.md` como ponto de salvamento, e `docs/ROTEAMENTO.md` como a primeira
leitura de qualquer pedido.

---

## 2026-08-28 — As skills NÃO são copiadas para cá

**Por quê:** elas são skills pessoais da conta e já vêm sincronizadas em toda
sessão (web, desktop, terminal). Uma cópia versionada aqui divergiria da original
sem ninguém perceber, e a sessão carregaria a versão errada.

**Consequência:** os caminhos absolutos de Windows que aparecem nos `SKILL.md`
(`C:\Users\netop\.claude\skills\...`) não valem aqui. Use `scripts/cp.sh` e
`scripts/skill-path.sh`, que resolvem o caminho em qualquer ambiente. Ver
`docs/AMBIENTE.md`.

---

## 2026-08-28 — Versão padrão da builder Hapvida: v7

As skills v5+ exigem "pedido explícito da versão". A linha no `CLAUDE.md` §3 é
essa autorização, feita uma vez, para não repetir a cada tarefa. **Para trocar,
edite aquela linha** — não decida por conta na hora.

---

## 2026-08-27 — Egress bloqueou os concorrentes e a linha seguiu assim mesmo

Registrado no `SKILL.md` da v7 (caso `plano-de-saude-barato`). A CI-1 não
conseguiu ler os concorrentes, declarou a limitação em letra miúda no state file,
**e os 25 agentes seguiram em frente**. O artigo inteiro foi julgado em cima de
uma pesquisa que nunca leu um concorrente; duas afirmações saíram falsas.

**Lição:** limitação de coleta não vira nota de rodapé. Desça a escada de rotas,
registre cada tentativa no state file e, se nada funcionar, **pare e avise**.
`checkpoint_ci1.py` existe por causa disso e roda antes de tudo.

---

<!-- modelo para a próxima entrada:

## AAAA-MM-DD — título curto da decisão

**Contexto:** o que estava em jogo.
**Decisão:** o que ficou valendo.
**Consequência:** o que muda na prática para quem vier depois.

-->
## 2026-08-28 — v7 é o padrão implícito, sem confirmação

O usuário determinou: artigo Hapvida é feito na **v7**, sempre. O parágrafo do
`CLAUDE.md` §3 é a autorização explícita e permanente que a skill exige. Não
perguntar a cada tarefa. Outra versão só quando o usuário nomear na hora.

---

## 2026-08-28 — Medida a diferença real entre este ambiente e o Desktop

Testado, não suposto:

- ❌ **`WebFetch` e `curl` para site externo são bloqueados** pela política de rede
  do environment (gateway responde 403 no CONNECT). Vale para `hapvida.com.br`,
  `ans.gov.br`, `ibge.gov.br`, `cnes.datasus.gov.br` e para os concorrentes.
  **É a mesma causa do incidente de 27/08.**
- ✅ `WebSearch`, todos os MCP (DataForSeo, BD, n8n, WordPress, GSC/GA4, Drive) e
  `pip install` funcionam — rodam no servidor, fora do contêiner.
- ✅ Subagentes com **modelo por chamada** (`opus`/`sonnet`/`haiku`/`fable`).

**Conclusão:** neste ambiente a linha multimodelo da v7.2 roda como foi desenhada —
coisa que o Desktop não permite, porque lá não há como dar modelo diferente ao
conferente. O único ponto em que se perde é a **leitura direta de concorrente**.

**Decisão:** `scripts/testar-egress.sh` roda antes de toda CI-1, e a escada de
rotas de `docs/CI1-SEM-EGRESS.md` passa a ser obrigatória. A rota 2 usa o
`assets/CI1-extrator-concorrentes.json` — um workflow n8n que já existia na skill
e nunca tinha sido usado; ele faz o `httpRequest` fora do contêiner, então o
bloqueio não o alcança.

**Pendente com o usuário:** liberar os domínios na política de rede do environment
resolve na origem e devolve o `WebFetch`. É a rota 1, e é a preferida.

---
## 2026-08-28 — Acesso de rede do ambiente: `Full`

**Contexto:** o ambiente estava em `Trusted`, que não alcança site externo — a
causa do incidente de 27/08, em que a CI-1 nunca leu um concorrente.

**Decisão do usuário:** nível **`Full`**, não `Custom` com lista. Motivo: os
concorrentes variam demais entre cidades e artigos; lista de domínios viraria
manutenção permanente e, pior, falharia em silêncio a cada concorrente novo na
SERP — reproduzindo o mesmo incidente por outro caminho.

**Consequência:** `WebFetch` volta a funcionar e a CI-1 roda pela rota 1. As rotas
2 a 5 de `docs/CI1-SEM-EGRESS.md` continuam documentadas como contingência — um
domínio pode cair sozinho a qualquer momento, e o `scripts/testar-egress.sh`
continua sendo o primeiro passo de toda CI-1.

**O que não muda:** o proxy de segurança continua à frente do tráfego em qualquer
nível. E página de concorrente segue sendo conteúdo não confiável: dado extraído
dela é `[VERIFICAR]` até bater com fonte primária.

---
## 2026-08-28 (fim do dia) — Rede liberada em `Full`, e uma armadilha medida

O ambiente passou para `Full` e a rede está liberada. Confirmado em sessão nova e
nesta. **Mas o `curl` e o `WebFetch` não andam juntos:**

| | Nesta sessão (aberta ANTES da mudança) |
|---|---|
| `curl` | ✅ alcança os cinco alvos — consulta o gateway a cada chamada |
| `WebFetch` | ❌ `EGRESS_BLOCKED` em `hapvida.com.br` e `ibge.gov.br` — carrega a política do início da sessão |

**Por que isto importa:** o `scripts/testar-egress.sh` concluía "✅ egress livre —
CI-1 pode ler concorrente direto por WebFetch". Era falso numa sessão aberta antes
da liberação, e mandaria a CI-1 por um caminho que falha. O script, o hook e os
três documentos foram corrigidos: teste do `curl` não vale como prova do `WebFetch`;
faça uma chamada de teste antes da CI-1.

**Rota 1b, nova:** `scripts/ler-pagina.sh <slug> <url>` lê a página com `curl`,
salva em `fontes/` e detecta desafio de bot. Medido: lê `tabelaplanos`, `hapvida`,
`tabelasaude` e `meuplanohap` inteiros; o IBGE devolve interstitial do Cloudflare
e o script reprova. Para concorrente — que é o que a CI-1 pede — funciona.

---
