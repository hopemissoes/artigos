# PLANO_MODELOS — hapclinica-duque-de-caxias-manaus

- tipo: hospital (unidade ambulatorial, HS1-HS4)
- escrito em: 2026-08-31
- autor: Agente 22 (roteador). Escrito pelo orquestrador — T5 proíbe delegar
  tarefa pequena, e a validação de verdade é o `checkpoint_modelos.py`, não a
  assinatura de quem digitou.

## Nota de honestidade sobre o Estágio 1

O Estágio 1 (pesquisa) e a conferência de fatos **já foram executados antes de a
linha ser autorizada**, pelo orquestrador em agente único, e passaram nas três
travas mecânicas (`checkpoint_ci1`, `checkpoint_fase0`, `checkpoint_suficiencia`)
e no portão humano. As linhas 1 a 5, CI-1 e CI-2 abaixo registram o que de fato
aconteceu — não um plano a executar. Elas ficam declaradas no modelo do
orquestrador para que a T2 seja comparada contra a realidade, e não contra uma
ficção conveniente: é por isso que o Agente 6 (conferente de fatos) e o Agente 13
(anti-doorway) rodam em modelo diferente do orquestrador.

O que a linha executa de fato, a partir daqui: 6, 7, 23, 24, 8, 9, 10, 11, 19,
20, 12, 13, 14, 15, 16a, 16b, 16c, 21, 17, 18.

PLANO_MODELOS:
22 | roteador-modelos      | barato | haiku  | escrito pelo orquestrador (T5)
1  | serp-tipo-pagina      | medio  | opus   | JA EXECUTADO no Estagio 1 pelo orquestrador
2  | rede-assistencial     | medio  | opus   | JA EXECUTADO — ficha CNES 9505970 + catalogo
3  | contexto-local        | barato | opus   | JA EXECUTADO — IBGE Censo 2022
4  | keywords-fanout       | medio  | opus   | JA EXECUTADO — DataForSeo
CI-1 | desmontagem         | forte  | opus   | JA EXECUTADO — 4 concorrentes lidos por WebFetch
CI-2 | ganho-informacao    | forte  | opus   | JA EXECUTADO — ganho nivel 1
5  | sintese-fio-condutor  | forte  | opus   | JA EXECUTADO — fio condutor no 00-ESTADO
6  | conferente-fatos      | forte  | sonnet | T2 com o 2 (opus) — confere a pesquisa ja feita
23 | juiz-pesquisa-a       | forte  | sonnet | T3b modelo != do 5 (opus)
24 | juiz-pesquisa-b       | forte  | fable  | T3b modelo != do 23 e != do 5
7  | conferente-dataforseo | barato | haiku  | T2 com o 4 (opus)
8  | redator-bloco-a       | forte  | sonnet | T2 com o 11 (opus)
9  | redator-bloco-b       | medio  | sonnet | T2 com o 11 (opus)
10 | redator-bloco-c       | medio  | sonnet | T2 com o 11 (opus)
11 | editor-chefe          | forte  | opus   |
19 | voz-humana            | medio  | sonnet | T2 com o 11 (opus)
20 | imagem-abertura       | barato | haiku  | artigo de unidade nao tem tabela de preco; aqui e so a figure de abertura
12 | veracidade            | forte  | opus   |
13 | anti-doorway          | forte  | sonnet | T2 com o 5 (opus)
14 | requisitos            | medio  | sonnet |
15 | citabilidade-geo      | forte  | opus   |
16a| juiz-factual          | forte  | opus   |
16b| juiz-doorway          | forte  | sonnet | T3 — lente B em modelo distinto
16c| juiz-leitor           | forte  | fable  | T3 — juiz != editor-chefe (opus) e != redatores (sonnet)
21 | varredura-doorway     | forte  | opus   | T2 com o 13 (sonnet)
17 | schema                | medio  | sonnet | execucao separada, so quando o usuario pedir
18 | registro-banco        | barato | haiku  | so depois do artigo aprovado

## Diversidade declarada

- Modelos distintos em uso: **4** (opus, sonnet, fable, haiku). Não é monomodelo.
- Painel final: 16a opus · 16b sonnet · 16c fable → 3 modelos distintos, e o 16c
  não coincide com o editor-chefe (opus) nem com os redatores (sonnet).
- Portão de pesquisa: 23 sonnet · 24 fable → distintos entre si e ambos distintos
  do Agente 5 (opus), que sintetizou a pesquisa.
