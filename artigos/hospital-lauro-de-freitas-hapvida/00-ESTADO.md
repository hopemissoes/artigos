# ESTADO — hospital-lauro-de-freitas-hapvida

> Este arquivo é o **ponto de salvamento** do artigo. Quem abrir uma sessão nova
> lê ele primeiro e continua daqui — sem refazer pesquisa nem readivinhar decisão.
> **Atualize ao fim de cada fase, antes de responder ao usuário.**

## Identificação

- **Slug:** hospital-lauro-de-freitas-hapvida
- **Tipo:** hospital (HS1-HS4)
- **Skill em uso:** hapvida-article-builder-v7 (MODO: monomodelo, declarado)
- **Aberto em:** 2026-08-31
- **URL de destino:** https://tabelaplanos.com.br/hospital-lauro-de-freitas-hapvida/
- **Keyword principal:** hospital lauro de freitas hapvida — 2.900/mês, KD 0, competição LOW
- **Hub (artigo de cidade):** plano-hapvida-salvador2

## Fase atual

- **Fase:** FASE 0 concluída — **aguardando o portão humano**
- **Próximo passo concreto:** usuário aprovar (ou corrigir) o state file. Só depois começa o HTML — entrega única, HS1-HS4.
- **Bloqueios:** nenhum técnico. Falta apenas a aprovação humana.

## Portões

| Portão | Status | Evidência |
|---|---|---|
| CI-1 — concorrente lido (`checkpoint_ci1.py`) | ✅ aprovado | `checkpoints/ci1.txt` — 5 concorrentes lidos por curl (HTTP 200) |
| FASE 0 (`checkpoint_fase0.py`) | ✅ aprovado | `checkpoints/fase0.txt` — 1 aviso ([VERIFICAR] fora do artigo) |
| Suficiência (`checkpoint_suficiencia.py`) | ✅ aprovado | `checkpoints/suficiencia.txt` — ganho em defensibilidade 1 |
| Aprovação humana do state file | ⬜ pendente | |
| Kit on-page (`checkpoint_onpage.py`) | ⬜ pendente | |
| Preço-primeiro / lead-herói (`checkpoint_preco_primeiro.py`) | ⬜ pendente | modo `hospital` — só confere H2 de preço órfão |
| Parágrafos / ritmo / citabilidade | ⬜ pendente | |
| Voz humana (`checkpoint_voz.py`) | ⬜ pendente | |
| Completude (`checkpoint_completude.py`) | ⬜ pendente | |
| `[VERIFICAR]` / tokens proibidos (`checkpoint_verificar.py`) | ⬜ pendente | 11 tokens armados na seção 9 |
| Varredura anti-doorway final (`checkpoint_doorway_final.py`) | ⬜ pendente | comparar contra `plano-hapvida-salvador2` |
| Registro no banco Supabase | ⬜ pendente | |

Legenda: ⬜ pendente · 🟡 rodado, com ressalva · ✅ aprovado (saída em `checkpoints/`)

## Decisões tomadas

- 2026-08-31 — pasta criada, tipo hospital. Skill escolhida pelo `docs/ROTEAMENTO.md`: artigo de hospital → `hapvida-article-builder-v7`.
- 2026-08-31 — `location_code` de Lauro de Freitas descoberto e confirmado no CSV de geotargets do Google Ads (2026-08-12): **1031776**. Salvador é 1001533. Registrar na tabela da skill `dataforseo-tabelaplanos`.
- 2026-08-31 — Labs do DataForSeo (`related_keywords`) **não aceita código de cidade**: usar 2076. Só `serp_local` aceita o código municipal.
- 2026-08-31 — **MODO monomodelo declarado.** A linha de 25 agentes da v7.2 não foi disparada: este ambiente proíbe abrir subagentes sem pedido explícito do usuário. Consequência assumida no state file, seção 10.
- 2026-08-31 — **O ganho de informação foi trocado.** A primeira versão elegeu a divergência de endereço (CNES × Guia Médico) como eixo; o `checkpoint_suficiencia.py` reprovou por defensibilidade 4. Eixo novo: **única porta hospitalar própria do corredor Estrada do Coco**, apoiado no catálogo `consultar_rede` (nível 1). A divergência de endereço virou achado de apoio da HS3.
- 2026-08-31 — **Nenhum número de leito/UTI e nenhum telefone entram no artigo.** O `checkpoint_verificar.py` reprova esses padrões mecanicamente, o que contradiz o card da HS3 descrito em `references/artigo-hospital.md`. A trava mecânica vence. Registrado em `docs/DECISOES.md`.
- 2026-08-31 — Linkagem definida contra `consultar_saturacao_destinos`: coparticipação (58) e carências (53) estão SATURADOS e **não serão linkados**, apesar de `artigo-hospital.md` sugerir. Destinos escolhidos: `plano-hapvida-salvador2` (5), `urgencia-e-emergencia-hapvida` (11), `hapvida-rede-pediatrica` (9), `clinicas-hapvida-por-capital` (9).

## Dados que faltam

Detalhe e onde foi procurado: seção 8 do state file.

- leitos e leitos de UTI — sub-módulo do CNES não renderiza por curl. **Não entram no artigo de todo modo** (trava).
- acreditação ONA, especialidades do corpo clínico, responsável técnico, horário por setor — campos existem no Guia Médico oficial e estão **vazios**.
- existência de maternidade / UTI neonatal — nenhuma fonte primária afirma nem nega. O artigo não afirma nem nega; encaminha a pergunta de parto para a rede de Salvador.
- estacionamento e linhas de ônibus — sem fonte primária.

## Pendências a propor ao usuário (não gravadas no banco)

1. **Catálogo incompleto:** `consultar_rede` não tem a *Clínica Lauro de Freitas II* nem a *Unidade de Autorização Lauro de Freitas*, que existem no Guia Médico oficial. Sugerir `adicionar_unidade_rede`.
2. **Possível erro no artigo de Salvador:** a S4 afirma "20 leitos de internação adulto, 10 leitos de UTI" sem fonte declarada. Nenhuma fonte primária confirma. Sugerir revisão.
3. **Pauta candidata:** `urgência e emergência hapvida salvador` — existe spoke para Recife, Fortaleza e Goiânia, não para Salvador.
4. Registrar **1031776** na tabela de `location_code` da skill `dataforseo-tabelaplanos`.

## Fio condutor

**O Hospital Lauro de Freitas é a porta 24h do corredor da Estrada do Coco — e a porta mais fácil de errar da rede Hapvida na Bahia.** Do km 2 ao litoral norte, só Camaçari tem outro hospital próprio: quando o caso passa de consulta, ou é aqui, ou é descer para Itaigara. E três unidades da operadora dividem o mesmo nome de cidade em dois números de uma via que tem três nomes — até o AI Overview do Google erra o endereço. O artigo existe para levar a pessoa à porta certa, na hora certa, e só depois falar de plano.
