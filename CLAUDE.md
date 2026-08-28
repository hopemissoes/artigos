# CLAUDE.md — repositório de artigos (hopemissoes/artigos)

Leia este arquivo inteiro antes de qualquer coisa. Ele existe porque, em sessões
anteriores, o trabalho foi feito no repositório errado e sem a skill certa.

---

## 1. O que é este repositório

É a **mesa de trabalho e o arquivo** da produção de artigos. Ele guarda:

- o **estado** de cada artigo em produção (`artigos/<slug>/00-ESTADO.md`);
- os **artefatos** de cada artigo (pesquisa, blocos HTML, schema, checkpoints);
- o **roteamento** — qual skill usar para cada pedido (`docs/ROTEAMENTO.md`);
- o **registro de decisões e erros** (`docs/DECISOES.md`).

**O que ele NÃO é:**

- ❌ Não é onde moram as skills. As skills são pessoais e já vêm carregadas em
  toda sessão (ver `docs/AMBIENTE.md`). **Nunca copie skill para cá.**
- ❌ Não é o banco de dados. A verdade sobre artigos publicados, hospitais,
  links, FAQs e pendências está no **Supabase**, via conectores MCP `BD - *`.
  Este repositório **aponta** para o banco; não o duplica.
- ❌ Não é o site. O conteúdo no ar está no WordPress (`site_tabela_planos`).

---

## 2. Regras duras (não negociáveis)

1. **Escolher a skill ANTES de produzir.** Todo pedido de artigo, pesquisa,
   auditoria, banco ou SERP passa primeiro por `docs/ROTEAMENTO.md`. Diga em voz
   alta qual skill você escolheu e por quê, **antes** de começar.
2. **Nenhum HTML antes da FASE 0 aprovada.** O state file
   `PESQUISA_<slug>_COMPLETO.md` tem que existir, passar no `checkpoint_fase0.py`
   (saída colada) e ser aprovado pelo usuário. "Já temos quase tudo" não existe.
3. **Um artigo = uma pasta.** Todo artefato vai para `artigos/<slug>/`.
   Nada de arquivo solto em `/tmp`, em Downloads ou na raiz.
4. **`00-ESTADO.md` é atualizado a cada fase concluída**, antes de responder ao
   usuário. É por ele que a próxima sessão sabe onde parou.
5. **Antes de qualquer ferramenta `BD - *`**, ler a skill `banco-tabelaplanos`.
   Antes de qualquer `DataForSeo`, ler `dataforseo-tabelaplanos`.
6. **Nunca inventar dado YMYL** (rede, carência, preço, coparticipação, regra da
   ANS). Não está no state file conferido → não escreve.
7. **Commitar ao fim de cada fase.** Contêiner de sessão é efêmero: o que não foi
   commitado e enviado, não existe.

---

## 3. Roteamento rápido

Tabela completa, com gatilhos: **`docs/ROTEAMENTO.md`**. Resumo:

| Pedido | Skill |
|---|---|
| Artigo Hapvida: cidade / hospital / tabela regional / pillar | `hapvida-article-builder-v7` ← **padrão deste repo** |
| "Hapvida cobre [exame/procedimento]?" (`/cobertura/`) | `hapvida-coverage-builder` |
| Artigo de bookkeeping (EUA, inglês) | `bookkeeping-article-builder-v5` |
| Artigo assinado pela pastora Mowana, a partir dos livros | `mowana-article-builder` |
| Consultar/editar/criar no banco Supabase | `banco-tabelaplanos` (**sempre antes** dos MCP `BD - *`) |
| SERP, volume, dificuldade, posição real, citação em IA | `dataforseo-tabelaplanos` |
| "por que essa página não sobe?", análise de cluster | `hapvida-ooda` |
| "está canibalizando?", veredito pontual | `hapvida-diagnostico` |
| Auditar artigo publicado / health check | `hapvida-seo-auditor` |
| Pendências, backlog, "o que falta fazer" | `pendencias-tabelaplanos` |
| Dado corporativo Hapvida (números, coparticipação, produtos) | `hapvida-data` (**não pesquise na web antes**) |
| ANS, carência, portabilidade, concorrentes | `hapvida-regulatory` |
| Inventário de artigos, anti-doorway, overlap | `hapvida-article-database` |
| Pesquisa Hapvida | ⛔ `hapvida-research` está **descontinuada** — use a FASE 0 da builder |

> **VERSÃO PADRÃO DA BUILDER HAPVIDA: `v7`** (com v7.4 lead-herói e v7.2 multiagente).
> Artigo Hapvida é feito na **v7**, sempre, sem perguntar. Este parágrafo é a
> autorização explícita e permanente que a skill exige — não peça confirmação a
> cada tarefa. Outra versão só quando o usuário nomear uma na hora ("faz na v6").

---

## 4. Onde cada coisa mora

```
artigos/<slug>/
├── 00-ESTADO.md                     ← controle: skill, fase, portões, próximo passo
├── PESQUISA_<slug>_COMPLETO.md      ← state file da FASE 0 (a fonte da verdade)
├── PLANO_MODELOS_<slug>.md          ← roteamento dos agentes (v7.2), se usado
├── checkpoints/                     ← saída .txt de cada checkpoint rodado
├── blocos/                          ← bloco-a.html, bloco-b.html, bloco-c.html
├── artigo.html                      ← HTML final, o que vai ao ar
├── schema.json                      ← JSON-LD (execução separada)
└── imagens/                         ← imagem da tabela de preço etc.

publicados/<slug>/                   ← cópia do que foi publicado + URL e data
docs/                                ← roteamento, ambiente, fluxo, decisões
scripts/cp.sh                        ← roda qualquer checkpoint das skills
```

Começar artigo novo: `scripts/novo-artigo.sh <slug>` — cria a pasta a partir de
`artigos/_TEMPLATE/`.

---

## 5. Ambiente (leia se for rodar checkpoint)

As skills foram escritas para o Claude Code no **Windows** e citam caminhos como
`C:\Users\netop\.claude\skills\...` e `C:\Users\netop\Downloads\`. **Aqui na web
esses caminhos não existem.** Traduza sempre:

| Na skill (Windows) | Aqui |
|---|---|
| `C:\Users\netop\.claude\skills\<skill>\` | resolva com `scripts/cp.sh` |
| `python -X utf8 ...\checkpoint_x.py A B` | `scripts/cp.sh <skill> checkpoint_x.py A B` |
| `C:\Users\netop\Downloads\` | `artigos/<slug>/` |
| `/mnt/user-data/outputs/` | `artigos/<slug>/` |

Detalhes e diagnóstico: `docs/AMBIENTE.md`.

**Duas coisas que mudam o trabalho neste ambiente:**

- ✅ **`WebFetch` e `curl` alcançam site externo** — o ambiente está no nível de
  rede `Full` (medido em 28/08: 5 alvos, nenhum bloqueado). **A CI-1 lê concorrente
  direto, pela rota 1.** Ainda assim, rode `scripts/testar-egress.sh` **antes** de
  toda CI-1: um domínio pode cair sozinho, e aí vale a escada de
  `docs/CI1-SEM-EGRESS.md` — que agora é contingência, não o caminho normal.
  Trecho de busca continua **não** sendo concorrente lido.
- ✅ **Subagentes aceitam modelo por chamada** — é o que torna a linha multimodelo
  da v7.2 executável de verdade. Ver `docs/LINHA-V7.md`.

---

## 6. Git

- Trabalhe sempre em branch (`claude/<assunto>`), nunca direto na `main`.
- Commit por fase concluída, mensagem descrevendo a fase:
  `artigo(recife): FASE 0 aprovada — checkpoint_fase0 OK`.
- Abrir PR **só** quando o usuário pedir.
