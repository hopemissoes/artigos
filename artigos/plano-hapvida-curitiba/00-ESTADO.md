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

- **Fase:** **reformatação de layout para a v7.4** (não é artigo novo — o texto chegou pronto,
  enviado pelo usuário, e foi **reordenado sem alteração de conteúdo**)
- **Próximo passo concreto:** revisão humana do HTML e, se aprovado, publicação. Depois:
  imagem de abertura, imagem da tabela e schema (execução separada, sob pedido).
- **Bloqueios:** nenhum. A trava da v7 fecha em ✅ APROVADO.

## Escopo desta sessão (o que NÃO foi feito)

Não houve FASE 0: o artigo não foi escrito aqui. Nenhuma pesquisa, nenhum dado novo,
nenhum número, nome de hospital, carência ou valor foi criado, alterado ou removido.
A sessão mexeu **só em ordem de blocos e no invólucro do lead**. Portanto os portões de
pesquisa (CI-1, FASE 0, suficiência) continuam **não aplicáveis a esta entrega** — e
continuariam pendentes se um dia este artigo for tratado como produção nova.

## Portões

| Portão | Status | Evidência |
|---|---|---|
| CI-1 — concorrente lido (`checkpoint_ci1.py`) | ⬛ n/a nesta entrega | artigo não produzido aqui |
| FASE 0 (`checkpoint_fase0.py`) | ⬛ n/a nesta entrega | idem |
| Aprovação humana do state file | ⬛ n/a nesta entrega | idem |
| Suficiência (`checkpoint_suficiencia.py`) | ⬛ n/a nesta entrega | idem |
| Kit on-page (`checkpoint_onpage.py`) | ⬜ pendente | precisa das secundárias do kit; não existem |
| **Preço-primeiro / lead-herói (`checkpoint_preco_primeiro.py`)** | ✅ **APROVADO** | `checkpoints/checkpoint_preco_primeiro.txt` |
| Voz humana (`checkpoint_voz.py`) | 🟡 reprovado **antes e depois, igual** | `checkpoints/checkpoint_voz.txt` — herdado, não introduzido |
| Completude (`checkpoint_completude.py`) | ✅ aprovado | `checkpoints/checkpoint_completude.txt` |
| Parágrafo / ritmo visual | ✅ aprovados | `checkpoints/` |
| Citabilidade (`checkpoint_citabilidade.py`) | 🟡 13 reprovadas **antes e depois, igual** | `checkpoints/checkpoint_citabilidade.txt` |
| `[VERIFICAR]` / tokens proibidos (`checkpoint_verificar.py`) | ⬜ pendente | exige state file da FASE 0 |
| Varredura anti-doorway final (`checkpoint_doorway_final.py`) | ⬜ pendente | exige lista de âncoras + artigos irmãos |
| Registro no banco Supabase | ⬜ pendente | só depois de publicado |

Legenda: ⬜ pendente · 🟡 rodado, com ressalva · ✅ aprovado · ⬛ não se aplica

## Decisões tomadas

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
