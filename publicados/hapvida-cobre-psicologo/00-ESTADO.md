# hapvida-cobre-psicologo — estado

- **Post WordPress:** 36525 · https://tabelaplanos.com.br/hapvida-cobre-psicologo/
- **Banco:** id 71, tipo `cobertura`, status `publicado`
- **Skill usada:** nenhuma builder — auditoria comparativa pontual (CI-1 rota 2, n8n)
- **Última ação:** 08/09/2026 — 17 correções aplicadas e conferidas no HTML no ar

## O que foi feito em 08/09/2026

Comparação com a concorrente `descontoplanodesaude.com.br/psicologo-hapvida/` (Jocross,
autor João Pinheiro), lida inteira via workflow n8n `NUUZmP5y4AtFb2jL` — `curl` e
`WebFetch` estão bloqueados nesta sessão (ver `docs/CI1-SEM-EGRESS.md`, rota 2).

Relatório completo: `auditoria-comparativa-2026-09-08.html`
Artefato publicado: https://claude.ai/code/artifact/d9f6818d-00d9-40a2-be33-2b6a646e0d7a

### 17 edições gravadas (uma a uma, com dry-run antes de cada)

| # | Edição | Ferramenta |
|---|---|---|
| 1 | meta description: `R$ 23` fixo → `[demais_capitais_demais_terapias]` + `[ano_atual]` | `editar_meta_description` |
| 2-3 | `[..._terapias_neurológicas]` → `[..._terapias_neurologicas]` (o acento quebrava o shortcode) | `substituir_no_artigo` |
| 4 | remove 2× `<div…>[elementor-templaté id=”11215″]</div>` (duplicata quebrada) | `substituir_no_artigo` |
| 5 | link 404 `/plano-de-saúde-hapvida-salvador/` → `/plano-hapvida-salvador2/` | `substituir_no_artigo` |
| 6-10 | 5 links que passavam por 301 → destino final (recife, fortaleza, belo-horizonte, sao-paulo2, hapvida-vs-unimed) | `substituir_no_artigo` |
| 11-17 | 7 correções de texto: principais · existe · necessária · etárias · Peça · "é obrigatória e ilimitada" · diagnosticará | `substituir_no_artigo` |

### Conferido no ar depois de gravar

- meta renderiza `a partir de R$ 24,27 por sessão … em 2026` — **o shortcode funciona no campo do Rank Math**
- zero shortcode cru na página; `R$ 78,87` renderiza na tabela de terapia neurológica
- os 6 destinos finais presentes; nenhum resto de slug antigo nem do 404
- as 7 palavras erradas sumiram

## Fatos conferidos (não deduzir de novo)

- **RN 541/2022** confirmada: publicada 11/07/2022, vigor 01/08/2022, revogou as DUTs que
  limitavam sessões de psicólogo/fono/TO/fisio. Os dois artigos citam certo.
- **Encaminhamento médico:** a ANS exige cobertura "conforme prescrição do profissional
  médico assistente". Nosso artigo está certo; a concorrente afirma "acesso direto sem
  pedido médico" **e se contradiz no próprio FAQ**.
- **Coparticipação canônica** (`consultar_coparticipacao`, demais_capitais):
  `demais` = R$ 24,27 · `terapia_neuro` = R$ 78,87
- **Nome certo dos shortcodes de coparticipação:** sem acento. Conferido no corpo do
  pillar `tabela-precos-hapvida-coparticipacao-guia-completo` (post 22798), onde renderizam.
- **Schema da concorrente:** as 6 páginas da nota 14 têm o MESMO bloco automático
  (WebSite, WebPage, BlogPosting, Person "João Pinheiro", ImageObject).
  **Nenhuma delas tem FAQPage.**

## Próximo passo

1. **Schema desta página** — hoje o HTML no ar não tem nenhum JSON-LD.
   Publicar Article + FAQPage (as 19 perguntas já estão na página) + Person da DRV.
2. Imagem no corpo (tabela de coparticipação de psicologia), com alt e legenda — hoje 0 `<img>`.
3. `registrar_atualizacao` e `registrar_links_artigo` no banco — **não feito, falta autorização**.

## Achados vizinhos (não tratados)

- `/rede-psiquiatrica-hapvida/` responde **301 apontando para ela mesma** (x-redirect-by: Rank Math) — laço, a página não abre.
- `/cobertura-psicologia-hapvida/` devolve **404**, mas o banco (id 86) marca como `publicado`.
- O banco registra o id 71 na URL `/cobertura/hapvida-cobre-psicologo/`, que hoje é só um 301 para a URL real.

---

## Reformatação para o layout v7 — 08/09/2026 (PRONTA, NÃO PUBLICADA)

Arquivo: `artigos/hapvida-cobre-psicologo/artigo.html` (gerado por `montar-v7.py`,
que fatia o HTML publicado e remonta — **não reescreve prosa**).

### Ressalva de arquétipo (registrar, não repetir a dúvida)

Este artigo é `cobertura`. A v7 tem quatro arquétipos — cidade, hospital, TR e
pillar — e o `artigo-pillar-produto.md` diz na linha 18: *"Não use aqui: … ou de
cobertura (skill `hapvida-coverage-builder`)"*. Essa skill **não está disponível**
nesta conta. Aplicamos a **camada de layout** da v7 (ordem preço-primeiro,
lead-herói v7.4, componentes v7.6), sem forçar a estrutura P1-P9.

Consequência mecânica: `checkpoint_preco_primeiro.py` em modo `pillar` **reprova**,
porque procura shortcode de tabela de cidade (`[cidade_menortabela]`,
`[cidade_emp_...]`) e este artigo tem uma `<table>` real de coparticipação. Em modo
`hospital` — o que dispensa a regra 1 para artigo sem tabela de preço — **aprova**.

### O que mudou

| | antes | depois |
|---|---|---|
| palavras | 4.623 | 4.834 |
| H2 / H3 / FAQ / formulários | 13 / 15 / 20 / 3 | 13 / 15 / 20 / 3 |
| lead-herói (v7.4) | 0 | 1 |
| selos v5-trust | 0 | 1 |
| faixa `fonte-oficial` (v7.6) | 0 | 2 |
| caixa `guia-box` (v7.6) | 0 | 1 |
| quadro comparativo (v7.6) | 0 | 1 |

Nova ordem: **lead-herói → H2 de preço + tabela (`id="precos"`) → formulário
`cotacao-1` → sumário → análise de preço + selos → demais seções na ordem antiga**.
Medido: 927 caracteres antes da tabela (teto 1.800) e 44 entre tabela e sumário
(teto 600).

### Edições de texto (nenhum fato tocado)

- 4 parágrafos acima de 480 caracteres quebrados em dois, no fim de frase
- H3 "Qualidade de Vida e Autoconhecimento" → "Burnout, Luto e Transições de
  Carreira" (o `checkpoint_voz.py --rigor alto` marcava "qualidade de vida" como
  marketing genérico); badge QV → BL
- abertura citável de 46 palavras na seção de FAQ (o `checkpoint_citabilidade.py`
  reprovava a seção por não ter `<p>` de corpo após o H2)
- 2º parágrafo do lead realocado para a seção da ANS
- 3º parágrafo do lead ("Neste guia completo, você vai entender…") removido: é o
  molde que a `voz-humana.md` lista como tique, e o único dado dele (coparticipação
  a partir de X) está no herói e na seção de preço

### Checkpoints (saídas coladas na conversa de 08/09/2026)

| checkpoint | resultado |
|---|---|
| `checkpoint_preco_primeiro.py … hospital` | ✅ APROVADO |
| `checkpoint_preco_primeiro.py … pillar` | ❌ 1 erro — sem shortcode de tabela de cidade (ver ressalva) |
| `checkpoint_completude.py … pillar` | ✅ APROVADO (8/8 itens) |
| `checkpoint_paragrafos.py` | ✅ APROVADO |
| `checkpoint_ritmo_visual.py` | ✅ APROVADO |
| `checkpoint_citabilidade.py` | ✅ APROVADO |
| `checkpoint_voz.py` (rigor padrão) | ✅ APROVADO |
| `checkpoint_voz.py --rigor alto` | ❌ 62 travessões (13,7/1.000 palavras, alvo ≤2) |

**Decisão sobre o 🟡 do rigor alto:** os 62 travessões ficam. Tirá-los é reescrever
o texto inteiro, não reformatar; e `--rigor alto` é a régua de pillar, não de
cobertura. Anotado como pendência de reescrita, não de layout.

### Próximo passo

Publicar exige `editar_conteudo_artigo`, que **sobrescreve o corpo inteiro** —
a operação mais perigosa do conector. Rodar antes com `apply: false` e conferir
`tamanhoAntes -> tamanhoDepois`: tem de bater com **116.672** caracteres. Número
diferente = truncamento; não gravar.
