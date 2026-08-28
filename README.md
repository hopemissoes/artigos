# artigos

Mesa de trabalho e arquivo da produção de artigos — Hapvida / tabelaplanos.com.br,
cobertura, bookkeeping (EUA) e Mowana.

## Para quem chega agora (humano)

| Quero… | Vá para |
|---|---|
| entender como o Claude deve trabalhar aqui | [`CLAUDE.md`](CLAUDE.md) |
| saber qual skill serve para cada pedido | [`docs/ROTEAMENTO.md`](docs/ROTEAMENTO.md) |
| entender as fases e os portões | [`docs/FLUXO.md`](docs/FLUXO.md) |
| rodar um checkpoint / entender caminhos | [`docs/AMBIENTE.md`](docs/AMBIENTE.md) |
| saber por que algo é do jeito que é | [`docs/DECISOES.md`](docs/DECISOES.md) |
| entender a linha de 25 agentes | [`docs/LINHA-V7.md`](docs/LINHA-V7.md) |
| ler concorrente com a rede bloqueada | [`docs/CI1-SEM-EGRESS.md`](docs/CI1-SEM-EGRESS.md) |
| **liberar a rede do ambiente** | [`docs/LIBERAR-REDE.md`](docs/LIBERAR-REDE.md) |
| ver onde cada artigo parou | `artigos/*/00-ESTADO.md` |

## Comandos

Na sessão do Claude:

| Comando | O que faz |
|---|---|
| `/novo-artigo <slug> [tipo]` | abre um artigo pelo caminho certo: skill → inventário → pasta → FASE 0 → portão humano |
| `/onde-parei` | tabela de todos os artigos em produção e o próximo passo de cada um |
| `/continuar <slug>` | retoma exatamente de onde a sessão anterior parou |
| `/checar <slug>` | roda as travas mecânicas e cola as saídas |
| `/linha <slug>` | dispara a linha multiagente/multimodelo da v7.2 |

No terminal:

```bash
scripts/novo-artigo.sh <slug> [city|hospital|tr|pillar|cobertura]
scripts/skill-path.sh <nome-da-skill>
scripts/cp.sh <skill> <checkpoint.py> [args...]
scripts/testar-egress.sh                  # antes de toda CI-1
scripts/ler-pagina.sh <slug> <url>        # lê concorrente e salva em fontes/
```

## O que este repositório não guarda

- **As skills** — são pessoais e sincronizam sozinhas para toda sessão.
- **O banco** — a verdade sobre artigos, hospitais, links, FAQs e pendências está
  no Supabase, via conectores MCP `BD - *`.
- **O site** — o que está no ar vive no WordPress.

Aqui ficam o **estado**, os **artefatos** e as **regras de roteamento**.
