# ESTADO — plano-de-saude-hapvida-infantil

> Este arquivo é o **ponto de salvamento** do artigo. Quem abrir uma sessão nova
> lê ele primeiro e continua daqui — sem refazer pesquisa nem readivinhar decisão.
> **Atualize ao fim de cada fase, antes de responder ao usuário.**

## Identificação

- **Slug:** plano-de-saude-hapvida-infantil
- **Tipo:** pillar  <!-- city | hospital | tr | pillar | cobertura -->
- **Skill em uso:** hapvida-article-builder-v7
- **Aberto em:** 2026-09-08
- **URL de destino:** https://tabelaplanos.com.br/plano-de-saude-hapvida-infantil/ (MANTER — sem 301)
- **Keyword principal:** plano hapvida infantil (a decidir no DR2: "valor do plano da hapvida infantil" é a de maior clique)

## Fase atual

- **Fase:** FASE 0 concluída (DR1+DR2) → **aguardando o PORTÃO HUMANO** para liberar o Bloco A
- **Próximo passo concreto:** o usuário aprovar (ou corrigir) o state file. Aprovado,
  entra o Bloco A na ordem v7.5: lead-herói → H2 de preço + tabela → formulário → sumário
- **Bloqueios:** nenhum bloqueio técnico; falta só a aprovação humana do state file

## DECISÃO DE ARQUITETURA (2026-09-08) — duas páginas, não uma

O usuário propôs separar marca × genérico. **Medido e confirmado:** a SERP de
"plano de saúde infantil valores" é multimarca (5 dos 9 orgânicos comparam operadoras;
o #1 é "Preços de 12 Operadoras"); o concorrente líder (tabelasaude) já opera as duas
páginas separadas; e esta página é a 2ª mais forte do site (347 cliques · 15.148
impressões · pos. 4,9 em 28 dias) — não é caso de trocar o eixo. Campo genérico
≈ 4.600 buscas/mês (KD 0-6) contra ≈ 860 do campo de marca.

- **Esta página:** reforma dentro do campo de marca. Secundárias genéricas SAEM do kit.
- **Artigo novo (a abrir):** multimarca para "plano de saúde infantil" — FASE 0 própria,
  depois que esta reforma estiver publicada.
- **Sem canibalização com** `/plano-de-saude-para-recem-nascido/`: ele vive de "bebê/RN"
  e não recebe nenhuma busca com "infantil" ou "criança".
- Documento com as medições: `DECISAO-ARQUITETURA.html`.

## FASE 0 — veredito (2026-09-08)

- **Eixo (P4):** o preço do plano infantil não muda com a idade — muda com a praça e a
  modalidade. Defensibilidade 1 (tabela vigente por cidade). Nenhum dos 3 concorrentes
  lidos monta essa comparação.
- **Keyword principal:** plano de saúde hapvida infantil (140/mês, KD 2). Campo de marca
  soma 860/mês. Secundárias genéricas de alto volume e KD 0-6: "plano de saúde infantil
  valores" (880), "…individual" (590), "…individual preço" (210), "…barato" (140).
- **Descartadas pelo veto de intenção:** todo o cluster de emergência infantil (390+320+320)
  — é de quem já é cliente e pertence a `/urgencia-e-emergencia-hapvida/`. Vira link.
- **Ressalva do checkpoint:** as 2 "FAQ sem âncora" apontadas pela trava de suficiência são
  H2 do concorrente citados na seção 5, não perguntas nossas.
- **MODO: monomodelo** declarado — a linha de 25 agentes não foi disparada; o portão humano
  vale mais e nenhuma trava mecânica foi dispensada.

## FASE P0 — veredito (2026-09-08) · detalhe em `FASE-P0.md`

- **Causa:** CONTEÚDO. A página é #2 orgânica nas duas keywords-cabeça e é fonte nº 1
  do AI Overview em "valor do plano da hapvida infantil" — mas está abaixo do mínimo do
  arquétipo P1-P9 em 6 itens (7 H2/mín. 8 · 2 H3/mín. 15 · 7 FAQ/mín. 12 · 0 cartão
  fonte-oficial · 0 guia-box · schema sem Person).
- **URL:** MANTER. 8 links internos apontam para ela e o AI Overview a cita pela URL.
  Contraponto registrado: o slug não tem "valor"/"preço", que é o que a demanda pede.
- **Canibalização:** parcial e não bloqueante — `/tabela-de-preco-hapvida/` aparece em
  #9 na mesma SERP em que a página é #2. Vigiar na Fase 5. A home não aparece.
- **Trava da reforma:** a passagem de preço atual é a que a IA extrai. Ampliar, nunca
  substituir o enquadramento.

## Portões

| Portão | Status | Evidência |
|---|---|---|
| CI-1 — concorrente lido (`checkpoint_ci1.py`) | ✅ aprovado | `checkpoints/ci1.txt` — 3 lidos (desconto 43 headings · tabelasaude 22 · joov 7), rota n8n |
| FASE 0 (`checkpoint_fase0.py`) | ✅ aprovado | `checkpoints/fase0.txt` — 25 FAQ · 8 secundárias · 7 dados nível 1-2 · 9 fan-out |
| Aprovação humana do state file | ⬜ pendente | |
| Suficiência (`checkpoint_suficiencia.py`) | ✅ aprovado | `checkpoints/suficiencia.txt` — 0 seção órfã · 8% FAQ sem âncora · ganho nível 1 |
| Kit on-page (`checkpoint_onpage.py`) | ⬜ pendente | |
| Preço-primeiro / lead-herói (`checkpoint_preco_primeiro.py`) | ⬜ pendente | |
| Voz humana (`checkpoint_voz.py`) | ⬜ pendente | |
| Completude (`checkpoint_completude.py`) | ⬜ pendente | |
| `[VERIFICAR]` / tokens proibidos (`checkpoint_verificar.py`) | ⬜ pendente | |
| Varredura anti-doorway final (`checkpoint_doorway_final.py`) | ⬜ pendente | |
| Registro no banco Supabase | ⬜ pendente | |

Legenda: ⬜ pendente · 🟡 rodado, com ressalva · ✅ aprovado (saída em `checkpoints/`)

## Decisões tomadas

<!-- uma linha por decisão, com data. Serve para a próxima sessão não reabrir. -->
- 2026-09-08 — pasta criada, tipo pillar.

## Dados que faltam

<!-- o que ficou como [VERIFICAR] ou nao_encontrado, e onde procurar -->

## Fio condutor

<!-- 2-3 linhas: a voz e o ângulo único deste artigo (Agente 5). Todos os blocos
     honram isto. Preencher ao fim da FASE 0. -->
