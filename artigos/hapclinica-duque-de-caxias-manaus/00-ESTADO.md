# ESTADO — hapclinica-duque-de-caxias-manaus

> Este arquivo é o **ponto de salvamento** do artigo. Quem abrir uma sessão nova
> lê ele primeiro e continua daqui — sem refazer pesquisa nem readivinhar decisão.
> **Atualize ao fim de cada fase, antes de responder ao usuário.**

## Identificação

- **Slug:** hapclinica-duque-de-caxias-manaus
- **Tipo:** hospital (unidade ambulatorial — arquétipo HS1-HS4)  <!-- city | hospital | tr | pillar | cobertura -->
- **Skill em uso:** hapvida-article-builder-v7
- **Aberto em:** 2026-08-31
- **URL de destino:** https://tabelaplanos.com.br/hapclinica-duque-de-caxias-manaus/
- **Keyword principal:** hapclinica duque de caxias (6.600/mês, KD 0, navigational)

## Fase atual

- **Fase:** LINHA DA v7.2 COMPLETA — 25 agentes, 5 estágios. Artigo pronto,
  todas as travas verdes, varredura final aprovada sem avisos.
- **Próximo passo concreto:** decisão do usuário sobre 3 pendências que o
  orquestrador NÃO pode executar sozinho (ver "Pendências para o usuário").
  Depois: gerar schema (execução separada), publicar no WordPress e registrar
  no banco (Agente 18).
- **Bloqueios:** o artigo em si não tem bloqueio. O que falta é decisão e dado
  de campo.

## Portões

| Portão | Status | Evidência |
|---|---|---|
| CI-1 — concorrente lido (`checkpoint_ci1.py`) | ✅ aprovado | `checkpoints/ci1.txt` — 4 lidos por WebFetch |
| FASE 0 (`checkpoint_fase0.py`) | ✅ aprovado | `checkpoints/fase0.txt` |
| Aprovação humana do state file | ✅ aprovado | usuário, 2026-08-31 |
| Roteamento de modelos (`checkpoint_modelos.py`) | ✅ aprovado | `checkpoints/modelos.txt` — 4 modelos distintos |
| Portão de pesquisa (agentes 23 e 24) | 🟡 2 rodadas, zero 🔴 | 23: 7/6 · 24: 8/7 — teto estrutural, não defeito |
| Conferência de fatos (agente 6) | ✅ corrigido | derrubou os booleanos do CNES |
| Conferência DataForSeo (agente 7) | ✅ corrigido | 3 divergências de keyword |
| Suficiência (`checkpoint_suficiencia.py`) | ✅ aprovado | `checkpoints/suficiencia.txt` — reprovou na 1ª e passou após correção |
| Kit on-page (`checkpoint_onpage.py`) | 🟡 no Agente 14 | |
| Preço-primeiro (`checkpoint_preco_primeiro.py`) | ✅ aprovado | hospital: regra 1 dispensada |
| Voz humana (`checkpoint_voz.py`) | ✅ aprovado | 0 tique, 0 aviso de densidade |
| Parágrafos (`checkpoint_paragrafos.py`) | ✅ aprovado | 0 acima de 480 chars |
| Ritmo visual (`checkpoint_ritmo_visual.py`) | ✅ aprovado | 7 seções, 0 reprovada |
| Citabilidade (`checkpoint_citabilidade.py`) | ✅ aprovado | 5 reprovadas → 0 |
| Completude (`checkpoint_completude.py`) | ✅ aprovado | 6 H2, 12 FAQ, 2.346 palavras |
| `[VERIFICAR]` / tokens (`checkpoint_verificar.py`) | ✅ aprovado | lista de tokens corrigida antes |
| Varredura anti-doorway final (`checkpoint_doorway_final.py`) | ✅ aprovado | `checkpoints/doorway_final.txt` — 0 avisos, D1 12,1%, D4 0,0% contra os 4 irmãos |
| Painel de juízes 16a/16b/16c | ✅ 3 rodadas de correção | 16a 5,0 · 16b 4,0 · 16c 6,5 na 1ª leitura; tudo corrigido |
| Varredura humana (Agente 21) | ✅ PUBLICA COM RESSALVA | itens do artigo aplicados; itens dos irmãos pendentes |
| Registro no banco Supabase | ⬜ pendente | |

Legenda: ⬜ pendente · 🟡 rodado, com ressalva · ✅ aprovado (saída em `checkpoints/`)

## Decisões tomadas

<!-- uma linha por decisão, com data. Serve para a próxima sessão não reabrir. -->
- 2026-08-31 — pasta criada, tipo hospital (unidade).
- 2026-08-31 — **alvo trocado por decisão do usuário (Rota B)**: o pedido original era
  Duque de Caxias/RJ, mas a keyword dos 6.600/mês é da unidade de **Manaus**. Registro
  em `ACHADO-BLOQUEANTE.md`.
- 2026-08-31 — arquétipo definido: unidade HS1-HS4, e **não** artigo de cidade. A
  unidade é uma policlínica ambulatorial, não um hospital.
- 2026-08-31 — ficha CNES 9505970 obtida em fonte primária oficial
  (`apidadosabertos.saude.gov.br`). Ela prova ausência de centro cirúrgico, centro
  obstétrico, centro neonatal, atendimento hospitalar e SUS. É o eixo do artigo.
- 2026-08-31 — coparticipação de Manaus confirmada na faixa `demais_capitais`
  (consulta R$ 25,42 · exame simples R$ 45,79 · exame complexo R$ 114,48).
- 2026-08-31 — links de coparticipação (58) e carência (53) **excluídos do plano por
  saturação**; substituídos por `o-que-e-plano-ambulatorial-2` (8, normal).
- 2026-08-31 — `checkpoint_suficiencia` reprovou na 1ª rodada (FAQ sem âncora local,
  2 secundárias de intenção de quem já é cliente, ganho sem nível, diferenciais
  genéricos). Corrigido de verdade e aprovado na 2ª.
- 2026-08-31 — **os campos booleanos do CNES não provam nada** (medido em 3
  unidades, inclusive um PA 24h: todos zerados). Tese refeita sobre
  `codigo_tipo_unidade` 4 e o turno de três turnos. Seção 3.1 do state file.
- 2026-08-31 — **a lista de FORBIDDEN_TOKENS foi corrigida**: proibia as palavras
  "internação", "parto", "UTI", que são o próprio encaminhamento — o ganho do
  artigo. E "UTI" dava falso positivo casando dentro do comentário
  `/* === UTILITY CLASSES === */` do CSS padrão. Tokens passaram a nomear a
  unidade ("internação na Hapclínica").
- 2026-08-31 — o artigo NÃO leva o `<script>` aditivo [V5]: não usa componente V5,
  e carregar JS morto é perda.
- 2026-08-31 — links de coparticipação e carência seguem fora por saturação; a
  ponte de coparticipação é o pillar do plano ambulatorial.

## Dados que faltam

Quatro itens `[VERIFICAR]` que NÃO podem entrar no artigo como fato:

1. **Telefone próprio da unidade** — o 4002-3633 é a central da Hapvida (o mesmo
   número consta do artigo do Nilton Lins). A FAQ 5 se responde em negação.
2. **Coleta laboratorial própria** — o CNES registra serviço de apoio, mas não
   nomeia coleta.
3. **Linha de ônibus 542** — veio de agregador de transporte.
4. **Atendimento pelo SUS** — o campo do CNES diz NAO, mas devolve NAO para as
   três unidades testadas e não se provou discriminante.

E a precisão do horário (06:00-20:00) vem de diretório; o que a fonte primária
sustenta é o turno de manhã, tarde e noite.

Não citar, em nenhuma hipótese: lista de especialidades (os diretórios se
contradizem), ano de inauguração, nome de médico e estacionamento — todos sem fonte.

## Pendências para o usuário — NÃO executáveis pelo orquestrador

1. **O horário real da unidade.** Três versões e nenhuma primária: CNES garante
   só manhã/tarde/noite; um diretório diz 6h-20h; o **nosso hub, no ar, diz
   7h-19h**. Alguém precisa ligar na unidade. O artigo hoje não afirma hora.
2. **A coordenada.** CNES (-3.101992, -60.025113) e a página oficial da Hapvida
   (-3.119259) estão a **2,43 km**. Nenhuma pode ir para o `schema.json`.
3. **Correções em páginas NO AR** (exigem autorização expressa — regra da
   `pendencias-tabelaplanos`):
   - `clinicas-hapvida-por-capital`: criar link descendente para este artigo
     (é a condição para o spoke ter chance na keyword) e remover a lista de
     especialidades da unidade, que não tem fonte primária;
   - `plano-hapvida-manaus`: corrigir "Av. Camapuã, **8**" para **695** no PA
     Cidade Nova (é endereço de emergência, e está errado independentemente
     deste artigo); rever o horário 7h-19h e o "10+ especialidades".
4. **`[URL_DA_IMAGEM]`** — a imagem de abertura ainda não existe.
5. No registro pós-publicação, `registrar_uso_faq` para os templates 95, 64 e 11.

## Fio condutor

O roteiro do paciente da Praça 14. Esta é uma policlínica de consulta e exame com
hora marcada — registrada no CNES como tipo 4 e operando em três turnos, não em
regime contínuo como os prontos atendimentos da mesma rede (tipo 73). Quem chega
aqui com um caso que ela não resolve precisa saber para qual unidade de Manaus ir.
Toda a SERP para no endereço; este artigo é o único que orienta.

⚠️ **Não escrever a negativa categórica** ("não faz cirurgia, não interna") como
fato apurado — ver seção 3.1 do state file. Afirmar a classificação e substituir a
negativa pelo encaminhamento nominal.
