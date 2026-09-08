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
- **Keyword principal:** plano de saúde hapvida infantil (140/mês, KD 2) — o campo de marca soma ~860/mês
- **Title SEO proposto:** Plano de Saúde Hapvida Infantil: Valores 2026 por Cidade
- **H1 proposto:** Plano de saúde Hapvida infantil: quanto custa e o que cobre
- **Meta proposta:** Veja o valor do plano de saúde Hapvida infantil em 2026, faixa 0 a 18 anos, o que cada modalidade cobre e as regras de carência do bebê.

## Fase atual

- **Fase:** ✅ **PUBLICADO** no WordPress em 08/09/2026 às 10:15, a pedido expresso
  do usuário. Post 12185, corpo sobrescrito de 64.596 para 78.514 caracteres.
  Conteúdo conferido no ar com cache furado: sha256 do corpo idêntico ao
  `artigo.html`, 16 FAQ, 2 quadros compensa/não compensa, 2 fontes oficiais,
  10 grifos, 1 figcaption e **os 16 shortcodes da tabela resolvidos**
  (Fortaleza R$ 107,83 · BH R$ 71,98 · SP R$ 56,94 · Belém R$ 101,96 na 1ª coluna).
- **Próximo passo concreto:** decidir sobre o que NÃO foi tocado (só a pedido):
  meta title, meta description e H1 continuam os antigos; `registrar_atualizacao`
  e `registrar_links_artigo` no Supabase não foram gravados; schema JSON-LD segue
  pendente.
- **Bloqueios:** nenhum bloqueio técnico. Falta a aprovação humana do artigo.

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
| Aprovação humana do state file | ✅ aprovado | usuário: "sim, siga" (08/09) |
| Suficiência (`checkpoint_suficiencia.py`) | ✅ aprovado | `checkpoints/suficiencia.txt` — 0 seção órfã · 8% FAQ sem âncora · ganho nível 1 |
| Tamanho de parágrafo (`checkpoint_paragrafos.py`) | ✅ aprovado | `checkpoints/artigo-completo.txt` — 39 `<p>`, nenhum >380 chars |
| Ritmo visual (`checkpoint_ritmo_visual.py`) | ✅ aprovado | 11 seções, nenhuma com 4+ `<p>` seguidos |
| Citabilidade GEO/AEO (`checkpoint_citabilidade.py`) | ✅ aprovado | 7 aberturas na faixa ideal, 3 aceitáveis, 0 reprovadas |
| Kit on-page (`checkpoint_onpage.py`) | ✅ aprovado | `checkpoints/onpage.txt` — principal em H1/title/URL/meta/1º parágrafo/2 H2; secundárias em 5 H2 |
| Preço-primeiro / lead-herói (`checkpoint_preco_primeiro.py`) | 🟡 exceção registrada | Regras 0, 2 e formulário ✅. Regra 1 vermelha por desenho: a tabela é feita de 16 shortcodes `_0` (pontuais), que o script não conta como tabela. Decisão do usuário (opção A) documentada no state file |
| Voz humana (`checkpoint_voz.py --rigor alto`) | ✅ aprovado | 3.351 palavras · nenhum tique bloqueante · nenhum aviso de densidade |
| Completude (`checkpoint_completude.py`) | ✅ aprovado | 10 H2 · 16 FAQ · 3.415 palavras · 2 fontes oficiais · 1 guia-box · Dica DRV · seção de rede |
| `[VERIFICAR]` / tokens proibidos (`checkpoint_verificar.py`) | ✅ aprovado | nenhum dado marcado afirmado no texto |
| Varredura anti-doorway final (`checkpoint_doorway_final.py`) | ✅ aprovado | `checkpoints/doorway-final.txt` — D1 11,8% (limite 45%) · D2 nenhuma seção sem âncora · D4 0,0% de sobreposição com os 3 irmãos |
| 🚦 **PORTÃO HUMANO — aprovação do artigo** | ✅ aprovado | usuário: "atualize agora o meu artigo no wordpress" (08/09) |
| Publicação no WordPress (post 12185) | ✅ feito | dry-run + apply + conferência no ar; backups em `fontes/wp-12185-antes.html` e `wp-12185-depois.html` |
| Imagem da tabela de preço | ❌ **não se aplica** | decisão do usuário (08/09): o artigo tem **uma imagem só**, a de abertura. Não existe imagem de tabela, e os valores saem **apenas dos shortcodes da tabela de 4 cidades** |
| Schema JSON-LD | ⬜ pendente | execução separada, só quando o usuário pedir |
| Registro no banco Supabase (`registrar_atualizacao`, `registrar_links_artigo`) | ⬜ pendente | REGRA ZERO: só com pedido expresso |
| Meta title / meta description / H1 no WordPress | ⬜ pendente | continuam os antigos; H1 no ar ainda é "Como escolher o melhor plano de saúde hapvida infantil para seu filho" |

Legenda: ⬜ pendente · 🟡 rodado, com ressalva · ✅ aprovado (saída em `checkpoints/`)

## Decisões tomadas

<!-- uma linha por decisão, com data. Serve para a próxima sessão não reabrir. -->
- 2026-09-08 — pasta criada, tipo pillar.
- 2026-09-08 — **URL mantida**, sem 301: a página é #2 orgânica nas duas head
  keywords e fonte #1 do AI Overview de "valor do plano da hapvida infantil";
  tem 8 links internos apontando para ela. Detalhe em `FASE-P0.md`.
- 2026-09-08 — **eixo mantido no campo de marca** (~860 buscas/mês). As
  secundárias genéricas ("plano de saude infantil valores" 880, "individual" 590)
  saem deste kit: 5 dos 9 primeiros orgânicos delas são multimarca. Medição em
  `DECISAO-ARQUITETURA.html`. O artigo multimarca ficou fora de escopo a pedido
  do usuário ("esqueça a multimarca").
- 2026-09-08 — **opção A: tabela de 4 cidades mantida**, com a exceção do
  `checkpoint_preco_primeiro` registrada por escrito no state file.
- 2026-09-08 — link para odontológico corrigido para a **URL canônica**
  `/plano-odonto-hapvida/` (a URL antiga responde 200 mas canonicaliza para essa).
- 2026-09-08 — **bug da skill corrigido no artigo**: o `<style>` obrigatório traz
  `.v5-hero-conv>p{display:none!important}`, que esconderia o parágrafo citável
  do lead-herói da v7.4. Trocado por `display:block!important` e retirado da lista
  anti-wpautop.
- 2026-09-08 — anti-doorway de pillar é medido **por produto**, não por cidade:
  `checkpoints/ancoras-produto.txt` (20 âncoras: infantil, criança, bebê,
  pediatra, faixa 0 a 18...). Com âncora de cidade o script reprova por desenho.

## Dados que faltam

- **Nada.** A `<figure>` da tabela de preço foi encerrada por decisão do usuário
  (08/09): o artigo tem **uma imagem só**, a de abertura
  (`img-plano-hapvida-infantil.webp`, com `alt`, `title` e `figcaption`).
- Os **valores de preço saem exclusivamente dos 16 shortcodes** da tabela de
  4 cidades. Não há tabela de 10 faixas etárias a levantar, nem shortcode de
  tabela agregada a criar. Isso torna a exceção do `checkpoint_preco_primeiro`
  **permanente**, não um contorno temporário.
- `checkpoint_verificar` verde: nada marcado `[VERIFICAR]` no corpo.

## Fio condutor

A criança não tem plano próprio: ela é a faixa mais barata da mesma tabela do
adulto. O que decide o preço dela não é a idade — é a **praça** e a **coluna**
(ambulatorial ou Nosso Plano, coparticipação total ou parcial). O artigo mostra
a mesma criança custando valores diferentes em quatro cidades e ensina a
comparar coluna com coluna, não cidade com cidade.
