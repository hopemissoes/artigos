# ROTEAMENTO — qual skill para qual pedido

Este é o documento que impede o erro mais caro: **produzir sem a skill certa**.
Leia antes de aceitar qualquer tarefa. Se o pedido não se encaixar em nenhuma
linha, **pergunte** — não improvise.

---

## Ordem de decisão (siga nesta ordem)

1. **É um artigo?** → qual arquétipo? (Hapvida / cobertura / bookkeeping / Mowana)
2. **É uma pergunta sobre dado?** → banco, DataForSeo ou `hapvida-data`?
3. **É um juízo sobre desempenho?** → OODA (análise) ou diagnóstico (veredito)?
4. **É conferência do que já está no ar?** → auditor.
5. **Nenhuma das anteriores** → pergunte antes de agir.

---

## 1. Produção de artigo

| Arquétipo | Skill | Gatilhos |
|---|---|---|
| Cidade (S1-S7), hospital (HS1-HS4), tabela regional (TR1-TR5), pillar (P1-P9) — tabelaplanos.com.br | **`hapvida-article-builder-v7`** | "artigo de [cidade]", "artigo do hospital", "tabela de preço [estado]", "artigo do plano", "preço primeiro", "lead-herói", "multiagente" |
| Mesma coisa, mas em versão anterior | `hapvida-article-builder-v6` / `-geo` | só sob pedido explícito ("faz na v6", "versão GEO") |
| "Hapvida cobre [exame/procedimento]?" — pillar `/cobertura/` (C1-C7) | **`hapvida-coverage-builder`** | "Hapvida cobre", "cobertura de", "carência de [proc]", "TUSS", "Rol ANS", nome de exame (ressonância, tomografia, endoscopia…) |
| Bookkeeping, EUA, inglês (Location L1-L7, Service S1-S7, Guide G1-G7) | **`bookkeeping-article-builder-v5`** | "bookkeeping article", "location page", "service page", cidade/estado dos EUA em contexto contábil |
| Artigo assinado pela pastora Mowana, feito dos livros dela | **`mowana-article-builder`** | "artigo da Mowana", "a partir do livro", "artigo cristão", "checa a fidelidade" |

**Regra de precedência entre versões:** o `CLAUDE.md` declara a versão padrão do
repo (hoje **v7**). Essa declaração é a autorização explícita que as skills v5+
exigem. Pedido do usuário na hora vence a declaração do repo.

**Trava comum a todas:** FASE 0 (pesquisa) antes de qualquer HTML, com state file
aprovado e checkpoint colado. Sem isso, não começa.

---

## 2. Dado

| Pedido | Skill | Observação |
|---|---|---|
| Consultar/criar/editar artigo, hospital, link, FAQ, pendência, backlink, dado canônico, coparticipação, overlap, histórico | **`banco-tabelaplanos`** | **Obrigatória antes de QUALQUER ferramenta `BD - Consultar/Criar/Editar/backlinks`.** Ela dá o nome exato da função, dos parâmetros e a ordem das chamadas. |
| Volume, dificuldade, posição real na SERP, keyword do concorrente, perguntas relacionadas, citação em IA | **`dataforseo-tabelaplanos`** | Traz `location_code`, formato exato de entrada, custo e os erros conhecidos (401, 40204, 40503) |
| Número corporativo da Hapvida, tabela de coparticipação, linha de produto, Qualivida, carência, credencial da DRV | **`hapvida-data`** | **Já validado — não pesquise na web antes de olhar aqui.** |
| Regra da ANS, portabilidade, reajuste, comparativo com Unimed/Bradesco/SulAmérica/Amil | **`hapvida-regulatory`** | Diz ONDE e O QUE pesquisar; não contém o dado |
| "quais cidades já fizemos", FAQ já usada, overlap, anti-doorway | **`hapvida-article-database`** | Ler ANTES de artigo novo; atualizar DEPOIS do Bloco C aprovado |
| GSC / GA4 (páginas, queries, tráfego) | ferramentas `seo-tools` | Sob o protocolo da OODA quando virar análise |

---

## 3. Juízo sobre desempenho

| Pedido | Skill | Por quê |
|---|---|---|
| "por que essa página não sobe?", "analisa o cluster", "vale a pena essa keyword?", "compara períodos" | **`hapvida-ooda`** | Protocolo anti-contradição: fixa escopo (≥5 keywords + URLs reais) antes de coletar |
| "está canibalizando?", "qual URL rankeia?", veredito pontual | **`hapvida-diagnostico`** | Roda script de veredito; **tem precedência** sobre o auditor para veredito pontual |
| "audita o artigo", "o que está errado", health check, E-E-A-T, links quebrados | **`hapvida-seo-auditor`** | Cruza banco + WordPress e gera relatório priorizado |
| Pendências, backlog, prioridade, "resolvi isso" | **`pendencias-tabelaplanos`** | ⚠️ **Nunca grava pendência sem autorização expressa do usuário** |

---

## 4. Skills que NÃO devem ser acionadas

| Skill | Motivo |
|---|---|
| `hapvida-research` | **Descontinuada.** Absorvida pela FASE 0 da builder. Se disparar por engano, redirecione. |
| `hapvida-article-builder` v1-v5 | Superadas pela versão padrão do repo; só sob pedido explícito e comparativo |

---

## 5. Antipadrões observados (o que já deu errado)

- **Trabalhar sem skill.** Escrever artigo "no talento" produz doorway e dado
  YMYL inventado. Se você não citou uma skill, você está errado.
- **Trabalhar no repositório errado.** Todo artefato de artigo vive aqui, em
  `artigos/<slug>/`.
- **Chamar MCP `BD - *` por tentativa e erro** em vez de ler `banco-tabelaplanos`.
- **Chamar `serp_local`/`keyword_data` avulso e dizer que "a pesquisa está feita".**
  Pesquisa diagnóstica não é FASE 0.
- **Pular o portão humano** porque o usuário pediu o HTML direto. A resposta certa
  é mostrar o checkpoint e o que falta.
- **Perder o fio entre sessões.** Sem `00-ESTADO.md` atualizado, a próxima sessão
  refaz pesquisa e contradiz a anterior.
