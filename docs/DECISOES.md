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

> 🔁 **SUPERADA no mesmo dia, no ponto do egress.** O ambiente passou para o nível
> `Full` e o `WebFetch` voltou a funcionar — ver a entrada *"Acesso de rede do
> ambiente: `Full`"*, logo abaixo, e a de 28/08 sobre Desktop × Claude Code. O
> registro fica como está para preservar a medição e a causa do incidente de
> 27/08. **O que continua valendo:** o `scripts/testar-egress.sh` antes de toda
> CI-1, e a vantagem do modelo por subagente.

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

**~~Pendente com o usuário~~ — RESOLVIDO em 28/08:** liberar a rede do environment
resolve na origem e devolve o `WebFetch`. É a rota 1, e é a preferida. O usuário
escolheu o nível `Full`; medido livre em 28/08 (5 alvos, nenhum bloqueado).

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

## 2026-08-28 — "Desktop" são duas coisas, e só uma delas degrada a v7

**Contexto:** a entrada acima e o `docs/LINHA-V7.md` dizem que "o Desktop não
permite modelo por subagente". Está certo, mas é ambíguo — e a ambiguidade
subestima o ambiente local do usuário.

**Distinção:**

| Onde | Disco local + git | Modelo por subagente | v7 |
|---|---|---|---|
| **Claude Code** (terminal do Windows ou app desktop) | ✅ | ✅ | **completa** — é o ambiente para o qual os `SKILL.md` foram escritos; os caminhos `C:\Users\netop\...` são literais lá |
| **Claude Desktop, o app de chat** | ⚠️ só por download manual, ou por conector local de sistema de arquivos | ❌ | **degradada** — `MODO: monomodelo` |

**Consequência:** ao dizer "no Desktop", pergunte qual dos dois. Teste de 10
segundos: peça um `git status`. Se rodar, é Claude Code e a v7 roda inteira.

**O que salvar em disco NÃO resolve:** a independência dos juízes. Os pares
proibidos de compartilhar modelo (`2×6`, `4×7`, `8/9/10×11`, `11×19`, `5×13`,
`13×21`) não são um problema de arquivo. No app de chat, declare `MODO:
monomodelo` no state file e reforce o portão humano.

**A ponte entre os dois mundos é este repositório:** trabalhando num clone local,
`00-ESTADO.md` e checkpoints viajam por `git push`/`pull`, e cada sessão continua
de onde a outra parou. É para isso que serve a regra 7 do `CLAUDE.md`.

---
