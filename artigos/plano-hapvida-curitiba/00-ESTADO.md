# ESTADO — plano-hapvida-curitiba

> Ponto de salvamento do artigo. Quem abrir sessão nova lê isto primeiro.

## Identificação

- **Slug:** plano-hapvida-curitiba
- **Tipo:** city (S1-S7 — ver ressalva "11 seções" abaixo)
- **Skill em uso:** hapvida-article-builder-v7
- **Aberto em:** 2026-09-01
- **URL de destino:** https://tabelaplanos.com.br/plano-hapvida-curitiba/ (ainda **não publicado** —
  `listar_artigos` não retorna esse slug; o que existe é `/plano-clinipam-curitiba/`, id 32466)
- **Keyword principal:** plano Hapvida Curitiba

## Fase atual

- **Fase:** **FASE 0 concluída (DR1 + DR2)** — rodada em 2026-09-01 a pedido do usuário, sobre
  um artigo **já publicado**. Antes dela, a reformatação de layout para a v7.4 (também concluída).
- **Próximo passo concreto:** publicar. Colar `TITULO-META.md` no Rank Math, colar o
  `artigo.html` e atualizar o `dateModified` (revisão real, regra 5c). Depois: imagem de
  abertura, imagem da tabela, schema e o registro no banco.
- **Bloqueios:** nenhum mecânico. `checkpoint_ci1` e `checkpoint_fase0` fecham em ✅ APROVADO.
- **Ressalva de método:** ⚠️ **MODO agente único** — a linha de 25 agentes da v7.2 NÃO rodou
  (subagentes não autorizados nesta sessão). Coleta, síntese e conferência saíram da mesma
  cabeça, então a trava "quem produz nunca confere" não existe aqui e o portão humano vale mais.
  `checkpoint_suficiencia.py` e os juízes de pesquisa (Agentes 23/24) seguem pendentes.

## Escopo desta sessão (o que NÃO foi feito)

Não houve FASE 0: o artigo não foi escrito aqui. Nenhuma pesquisa, nenhum dado novo,
nenhum número, nome de hospital, carência ou valor foi criado, alterado ou removido.
A sessão mexeu **só em ordem de blocos e no invólucro do lead**. Portanto os portões de
pesquisa (CI-1, FASE 0, suficiência) continuam **não aplicáveis a esta entrega** — e
continuariam pendentes se um dia este artigo for tratado como produção nova.

## Portões

| Portão | Status | Evidência |
|---|---|---|
| **CI-1 — concorrente lido (`checkpoint_ci1.py`)** | ✅ **APROVADO** — 4 lidos | `checkpoints/checkpoint_ci1.txt` |
| **FASE 0 (`checkpoint_fase0.py`)** | ✅ **APROVADO** | `checkpoints/checkpoint_fase0.txt` |
| **Aprovação humana do state file** | ✅ aprovado pelo usuário em 2026-09-01 | — |
| **Kit on-page (`checkpoint_onpage.py`)** | ✅ **APROVADO** | `checkpoints/checkpoint_onpage.txt` |
| **`[VERIFICAR]` / tokens proibidos (`checkpoint_verificar.py`)** | ✅ **APROVADO** | `checkpoints/checkpoint_verificar.txt` |
| **Citabilidade (`checkpoint_citabilidade.py`)** | ✅ **APROVADO** — 0 reprovadas (eram 13) | `checkpoints/checkpoint_citabilidade.txt` |
| Suficiência (`checkpoint_suficiencia.py`) + juízes 23/24 | ⬜ pendente | exige arquivo de âncoras |
| **Preço-primeiro / lead-herói (`checkpoint_preco_primeiro.py`)** | ✅ **APROVADO** | `checkpoints/checkpoint_preco_primeiro.txt` |
| Voz humana (`checkpoint_voz.py`) | 🟡 **reprova por NOME PRÓPRIO — decisão registrada** | `checkpoints/checkpoint_voz.txt` |
| Completude (`checkpoint_completude.py`) | ✅ aprovado | `checkpoints/checkpoint_completude.txt` |
| Parágrafo / ritmo visual | ✅ aprovados (0 reprovados; eram 5 e 2 depois que a trava passou a enxergar o corpo) | `checkpoints/` |
| Varredura anti-doorway final (`checkpoint_doorway_final.py`) | ⬜ pendente | exige lista de âncoras + artigos irmãos |
| Registro no banco Supabase | ⬜ pendente | só depois de publicado |

Legenda: ⬜ pendente · 🟡 rodado, com ressalva · ✅ aprovado · ⬛ não se aplica

## Achados da FASE 0 (2026-09-01) — ordenados por impacto

1. 🔴 **CTR quebrado.** 151 impressões/28d em "hapvida curitiba" na posição 6,28 → **1 clique**
   (CTR 0,66%; a posição comportaria 5-8%). É o maior retorno disponível e se resolve em
   title + meta, não em conteúdo.
2. 🔴 **Canibalização em 9 URLs.** Para "hapvida curitiba", nove páginas nossas recebem
   impressão. `/plano-clinipam-curitiba/` aparece em **posição 1,0** enquanto a página de
   cidade fica em 6,28. Na SERP real de "plano hapvida curitiba", quem aparece é a **home**
   (absoluto 20) — a página de cidade não aparece no orgânico.
3. 🔴 **A keyword-alvo tem volume zero.** "plano hapvida curitiba" → `items_count: 0`.
   "hapvida curitiba" → 1.000/mês, mas navegacional (8 dos 18 orgânicos são da própria Hapvida)
   e caindo 28% ao ano. A demanda capturável é a cauda longa do GSC.
4. 🟢 **A brecha, e ela é grande:** nenhum dos 4 concorrentes lidos publica o endereço de uma
   única unidade. Nós temos as **14** no catálogo do banco. E o GSC mostra gente buscando por
   **nome de rua** (Nossa Senhora da Luz 30 impressões, Monsenhor Celso 16, São Lourenço 6) —
   as três são endereços de unidades nossas.
5. 🟢 **RMC ignorada.** ~37 impressões/28d vêm de Campo Largo, Quatro Barras, Pinhais,
   Almirante Tamandaré, Fazenda Rio Grande, São José dos Pinhais e Araucária. O artigo não
   nomeia nenhuma. E 2 das 14 unidades ficam **fora** do município (Colombo e Pinhais).
6. 🟡 **Pronto atendimento subaproveitado.** "pronto atendimento hapvida curitiba" está em
   posição **2,29** com 21 impressões e zero clique. O artigo não tem bloco de PA 24h.
7. 🔴 **Dois números do artigo não têm fonte:** "19+ centros clínicos" (o catálogo tem 11
   unidades não-hospitalares) e o nome "Hospital Ônix Mateus Leme" (o catálogo tem **dois**
   hospitais distintos: Mateus Leme/São Francisco e Onix Batel/Seminário). Ambos em
   FORBIDDEN_TOKENS até serem batidos no Guia Médico.
8. 🟡 **Links saturados.** O artigo aponta para 4 destinos SATURADOS (carência 53 backlinks,
   tabela-de-preço 44, Qualivida 17 — este 3× no mesmo artigo, empresarial 17) e para
   `/coparticipacao-hapvida/`, que **redireciona** para o destino mais saturado do site (58).
   Destinos subutilizados e relevantes ignorados: `/plano-hapvida-sao-jose-dos-pinhais/` (4),
   `/plano-hapvida-londrina/` (5), `/urgencia-e-emergencia-hapvida/` (12).
9. 🟡 **Curitiba não está na fila do cotador** — sem dado de nível 2 de cotação nesta praça.
10. ✅ **Confere:** a população "1,83 milhão (IBGE 2025)" bate com a estimativa IBGE de 2025
    (1.830.795), e Curitiba é mesmo do grupo `demais_capitais` da coparticipação.

## Decisões tomadas

- 2026-09-01 — **FASE 0 rodada e aprovada nas duas travas.** `location_code` de Curitiba
  descoberto e confirmado em duas versões do CSV de geotargets: **1001634** (não estava na
  tabela da skill `dataforseo-tabelaplanos` — vale acrescentar lá).
- 2026-09-01 — pasta criada; original preservado em `artigo-ORIGINAL.html`, reformatado em `artigo.html`.
- 2026-09-01 — **lead virou LEAD-HERÓI (v7.4).** A faixa navy é o 1º elemento do `<article>`;
  dentro dela, o `<p>` citável de 52 palavras, montado **só** com fatos que já estavam no lead
  e no grid de métricas da S1 (rede própria Clinipam/1983, 3 hospitais, 19+ centros clínicos,
  única maternidade de operadora, Tabela 1). Sem CTA e sem autorreferência, como a v7.4 exige.
- 2026-09-01 — **os parágrafos 2 e 3 do lead antigo desceram para dentro da S1**, íntegros
  (IBGE, 50,4% de cobertura, PIB per capita, IDH). Nada de lead foi descartado, exceto o
  parágrafo 1, que **virou** o herói — é a transformação que a v7.4 descreve, não um corte.
- 2026-09-01 — **grifo animado:** o herói não aceita `destaque-laranja-suave` (laranja a 22%
  some sobre navy). O grifo que saiu do lead foi compensado no corpo, na S1 ("50,4% da
  população possui convênio médico"). Total permanece **6**, igual ao original.
- 2026-09-01 — **S2 partida em duas `<section>`**, como manda a v7.1: `S2↑a` (H2 de preço +
  contexto + tabela, com `id="precos"`) e `S2↑b` (análise, box Importante, comparativo regional).
  Mesma S2 para numeração/banco/schema; **não renumerar**.
- 2026-09-01 — **sumário colado na tabela** (37 caracteres de texto entre as duas; limite 600)
  e reordenado para a ordem nova. Ganhou o item obrigatório **"Faça uma Cotação" → `#cotacao-1`**,
  que não existia. O 1º formulário ganhou `id="cotacao-1"`, que também não existia.
- 2026-09-01 — **coparticipação continua H2 próprio, movida para logo depois da S2↑b.** O
  checkpoint classifica esse H2 como "de preço" (coparticipação em valor), e a Regra 2 manda
  agrupar todos os H2 de preço no topo. Alternativa seria rebaixá-la a H3 dentro da S2↑b —
  **não feito de propósito**: cortaria conteúdo, e a v7 é reordenação, não emagrecimento.
- 2026-09-01 — **aviso 🟡 do checkpoint, decisão registrada:** ele acusa "H2 de preço fora do
  bloco do topo" na **conclusão** ("Hapvida Curitiba: Rede Própria, Preço Competitivo…"). É
  falso positivo do vocabulário (a palavra "preço" no título da conclusão). **Fica como está.**
- 2026-09-01 — **`<style>` ganhou uma linha anti-wpautop** para o componente novo:
  `.v5-hero-metricas>p,.v5-hero-metricas>br{display:none!important}`. Não se tocou no `<script>`.
- 2026-09-01 — **shortcodes corrigidos, com o nome confirmado pelo usuário:** a tabela passou de
  `[curitiba_empresarial_total]` (nome inexistente na `shortcodes.md`) para **`[curitiba_menortabela]`**,
  o utilitário documentado. Os 6 usos **inline** que estavam com shortcode de tabela inteira dentro
  de célula e de resposta de FAQ passaram para o chamariz **`[cidade_menorvalor]`**, por cidade:
  `[curitiba_menorvalor]` (3×), `[belo-horizonte_menorvalor]` (2×), `[recife_menorvalor]` (1×).
  É o mesmo shortcode que o `/plano-clinipam-curitiba/` publicado já usa.
- 2026-09-01 — **`[sao-paulo_pme_enfermariatotal]` (2×) ficou como estava.** Não entrou na pergunta
  ao usuário e é outro produto (enfermaria, não ambulatorial): trocar mudaria o que a linha de
  São Paulo compara. Fica como pendência 2 abaixo.

## Dados que faltam / pendências herdadas (NÃO são efeito da reformatação)

1. 🟡 **Conferir no WordPress se `[curitiba_menortabela]` está cadastrado** e renderiza a tabela
   das 10 faixas. É o nome documentado e o indicado pelo usuário, mas nenhum artigo publicado do
   site o usa hoje — vale abrir a prévia antes de publicar.
2. 🟡 **`[sao-paulo_pme_enfermariatotal]` (2×) segue sendo shortcode de produto diferente** usado
   inline no comparativo e na FAQ. Se a intenção da linha de SP for o mesmo "a partir de" das
   outras, vira `[sao-paulo_menorvalor]`; se for enfermaria de propósito, fica.
3. 🟡 **O artigo usa dois shortcodes para o mesmo número:** `[curitiba_menorvalor]` (3×) e
   `[curitiba_emp_ambulatorialtotal_0]` (5×, incluindo as 2 do herói). Ambos válidos e devem dar
   o mesmo valor; uniformizar é cosmético.
4. 🟡 **Sem `<figure>` de abertura.** City é obrigado a ter uma; o artigo não tem nenhuma imagem.
   Na v7.4 ela entraria na S1, depois do parágrafo de abertura. Falta a URL (o usuário fornece).
5. 🟡 **Sem imagem da tabela** (`gerar_imagem_artigo.py`) no fim da S2↑b.
6. 🟡 **Grifos animados: 6; o mínimo da skill é 10.** Herdado do original.
7. 🟡 **11 seções numeradas + 13 itens de sumário** — a arquitetura city é S1-S7 e o sumário
   pede 10-11 itens. Herdado; reordenar não conserta. Consolidar exigiria fundir seções
   (Tecnologia é "ELIMINADA" no modelo S1-S7), o que é reescrita, não reformatação.
8. 🟡 **`/programa-qualivida-hapvida/` linkado 3×** — a regra é cada URL no máximo 1×. Herdado.
9. 🟡 **Link para a home perdido.** Ele vivia no parágrafo 1 do lead, que virou o herói; a v7.4
   proíbe CTA/autorreferência ali. Restam 8 URLs internas distintas (mínimo é 5).
10. 🟡 **Voz e citabilidade reprovam — igual antes e depois.** Todas as 13 seções abrem com o
   `<p>` de subtítulo (15px) em vez da resposta citável de 40-60 palavras. É padrão do artigo
   original, não da reformatação.

## Fio condutor

Curitiba é a praça onde a Hapvida **não** chegou comprando rede credenciada: ela herdou, via
Clinipam (1983), uma rede 100% própria com 40+ anos — 3 hospitais 24h, 19+ centros clínicos e a
única maternidade de operadora da cidade — e ainda pratica a Tabela 1 de coparticipação, a de
menores valores do país. É esse cruzamento (rede própria antiga + tabela mais barata) que
nenhum concorrente local reúne.


---

## Otimizações aplicadas em 2026-09-01 (achados 1 a 10)

- **Título, meta e H1 reescritos** (achados 1 e 3) → entregues em `TITULO-META.md`, para colar
  no Rank Math. A principal passou a ser **"hapvida curitiba"** (1.000/mês) no lugar de
  "plano hapvida curitiba" (volume ZERO), e a parte variável virou o ganho de informação:
  as 19 unidades com endereço. `checkpoint_onpage` ✅.
- **As 3 unidades do catálogo que faltavam entraram** (achado 4): Clínica São Lourenço,
  Clínica Barão do Serro Azul e Centro Clínico Colombo, cada uma com endereço, em cards.
  São Lourenço já ranqueava em 4,67 num artigo que não a citava.
- **Bloco novo de pronto atendimento** (achado 6), nomeando as 3 unidades de PA com endereço
  e separando PA de pronto-socorro hospitalar. A busca está em posição 2,29.
- **A tabela da RMC parou de mandar Colombo à capital** (achado 5): existe Centro Clínico
  Colombo na própria cidade. Entraram também os links para São José dos Pinhais e Londrina.
- **Links consertados** (achado 8): `/coparticipacao-hapvida/` era um 301 e virou a URL
  direta; Qualivida caiu de 3× para 1×; 11 links internos, **nenhuma URL repetida**.
- **Dado YMYL sem fonte removido** (achado 7): contagem de leitos e salas cirúrgicas, dois
  telefones 0800, o superlativo "única maternidade de operadora" e os números da Unimed
  (4.700 médicos / 54 hospitais) vindos de concorrente. `checkpoint_verificar` ✅.
- **Corpo do texto de 17px para 18px** — o artigo estava fora da especificação da skill
  ("Body text #4a5568, font-size: 18px"). Foi um conserto de CSS com efeito grande: as travas
  de citabilidade, parágrafo e ritmo **não enxergavam o corpo do artigo**. Citabilidade saiu
  de 13 reprovadas para 0; parágrafo e ritmo revelaram 5 parágrafos longos e 2 sequências sem
  quebra, todos corrigidos.
- **Passagem citável na FAQ** (54 palavras), que abria direto no acordeão.

## Decisões registradas sobre avisos que NÃO bloqueiam

- **`checkpoint_voz` segue REPROVADO por 4 ocorrências de "qualidade de vida"** — e as quatro
  são o **nome próprio da unidade** "Centro de Qualidade de Vida (Rua XV de Novembro, 556)".
  Renomear seria adulterar fato, o que a regra-mãe da camada de voz proíbe: *"se limpar o
  tique custar precisão, o tique fica e o editor anota o porquê"*. **Fica.** As outras duas
  famílias de tique (uso genérico de "qualidade de vida" e "cobertura total", que contraria a
  ANS) foram corrigidas — esta última virou "atendimento eletivo completo", que é mais preciso.
- **Travessão em 25 ocorrências (alvo ≤ 2 por 1.000 palavras)** — 🟡 de densidade. Em pt-BR o
  travessão é pontuação padrão de aposto; forçar o alvo deixaria o texto artificial. Reduzi os
  que eu mesmo introduzi e mantive os do texto original.
- **Aviso do `checkpoint_preco_primeiro`: "H2 de preço fora do bloco do topo"** — é a
  **conclusão**, que tem a palavra "preço" no título. Falso positivo do vocabulário. Fica.

## Correções ao que eu havia afirmado na FASE 0

Duas coisas que apontei como erro do artigo **não eram erro**, e conferi antes de editar:

1. **"Hospital Ônix Mateus Leme" não é fusão de dois hospitais.** O artigo tem os três cards
   separados, com os endereços exatos do catálogo. "Ônix" é prefixo de marca usado nos dois
   (Ônix Mateus Leme e Ônix Batel), e o GSC confirma a busca real por "hospital onix mateus
   leme" na posição 2,43. **Mantido.**
2. **"19+ centros clínicos" não estava refutado.** O catálogo tem 14 unidades, mas o artigo
   nomeia ~16 com endereço e CEP, e a regra da skill é que ausência no banco não prova ausência
   na rede. Com as 3 unidades do catálogo que faltavam, o artigo passou a nomear **19 unidades
   com endereço** — o número virou literalmente contável no próprio texto.

Os dois saíram do `FORBIDDEN_TOKENS` na prática (não aparecem mais como afirmação sem fonte);
o bloco no state file foi mantido como registro do que se investigou.

---

## Varredura anti-doorway contra os artigos irmãos (2026-09-01)

Rodada porque o usuário perguntou se este artigo é doorway do `/plano-clinipam-curitiba/`.
Trava: `checkpoint_doorway_final.py` com 53 âncoras locais (`ancoras.txt`) e 3 irmãos.

| Irmão | sobreposição de shingles | maior trecho idêntico |
|---|---|---|
| plano-clinipam-curitiba | **0,1%** | 10 palavras |
| plano-hapvida-londrina | 0,0% | 0 palavras |
| plano-hapvida-fortaleza | 0,0% | 8 palavras |

Limiares da skill: 🟡 a partir de 8%, 🔴 a partir de 15% (ou trecho literal ≥ 40 palavras).
**Nenhum chega perto.** D2 (seção sem âncora local) e D3 (clichê de operadora): zero.
D5 (title e meta no teste de substituição): passa. Veredito do script: ✅ APROVADO.

`consultar_overlaps_doorway`: os 13 overlaps catalogados no banco **não envolvem** nenhum dos
dois artigos de Curitiba. FAQ: 20 no de Curitiba, 13 no do Clinipam, **0 idênticas**.

### O que a trava NÃO pega, e que existe

1. **Sobreposição de tema, não de texto.** Três H2 tratam do mesmo assunto nos dois artigos:
   "Rede Própria em Curitiba" (os dois têm), "Como Contratar" e a FAQ. E ~4 FAQs são a mesma
   pergunta com outras palavras — "Curitiba tem pronto-socorro Hapvida?" × "Curitiba tem pronto
   atendimento Clinipam 24h?"; "Atende em São José dos Pinhais, Araucária e Colombo?" ×
   "O Hapvida Clinipam atende em São José dos Pinhais e região metropolitana?". Texto diferente,
   intenção igual. Isso é **canibalização** (achado 2), não doorway — e resolve-se dividindo
   território, não reescrevendo.
2. **🟡 D1: 31,3% do texto em parágrafos sem âncora local** (alerta a partir de 30%, reprova a
   partir de 45%). São os parágrafos de conteúdo nacional: mecânica de coparticipação,
   modalidades de plano, "a rede própria garante prontuário eletrônico integrado", benefícios
   digitais. **Esse é o doorway real do artigo — e não é contra o Clinipam, é contra as outras
   cidades.** O banco já cataloga esse padrão exato como risco ALTO para BH, São Paulo,
   Fortaleza e Londrina, nas mesmas quatro seções que Curitiba também tem: Coparticipação,
   Carências, Tipos de Planos e Tecnologia. Curitiba ainda não está catalogada, mas tem a
   mesma estrutura.
