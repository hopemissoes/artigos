# AMBIENTE — onde as skills moram e como rodar os checkpoints

## 1. As skills não ficam neste repositório

Elas são **skills pessoais da conta**, sincronizadas automaticamente para toda
sessão — desktop, terminal ou web. Nesta sessão web elas estão em:

```
/root/.claude/skills/synced/<uuid-da-conta>_<uuid-do-set>/<nome-da-skill>/
```

O `<uuid>` **muda entre ambientes** — nunca escreva esse caminho fixo em lugar
nenhum. Para descobrir onde está uma skill agora:

```bash
scripts/skill-path.sh hapvida-article-builder-v7
```

**Consequência prática:** não copie skill para dentro deste repositório. Duas
cópias divergem, e a versão do repo fica velha sem ninguém perceber. Para mudar
uma skill, use a skill `skill-creator` e edite a original.

## 2. Tradução de caminhos Windows → aqui

Os `SKILL.md` foram escritos para o Claude Code no Windows e citam caminhos
absolutos que **não existem** neste ambiente. Traduza sempre:

| No SKILL.md (Windows) | Aqui (Linux / web) |
|---|---|
| `C:\Users\netop\.claude\skills\<skill>\` | saída de `scripts/skill-path.sh <skill>` |
| `python -X utf8` | `python3` (o UTF-8 já é o padrão) |
| `C:\Users\netop\Downloads\` | `artigos/<slug>/` |
| `/mnt/user-data/outputs/` | `artigos/<slug>/` |
| `/mnt/user-data/uploads/` | `artigos/<slug>/fontes/` |

## 3. Rodando um checkpoint

```bash
# forma geral
scripts/cp.sh <skill> <checkpoint.py> [argumentos...]

# exemplos
scripts/cp.sh hapvida-article-builder-v7 checkpoint_fase0.py \
    artigos/recife/PESQUISA_recife_COMPLETO.md city

scripts/cp.sh hapvida-article-builder-v7 checkpoint_preco_primeiro.py \
    artigos/recife/artigo.html city
```

**Sempre salve a saída** em `artigos/<slug>/checkpoints/` e **cole a saída na
conversa** — as skills exigem a saída colada, não um "passou".

```bash
scripts/cp.sh hapvida-article-builder-v7 checkpoint_fase0.py \
    artigos/recife/PESQUISA_recife_COMPLETO.md city \
    | tee artigos/recife/checkpoints/fase0.txt
```

## 4. Checkpoints disponíveis (v7)

| Script | Quando | Sobre o quê |
|---|---|---|
| `checkpoint_ci1.py` | antes de tudo | o concorrente foi realmente LIDO? |
| `checkpoint_fase0.py` | entrada | a pesquisa foi feita? (conta dado, não palavra) |
| `checkpoint_suficiencia.py` | fim do estágio 2 | a pesquisa sustenta o artigo? |
| `checkpoint_modelos.py` | pré-voo | o `PLANO_MODELOS` é válido? |
| `checkpoint_onpage.py` | Bloco A | kit on-page (keyword, title, meta, URL, H1) |
| `checkpoint_preco_primeiro.py` | HTML | ordem preço-primeiro + lead-herói (v7.4) |
| `checkpoint_voz.py` | HTML | tiques de texto de IA em português |
| `checkpoint_paragrafos.py` · `checkpoint_ritmo_visual.py` | HTML | ritmo e parede de texto |
| `checkpoint_citabilidade.py` | HTML | GEO/AEO — passagem citável |
| `checkpoint_completude.py` · `checkpoint_verificar.py` | HTML | cobertura e `[VERIFICAR]` / tokens proibidos |
| `checkpoint_doorway_final.py` | saída, no HTML final | varredura anti-doorway (Agente 21) |

Liste o que existe de fato:

```bash
ls "$(scripts/skill-path.sh hapvida-article-builder-v7)"/checkpoint_*.py
```

## 5. Conectores MCP nesta sessão

`BD - Consultar` · `BD - Criar` · `BD - Editar` · `BD - backlinks` ·
`DataForSeo` · `SEO - Hapvida` (n8n) · `site_tabela_planos` (WordPress) ·
`seo-tools` (GSC/GA4) · `Google Drive` · `github`.

Se um conector não responder, **diga que não respondeu** — não substitua o dado
por estimativa.

## 6. O que este ambiente alcança (medido em 2026-08-28)

| Recurso | Status | Consequência |
|---|---|---|
| `WebSearch` | ✅ | SERP, títulos e trechos — **não** a página inteira |
| MCP `DataForSeo`, `BD - *`, `SEO - Hapvida`, `site_tabela_planos`, `seo-tools` | ✅ | rodam no servidor, fora deste contêiner |
| `pip install` | ✅ | pypi liberado (`requirements.txt`) |
| Subagentes com modelo por chamada (`Agent`) | ✅ | é o que torna a linha da v7.2 possível — ver `docs/LINHA-V7.md` |
| `WebFetch` / `curl` para site externo | ❌ **bloqueado** (nível Trusted) | **a CI-1 não lê concorrente direto** — contorno em `docs/CI1-SEM-EGRESS.md`, solução em `docs/LIBERAR-REDE.md` |

Meça na hora, não confie nesta tabela:

```bash
scripts/testar-egress.sh
```

## 7. Dependências python

```bash
pip install -r requirements.txt   # só Pillow; os checkpoint_*.py são stdlib
```

O `SessionStart` hook (`.claude/hooks/session-start.sh`) já faz isso e ainda
imprime o roteamento, o estado do egress e os artigos abertos.

## 8. Arquivos-fonte (PDF de rede, OCR, captura de concorrente)

Não há arrastar-e-soltar aqui. Três rotas:

1. **Google Drive** — o MCP está disponível (`search_files`, `read_file_content`);
2. **colar no chat** e eu salvo em `artigos/<slug>/fontes/`;
3. **commitar** direto na pasta `fontes/` do artigo.

Arquivo-fonte fica em `artigos/<slug>/fontes/`, sempre — é o que permite conferir
o dado meses depois.
