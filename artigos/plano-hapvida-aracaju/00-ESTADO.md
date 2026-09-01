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

- **Fase:** LAYOUT v7.4 + FASE 0 + CORREÇÕES DO RELATÓRIO aplicadas. Artigo pronto
  para publicação, pendente dos itens que dependem de material do usuário.
- **Natureza do trabalho:** o usuário entregou um artigo **já escrito** (ordem v6) e
  pediu a reformatação do layout para a v7. **Não houve FASE 0** — nenhum dado novo
  foi pesquisado nem afirmado. Todo número do lead-herói já existia no texto original.
- **Próximo passo concreto:** publicar. `ENTREGA-WORDPRESS.md` traz o corpo, o H1, o
  title e a meta novos. Depois: imagem de abertura, imagem da tabela e sincronizar o banco.
- **Bloqueios:** nenhum bloqueio de dado. O `checkpoint_verificar.py` segue acusando 5
  ocorrências, todas de "130 leitos" — decisão editorial documentada abaixo, não erro.
- **Nota histórica:** a FASE 0 foi aberta a pedido do usuário DEPOIS da reformatação de
  layout. Ela não era pré-requisito do layout (o HTML já vinha escrito) e não é —
  mas foi ela que revelou o erro de contagem da rede, que estava no ar.

## Portões

| Portão | Status | Evidência |
|---|---|---|
| CI-1 — concorrente lido (`checkpoint_ci1.py`) | ✅ aprovado | `checkpoints/ci1.txt` — 4 concorrentes lidos por curl |
| FASE 0 (`checkpoint_fase0.py`) | ✅ aprovado | `checkpoints/fase0.txt` — 7 unidades, 21 FAQ, 8 secundárias, 16 dados nível 1-2 |
| Aprovação humana do state file | ⬜ pendente | portão do usuário |
| Suficiência (`checkpoint_suficiencia.py`) | ✅ aprovado | `checkpoints/suficiencia.txt` |
| Kit on-page (`checkpoint_onpage.py`) | ✅ aprovado | `checkpoints/onpage.txt` — com o H1/title/meta de `ENTREGA-WORDPRESS.md` |
| Preço-primeiro / lead-herói (`checkpoint_preco_primeiro.py`) | ✅ aprovado | `checkpoints/preco_primeiro.txt` — 0 avisos |
| Tamanho de parágrafo (`checkpoint_paragrafos.py`) | ✅ aprovado | `checkpoints/paragrafos.txt` — 0 reprovados, 20 no limite |
| Ritmo visual (`checkpoint_ritmo_visual.py`) | ✅ aprovado | `checkpoints/ritmo_visual.txt` — 1 seção em aviso (4 P) |
| Citabilidade (`checkpoint_citabilidade.py`) | 🟡 1 reprovação | `checkpoints/citabilidade.txt` — é a seção de FAQ; ver Decisões |
| Voz humana (`checkpoint_voz.py`) | ✅ aprovado | `checkpoints/voz.txt` — 0 🔴; 🟡 densidade de travessão (herdada) |
| Completude (`checkpoint_completude.py`) | ✅ aprovado | `checkpoints/completude.txt` — 12 H2, 14 FAQ |
| `[VERIFICAR]` / tokens proibidos (`checkpoint_verificar.py`) | 🟡 5 ocorrências | `checkpoints/verificar.txt` — só "130 leitos"; ver decisão de 01/09 |
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
- 2026-09-01 — **sumário reordenado** para bater com a nova ordem e ganhou o item
  "Faça uma Cotação" → `#cotacao-1`, que não existia. **Correção do usuário no mesmo dia:**
  eu havia feito só texto laranja; o template de `components.md` define o item como BOTÃO —
  badge `$` + fundo laranja em gradiente, texto branco, padding, radius e sombra. Corrigido. Ficou com 14 itens (13 seções + CTA);
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

### Correções aplicadas em 2026-09-01 (depois do relatório)

- **Rede: 10 → 7 unidades.** Corrigido no herói, na métrica, no H2, no subtítulo, no sumário,
  no Resumo Rápido da S1, na cobertura por bairro e na conclusão. Os cards "Diagnóstico
  Aracaju" e "Diagnóstico Gabriel Soares" saíram: duplicavam o endereço da Hapclínica e do
  hospital, e o que descreviam já está no texto das duas unidades.
- **Clínica São José (Tv. Juca Barreto, 177) incluída** como 7ª unidade. O card afirma só o
  que o catálogo traz — existe, é própria, fica no São José — e manda conferir as
  especialidades no Guia Médico.
- **H1, title e meta reescritos** (em `ENTREGA-WORDPRESS.md`): passam a conter a keyword
  principal e perdem o ano congelado. `checkpoint_onpage.py` ✅.
- **O preço no título passa a ser shortcode, não número fixo** — decisão do usuário em
  01/09. Title: `Plano Hapvida Aracaju: Rede e Preços a Partir de [aracaju_menorvalor]`
  (58 caracteres renderizados); a meta idem. Levantei que o WordPress não roda
  `do_shortcode()` no `<title>` por padrão; o usuário confirmou ter plugin que renderiza.
  Conferir o `<title>` no ar depois de publicar (comando no `ENTREGA-WORDPRESS.md` §5).
  Ganho: título e tabela nunca divergem — no reajuste, a SERP acompanha sozinha.
- **Links: 2 → 9 destinos internos**, priorizando os SUBUTILIZADOS do
  `consultar_saturacao_destinos`: teleconsulta (4 backlinks), laboratórios por capital (4),
  clínicas por capital (10), rede pediátrica (10), urgência e emergência (12), e os
  cross-links de Maceió (1) e Salvador (6). A URL de carências deixou de aparecer 2×.
- **Link externo nº 2 (ANS)** acrescentado na seção de carências. Agora são 2, o mínimo.
- **Seção "Tecnologia e Atendimento Digital" eliminada** e transformada em bridge de um
  parágrafo dentro da S7, preservando o único trecho local (o Qualivida operado na unidade
  da Gentil Tavares). É a ação que a tabela de migração da skill e o banco recomendavam.
- **2 H2 passaram a carregar keyword secundária** ("Hospital Hapvida Gabriel Soares…" e
  "…Onde Ficam as Clínicas Hapvida em Aracaju").
- **Menções à DRV: 13 → 3.** Duas das três caixas "DICA DRV" viraram callout (o conteúdo
  ficou); as menções em texto corrido saíram.
- **FAQ: 18 → 14.** Saíram 3 nacionais (Nosso Plano × Mix, mecânica da coparticipação,
  mínimo de vidas do empresarial — as duas primeiras catalogadas como overlap de risco alto)
  e a do telefone, que era tráfego de quem já é cliente e carregava 2 telefones.
- **Dado YMYL:** os 3 telefones saíram; as contagens de leitos sem fonte (56, 74, 145, 186)
  saíram. **"130 leitos" ficou** — é anúncio público datado (dez/2025), com fonte no state
  file, e é o dado prospectivo central do artigo. A repetição caiu de 10 para 5 ocorrências.
  Esta é a única razão de o `checkpoint_verificar.py` seguir vermelho.
- **Tipografia, parágrafos e ritmo** reajustados depois das edições: 3 parágrafos que
  passaram de 480 chars foram quebrados em fronteira de frase e entrou um H3
  ("Estrutura e especialidades") na seção do Gabriel Soares.

## Dados que faltam

- **Rede: o artigo afirma 10 pontos; o catálogo tem 7.** Ver item 1 do relatório.
- **IBGE não reconferido** — WebFetch devolveu HTTP 403 nesta sessão. População, IDH e PIB
  seguem os do texto publicado.
- **Beneficiários da Hapvida em SE**: não há número com fonte. Não usar a faixa "~60-84 mil"
  que está no campo `concorrentes` do banco.
- **location_code de Aracaju = 1001715** (confirmado no CSV de geotargets do Google Ads).
  A tabela da skill `dataforseo-tabelaplanos` só tem Brasil e BH — vale acrescentar.
- **Armadilha nova do DataForSeo:** o Labs (`keyword_data`, `keyword_suggestions`) rejeita
  `location_code` de cidade que a SERP aceita (erro 40501 `Invalid Field: 'location_code'`).
  Para Labs, usar 2076.
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
