# ESTADO — plano-hapvida-aracaju

> Este arquivo é o **ponto de salvamento** do artigo. Quem abrir uma sessão nova
> lê ele primeiro e continua daqui — sem refazer pesquisa nem readivinhar decisão.
> **Atualize ao fim de cada fase, antes de responder ao usuário.**

## Identificação

- **Slug:** plano-hapvida-aracaju
- **Tipo:** city  <!-- city | hospital | tr | pillar | cobertura -->
- **Skill em uso:** hapvida-article-builder-v7 (camada de ORDEM: v7.1 + v7.4)
- **Aberto em:** 2026-09-01
- **URL de destino:** `/plano-hapvida-aracaju/` (a confirmar com o usuário)
- **Keyword principal:** "plano hapvida aracaju" (inferida do texto — **não** veio de FASE 0)

## Fase atual

- **Fase:** REFORMATAÇÃO DE LAYOUT concluída — artigo em `artigo.html`
- **Natureza do trabalho:** o usuário entregou um artigo **já escrito** (ordem v6) e
  pediu a reformatação do layout para a v7. **Não houve FASE 0** — nenhum dado novo
  foi pesquisado nem afirmado. Todo número do lead-herói já existia no texto original.
- **Próximo passo concreto:** nenhum, do ponto de vista de layout. O que sobrou são
  itens que dependem de material do usuário (URL da imagem de abertura, imagem da
  tabela, title/meta/H1 reais) — ver "Dados que faltam".
- **Bloqueios:** nenhum. **Não abrir FASE 0 por causa deste artigo.** A FASE 0 é o
  portão que antecede a escrita de HTML; aqui o HTML já veio escrito e o pedido era
  de layout. As travas `ci1`, `suficiencia`, `verificar` e `doorway_final` não rodam
  porque leem o state file de pesquisa — é limitação de ferramenta em artigo herdado,
  não pendência de trabalho. Se um dia surgir dúvida sobre um dado do texto, o
  caminho é a auditoria MODO 1 (veracidade) sobre o dado específico, não refazer
  pesquisa inteira.

## Portões

| Portão | Status | Evidência |
|---|---|---|
| CI-1 — concorrente lido (`checkpoint_ci1.py`) | ➖ não se aplica | artigo herdado; trava lê o state file |
| FASE 0 (`checkpoint_fase0.py`) | ➖ não se aplica | o pedido foi de layout, não de artigo novo |
| Aprovação humana do state file | ➖ não se aplica | idem |
| Suficiência (`checkpoint_suficiencia.py`) | ➖ não se aplica | trava lê o state file |
| Kit on-page (`checkpoint_onpage.py`) | 🟡 parcial | `checkpoints/onpage.txt` — principal ok; secundárias/H1/title/URL/meta não informados |
| Preço-primeiro / lead-herói (`checkpoint_preco_primeiro.py`) | ✅ aprovado | `checkpoints/preco_primeiro.txt` — 0 avisos |
| Tamanho de parágrafo (`checkpoint_paragrafos.py`) | ✅ aprovado | `checkpoints/paragrafos.txt` — 0 reprovados, 20 no limite |
| Ritmo visual (`checkpoint_ritmo_visual.py`) | ✅ aprovado | `checkpoints/ritmo_visual.txt` — 1 seção em aviso (4 P) |
| Citabilidade (`checkpoint_citabilidade.py`) | 🟡 1 reprovação | `checkpoints/citabilidade.txt` — é a seção de FAQ; ver Decisões |
| Voz humana (`checkpoint_voz.py`) | ✅ aprovado | `checkpoints/voz.txt` — 0 🔴; 🟡 densidade de travessão (herdada) |
| Completude (`checkpoint_completude.py`) | ✅ aprovado | `checkpoints/completude.txt` — 13 H2, 18 FAQ, 5.5k palavras |
| `[VERIFICAR]` / tokens proibidos (`checkpoint_verificar.py`) | ➖ não se aplica | exige `FORBIDDEN_TOKENS` do state file |
| Varredura anti-doorway final (`checkpoint_doorway_final.py`) | ⬜ rodável | precisa das âncoras + HTML dos artigos irmãos, não do state file |
| Registro no banco Supabase | ⬜ pendente | só depois do artigo aprovado |

Legenda: ✅ aprovado (saída em `checkpoints/`) · 🟡 rodado, com ressalva · ⬜ pendente ·
➖ não se aplica a artigo herdado (a trava lê o state file da FASE 0)

## Decisões tomadas

- 2026-09-01 — pasta criada, tipo city.
- 2026-09-01 — original preservado em `fontes/artigo-original-v6.html`; a reformatação
  é reprodutível por `build_v7.py` (recorta os blocos do original e remonta).
- 2026-09-01 — **ordem v7.4 aplicada:** lead-herói navy (1º elemento) → S2↑a (H2 de preço
  + contexto + `[aracaju_menortabela]`, `id="precos"`) → sumário → `id="cotacao-1"` →
  S2↑b (box Importante + análise) → Coparticipação (2º H2 de preço, agrupado no topo) →
  S1 → Tipos → Rede → Hospital → Cobertura → Comparativo → CTA inter → Carências →
  Tecnologia → Contratação → FAQ → CTA final → Conclusão.
- 2026-09-01 — **o lead virou o herói.** Os 3 parágrafos do lead antigo saíram: os fatos
  já estavam repetidos no box "Resumo Rápido" da S1 e a passagem citável do herói os
  carrega. O parágrafo "Neste guia, você vai encontrar…" foi eliminado por ser
  autorreferência (proibida no herói pela v7.4) e molde de IA (`voz-humana.md`).
- 2026-09-01 — **link externo do IBGE preservado**: migrou do lead extinto para o fim da S1,
  como nota de fonte demográfica.
- 2026-09-01 — **sumário reordenado** para bater com a nova ordem e ganhou o item laranja
  "Faça uma Cotação" → `#cotacao-1`, que não existia. Ficou com 14 itens (13 seções + CTA);
  o limite da skill é 10-11 porque pressupõe 7 seções — este artigo tem 13 H2.
- 2026-09-01 — **ano fixo → shortcode:** "Tabela de Preços Hapvida Aracaju 2026" virou
  `[ano_atual]` (H2 e sumário) e a nota de rodapé virou "Dados de preços atualizados em
  `[mes_atual]` de `[ano_atual]`". "R$ 2 bilhões até 2026" ficou: é meta datada, não data corrente.
- 2026-09-01 — **H2 da conclusão deixou de citar preço** ("Menor Preço, Rede em Expansão…"
  → "Rede em Expansão e Cobertura Nacional"): como H2 de preço no rodapé, disparava o
  aviso de "H2 de preço fora do bloco do topo" da regra 2 da v7.
- 2026-09-01 — **duas transições reescritas** porque a reordenação as tornou falsas:
  "A seguir, detalhamos cada tipo de plano" → aponta agora para a coparticipação.
- 2026-09-01 — **tipografia de corpo 17px/1.9 → 18px/1.7** (padrão da skill). Efeito
  colateral importante: os `checkpoint_paragrafos.py`, `ritmo_visual.py` e
  `citabilidade.py` só enxergam `<p>` de corpo em **18px** — no original eles passavam
  **vazios** (falso "aprovado"). Com a correção passaram a medir de verdade.
- 2026-09-01 — **5 parágrafos acima de 480 chars quebrados** em fronteira de frase
  (nenhuma palavra alterada), conforme a trava obrigatória de `checkpoint_paragrafos.py`.
- 2026-09-01 — **H3 "O novo hospital do Grageru"** inserido na seção do Gabriel Soares:
  a quebra acima deixou 6 `<p>` seguidos e o ritmo visual reprovou.
- 2026-09-01 — **`<style>`/`<script>` recuperados do wpautop.** O original tinha `<br />`
  no fim de cada linha dos dois blocos (sinal de colagem no editor visual): o JS do grifo
  animado **não rodava** e a maior parte do CSS estava quebrada. Blocos remontados limpos.
- 2026-09-01 — **citabilidade: a reprovação da seção de FAQ não foi "corrigida".** O
  template de FAQ da própria skill (`components.md` → "FAQ Structure") vai do H2 direto
  para os `<details>`, sem `<p>` de corpo. Escrever um parágrafo de abertura ali seria
  inventar texto novo num artigo herdado. Fica registrado como limite do script.
- 2026-09-01 — **ritmo visual: o aviso de 4 `<p>` na seção do Gabriel Soares fica.** Há uma
  linha do tempo entre o 2º e o 3º parágrafo — quebra visual legítima pela tabela da skill —,
  mas o tokenizador do script não reconhece aquele `<div>` como break.

## Dados que faltam

- **Conteúdo herdado, não conferido por mim.** Rede, hospitais, números de mercado e o
  comparativo com Unimed/Plamed vieram prontos no arquivo enviado. Eu não os alterei nem
  os verifiquei. Isso **não** é motivo para abrir FASE 0: se algum dado específico levantar
  dúvida, o caminho é a auditoria MODO 1 (veracidade) naquele dado.
- **`<figure>` de abertura ausente** — a v7.4 manda a imagem descer para dentro da S1;
  aqui não há imagem nenhuma no artigo. Falta a URL (o usuário fornece; nunca inventar).
- **Imagem da tabela de preço ausente** (`gerar_imagem_artigo.py`) — o artigo tem seção de
  preço e, pela v6/v7, deveria fechar a S2↑b com a `<figure>` da tabela.
- **Perfil de links abaixo do mínimo da skill:** hoje 1 link externo (IBGE) para um mínimo
  de 2, e 2 destinos internos para um mínimo de 5 (3 pillars + 2 cross-links de cidade).
  A URL `plano-de-saude-hapvida-carencia` aparece 2× (a regra é máx. 1× por URL).
- Título SEO, meta description, H1 e slug reais não foram informados — `checkpoint_onpage.py`
  não pôde conferi-los.

## Fio condutor

<!-- Não definido por FASE 0. O ângulo que o texto herdado carrega, e que o lead-herói
     preserva: Aracaju é mercado de três operadoras, com a Hapvida ganhando pelo preço e
     por uma rede própria concentrada no eixo Centro–São José, em expansão para o Grageru. -->
