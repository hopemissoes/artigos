# Edição pontual no WordPress — `scripts/wp.py`

## Por que existe

A ferramenta MCP `editar_conteudo_artigo` **sobrescreve o corpo inteiro** do
post. Para trocar três caracteres numa página de 300 mil, o corpo teria que
passar pelo contexto do modelo e ser redigitado inteiro — risco de corromper
uma página no ar, maior que o erro a consertar.

O `wp.py` fala direto com a REST API do WordPress. **O corpo nunca passa pelo
modelo**: o script baixa, altera a região exata e devolve.

Descoberto em 02-09-2026, ao tentar corrigir `Av. Camapuã, 8` → `695` no hub
de Manaus (post 33477, 282.873 caracteres).

## O que ele garante

| Trava | O que impede |
|---|---|
| **Dry-run por padrão** | só grava com `--apply` |
| **`--esperado N`** | aborta se a contagem de ocorrências não bater |
| **Máscara de texto seguro** | nunca altera dentro de tag, atributo, `<script>`, `<style>`, heading, `<code>`, ou shortcode do WP |
| **Sem `<a>` aninhado** | recusa linkar frase que já está dentro de um link — HTML inválido |
| **Um link por destino** | aborta se a página já aponta para o slug |
| **Ambiguidade explícita** | com N ocorrências, exige `--ocorrencia N`; não escolhe sozinho |
| **Revisão** | o WordPress guarda revisão automática — dá para reverter pelo editor |

## Credencial

Leitura (`get`, `grep`, `verify`, e todo dry-run) **não precisa de nada**.

Escrita precisa de duas variáveis no **ambiente** (não no repositório):

```
WP_USER            usuário do WordPress
WP_APP_PASSWORD    Application Password
```

Gerar em: **WordPress → Usuários → Perfil → Senhas de aplicativo**. Não é a
senha da conta; é um token revogável, específico para isto. Application
Passwords já está habilitado no site (confirmado em `/wp-json/`).

Como o contêiner da sessão é efêmero, as variáveis têm que estar na
**configuração do ambiente** do Claude Code, não num arquivo — assim toda
sessão futura já nasce com elas.

## Uso

```bash
# ler
scripts/wp.py get   39474 --out /tmp/corpo.html
scripts/wp.py grep  33477 "Camapuã[^|]*"
scripts/wp.py verify 36272 --destino hapclinica-duque-de-caxias-manaus

# corrigir texto (dry-run; some o --apply para valer)
scripts/wp.py replace 33477 \
    --find "Av. Camapuã, 8 (Cidade Nova)" \
    --repl "Av. Camapuã, 695 (Cidade Nova)" \
    --esperado 1 --apply

# inserir link interno
scripts/wp.py link 36272 \
    --frase "Hapclínica Duque de Caxias" \
    --destino hapclinica-duque-de-caxias-manaus --apply
```

## Depois de qualquer escrita

O script muda o **site**. O **banco** não se atualiza sozinho:

1. `registrar_links_artigo` (é **aditivo** — não apaga os links já gravados
   da origem; verificado por sondagem em 02-09-2026);
2. `registrar_atualizacao`, para o histórico;
3. `scripts/wp.py verify`, para confirmar que o que está no banco é o que
   está no ar.

## O que ele NÃO faz

- Não decide **onde** o link entra. Isso é trabalho editorial: a frase âncora
  tem que existir num trecho que justifique o link, e a `consultar_saturacao_destinos`
  manda não apontar para destino com 15+ backlinks.
- Não inventa dado. Se a informação a corrigir não tem fonte primária
  conferida, o problema não é de ferramenta — é de pesquisa.
