# Skill v7 × concorrente descontoplanodesaude.com.br (08/09/2026)

## 1. O método dela é template, e repete

Quatro artigos lidos inteiros (infantil, carência, cirurgias, psicólogo):

| Artigo | Palavras | H2 | H3 | FAQ | Fonte oficial | Sobre este guia | Leitura |
|---|---|---|---|---|---|---|---|
| plano-hapvida-infantil | 4.692 | 27 | 15 | 15 | 3 | 1 | 19 min |
| carencia-hapvida | 4.361 | 26 | 12 | 15 | 3 | 1 | 18 min |
| quais-cirurgias-o-hapvida-cobre | 4.951 | 22 | 21 | 15 | 3 | 1 | 19 min |
| psicologo-hapvida | 2.926 | 22 | 5 | 15 | 3 | 1 | 18 min |

Rodapé idêntico nos quatro: Erros comuns → Vale a pena → Conclusão: [keyword] →
Perguntas frequentes (15) → Sobre este guia → bio do autor → CTA.

## 2. A skill cobre — e duas coisas já vieram dela

A v7.6 nasceu da CI-1 na página `fonoaudiologia-hapvida` do mesmo site (05/09/2026):
cartão "Fonte oficial" e caixa "Sobre este guia" são de lá, hoje obrigatórios e
travados no `checkpoint_completude.py`. FAQ 15-17, 8-9 H2, 15-28 H3, citabilidade,
autor/Person, countup/trust, linha-resumo, quadro comparativo e nota de rodapé com
data: tudo já está na skill, com régua igual ou mais alta.

NÃO coberto (2 itens menores): seção fixa "Erros comuns na hora de…" (a skill trata
erros comuns como conteúdo do pillar Como Contratar) e "Leitura de X minutos".
A skill é MAIS forte num ponto: P9 exige as duas listas (compensa / não compensa);
ela só publica o lado positivo.

## 3. O buraco é a página, não a skill

`plano-de-saude-hapvida-infantil` é `pillar_produto` (arquétipo P1-P9) e reprovaria
no checkpoint da própria skill:

| Requisito | Mínimo | Na página |
|---|---|---|
| H2 de corpo | 8 | 7 |
| H3 | 15 | 3 |
| FAQ (details) | 12 | 7 |
| cartão fonte-oficial | 1 | 0 |
| caixa guia-box | 1 | 0 |
| schema com Person | obrigatório | ausente |
| palavras | 2.500 (alvo 3.500-4.500) | 2.711 |
| links internos únicos | 8 | 21 (ok) |
| links externos | 2 | 3 (ok) |

A página é de 2024 e foi construída antes da v7.

## Correções do documento anterior

- "Falta linha-resumo sob cada H2" — já existe na página.
- "Falta link para fonte oficial" — os links existem (planalto + gov.br/ans);
  o que falta é o cartão `fonte-oficial` da v7.6 (0 ocorrências no HTML).

Documento visual: `comparativo.html`. Textos completos: `dados/*.md`.
CI-1: rota 2 (workflow n8n `NUUZmP5y4AtFb2jL`) — egress externo bloqueado.
