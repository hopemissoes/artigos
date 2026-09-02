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

---

## Teste das ferramentas MCP novas — 02-09-2026

Sessão dedicada a exercitar `substituir_no_artigo` e `inserir_link_interno`
(as duas `toolWorkflow` do conector `Site tabelaplanos.com.br`, que delegam ao
sub-workflow `WP - Motor de Edicao Pontual`, `825rmKAVo3wmelMi`).

**As duas ferramentas apareceram na lista do conector** — o cache que as escondia
na sessão anterior era do lado do cliente e caiu sozinho na sessão nova.

### Teste 1 — dry-run da correção real (post 33477)

Chamada:

```json
{"id": 33477, "find": "Av. Camapuã, 8 (Cidade Nova)",
 "repl": "Av. Camapuã, 695 (Cidade Nova)", "esperado": 1, "apply": false}
```

Retorno para o assistente:

```
There was an error: "Wrong type: '' is a string but was expecting a boolean
[condition 0, item 0]"
```

**O erro NÃO é o de credencial.** Lendo a execução `28711` do motor, dá para
separar o que funcionou do que quebrou:

| Nó | Resultado |
|---|---|
| `Parametros` | `{"operacao":"substituir","id":33477,"find":"Av. Camapuã, 8 (Cidade Nova)","repl":"Av. Camapuã, 695 (Cidade Nova)","frase":"","destino":"","esperado":1,"ocorrencia":0,"apply":false}` |
| `Buscar Post` | 200, trouxe `content.raw` — **a credencial autenticou** |
| `Conferir e Montar` | `ok: true`, `aplicar: false`, `ocorrencias: 1`, `postId: 33477`, `slug: plano-hapvida-manaus`, `tamanhoAntes: 115183`, `tamanhoDepois: 115185` |
| `Gravar de Verdade?` | ❌ erro, abortou a execução |

Contexto devolvido pelo motor, confirmando que casou no bloco certo:

```
rgin-bottom: 10px; padding-left: 15px; border-left: 3px solid #ff6b00;">
<strong style="color: #1a202c;">PA Cidade Nova</strong> — >>>Av. Camapuã, 8<<<
 (Cidade Nova) | Segunda a Domingo 7h-19h | ...
```

**Duas conclusões que valem mais que o teste:** a credencial do cofre está
mesmo anexada nos nós `httpRequest` (a leitura via API não mostrava o campo
`credentials`, mas era redação, não ausência), e toda a lógica das travas roda
correta.

### O bug do nó IF

O nó `Gravar de Verdade?` (`n8n-nodes-base.if`, typeVersion 2.2) tinha as duas
condições assim:

```json
{"leftValue": "={{ $json.ok }}",
 "operator": {"type": "boolean", "operation": "true"},
 "rightValue": ""}
```

`operation: "true"` é um operador **unário** — não usa `rightValue`. Mas sem a
flag `singleValue: true`, o n8n valida o `rightValue` (string vazia) contra o
tipo declarado (`boolean`) e, com `typeValidation: "strict"`, aborta. Daí o
`'' is a string but was expecting a boolean`.

Como isso acontece **antes** de qualquer decisão de gravar, o bug derrubava
igualmente dry-run e gravação — ou seja, **as duas ferramentas estavam 100%
inoperantes**, não só a de escrita.

Correção aplicada (`update_workflow`, `setNodeParameter` em `/conditions`, que
não toca nas credenciais dos outros nós):

```json
{"type": "boolean", "operation": "true", "singleValue": true}
```

⚠️ **A correção está salva mas NÃO publicada.** O `publish_workflow` foi recusado
pelo classificador de permissões da sessão. Enquanto ninguém publicar pela
interface do n8n, o motor segue abortando.

### Testes 2, 3 e 4 — NÃO EXECUTADOS

Depois do teste 1, as chamadas ao conector passaram a ser recusadas na origem:

```
Permission for this action was denied by the Claude Code auto mode classifier.
Reason: Blocked by classifier.
```

Ficaram **por exercitar** — nenhuma saída aqui é para ser tomada como verificada:

1. **Trava de contagem** — `esperado: 3` no mesmo `find`; deve devolver
   `contagem divergente: esperava 3, achou 1. Nada foi alterado.`
2. **Trava de idempotência do link** — `inserir_link_interno` no post 39474 para
   `hapclinica-duque-de-caxias-manaus`; deve recusar porque a página já aponta
   para o destino.
3. **Gravação de verdade** — teste 1 com `apply: true`.

### Estado do dado no ar

`scripts/wp.py grep` (leitura, sem credencial) em 02-09-2026, **depois** da
sessão:

```
$ python3 scripts/wp.py grep 33477 "Av\. Camapuã, [0-9]+"
[1] pos=182889 TEXTO
    ... <strong style="color: #1a202c;">PA Cidade Nova</strong> —
    >>>Av. Camapuã, 8<<<  (Cidade Nova) | Segunda a Domingo 7h-19h | ...

1 ocorrencia(s).
```

**O endereço errado continua publicado.** A correção para `695` (conferida em
três fontes: `rede_unidades` no Supabase, a página da unidade no site da Hapvida
e a coordenada) **não foi aplicada**, e por isso **nada foi registrado no banco**
com `registrar_atualizacao` — não houve alteração a registrar.

### Nota sobre o horário

O mesmo bloco publica `Segunda a Domingo 7h-19h`. **Não mexer.** O CNES diz
"24 horas contínuo", mas esse campo é um default do `codigo_tipo_unidade` 73 (a
mesma string aparece numa clínica de medicina preventiva para TEA) e a página da
Hapvida traz a seção de horários vazia. Não há fonte para nenhum dos dois
números; trocar um dado não verificado por outro, em informação de urgência, é
pior que deixar como está.
