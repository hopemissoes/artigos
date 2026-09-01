# PESQUISA plano-hapvida-aracaju — FASE 0 (state file)

> **Este arquivo em branco REPROVA no `checkpoint_fase0.py` — e é para reprovar.**
> Ele é só o esqueleto com os **nomes de campo exatos** que a trava lê. O conteúdo
> e a ordem das etapas estão em `references/pesquisa.md` da skill — leia lá, não
> reinvente aqui.
>
> Rodar:
> `scripts/cp.sh hapvida-article-builder-v7 checkpoint_fase0.py artigos/plano-hapvida-aracaju/PESQUISA_plano-hapvida-aracaju_COMPLETO.md city | tee artigos/plano-hapvida-aracaju/checkpoints/fase0.txt`

## 1. SERP real (serp_local)

coletado_em: [X]  # serp
- posicoes_principal: [X]
- featured_snippet / formato de snippet: [X]
- URLs concorrentes:
  - [X]

## 2. Kit on-page [V5]

- principal: kw: [X] | volume: [X] | dificuldade: [X]
- secundarias:
  - kw: [X] | intencao: [X] | veredito: qualificada
    <!-- mínimo 6 com "veredito: qualificada" -->
- matriz de posicionamento: [X]
- query fan-out (mínimo 5):
  - [X]

## 3. Contexto local (IBGE / CNES / DATASUS)

- populacao: [X] — fonte: [X] — https://[X]
- leitos / CNES: [X] — fonte: [X]

## 4. Rede assistencial (consultar_rede ANTES da web)

coletado_em: [X]  # rede
<!-- mínimo por tipo: city 5 unidades · hospital 1. Endereço com ≥8 caracteres. -->
### [nome da unidade]
- endereço: [X]
- tipo: [X]
- fonte: [X]
- defensibilidade: 1

## 5. Desmontagem de concorrentes [V4 / CI-1]

<!-- O concorrente tem de ter sido LIDO. Se o egress bloquear, desça a escada de
     rotas da skill e REGISTRE cada tentativa aqui. Não degrade em silêncio. -->
- concorrente: [X] — url: https://[X] — lido_em: [X]
  - matriz de cobertura: [X]

## 6. Ganho de informação / brechas [V4 / CI-2]

- must-match: [X]
- brecha: [X]

## 7. Dado proprietário [V7.2] (consultar_rede · cotador_fila · banco)

- dado_proprietario: [X] — defensibilidade: 1 — fonte: [X]

## 8. Não encontrado [V7.2]

nao_encontrado:
- [X] — onde foi procurado: [X]

## 9. FORBIDDEN_TOKENS

<!-- um token exato por linha: nomes e números que NÃO podem aparecer no artigo.
     Sem este bloco, o checkpoint_verificar.py roda desarmado. -->
FORBIDDEN_TOKENS:
- [X]

## 10. PLANO_MODELOS [V7.2]

<!-- colar aqui o bloco gerado em PLANO_MODELOS_plano-hapvida-aracaju.md -->

## 11. Datas de coleta

coletado_em: [X]  # serp
coletado_em: [X]  # rede
coletado_em: [X]  # concorrentes

## 12. FAQ local

<!-- mínimo por tipo: city 15 · pillar 15 · hospital 10 · tr 8.
     Uma pergunta por linha, terminada em "?", com 5 palavras ou mais. -->
- [X]?

## 13. Anti-doorway

- teste_substituicao: [X]
- dados_unicos: [X]   <!-- mínimo 10 -->
- frases_genericas: [X]
- anti-doorway: [X]   <!-- tem de dizer APROVADO nesta mesma linha -->

## 14. Fio condutor

<!-- 2-3 linhas — copiar também para 00-ESTADO.md -->
