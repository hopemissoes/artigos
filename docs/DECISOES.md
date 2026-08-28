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
