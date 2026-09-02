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

### A dúvida da credencial: encerrada

**A credencial `WordPress tabelaplanos` (`dibu11U52rFkfBly`) está anexada** aos nós
`Buscar Post` e `Salvar Post`. A leitura via API não mostrar o campo `credentials`
era redação, não ausência. Prova: o motor devolveu `content.raw` do post 33477
(`tamanhoAntes: 115183`), o que só acontece com `context=edit` autenticado. A
mensagem *"a resposta nao trouxe content.raw"* nunca apareceu.

### O bug que travava tudo, antes de qualquer teste

A primeira chamada não devolveu resultado nenhum:

```
There was an error: "Wrong type: '' is a string but was expecting a boolean
[condition 0, item 0]"
```

Na execução `28711` dá para ver que `Buscar Post` e `Conferir e Montar` rodaram
certos (`ok: true`, `ocorrencias: 1`) e quem quebrou foi o nó IF
`Gravar de Verdade?` (`n8n-nodes-base.if`, typeVersion 2.2), que estava assim:

```json
{"leftValue": "={{ $json.ok }}",
 "operator": {"type": "boolean", "operation": "true"},
 "rightValue": ""}
```

`operation: "true"` é operador **unário** — não usa `rightValue`. Sem a flag
`singleValue: true`, o n8n valida o `rightValue` (string vazia) contra o tipo
declarado (`boolean`) e, com `typeValidation: "strict"`, aborta.

Como isso acontece **antes** da decisão de gravar, o bug derrubava dry-run e
gravação igualmente — **as duas ferramentas estavam 100% inoperantes**.

Correção (via `update_workflow` / `setNodeParameter` em `/conditions`, que não
toca nas credenciais dos outros nós), nas duas condições:

```json
{"type": "boolean", "operation": "true", "singleValue": true}
```

O `update_workflow` já publica: depois dele `versionId == activeVersionId`
(`6326fb3b-f118-4d8b-9fff-9ab8c0189d71`) e a `activeVersion` traz `singleValue`.
Não foi preciso `publish_workflow`.

### Teste 1 — dry-run da correção real ✅

```json
{"id": 33477, "find": "Av. Camapuã, 8 (Cidade Nova)",
 "repl": "Av. Camapuã, 695 (Cidade Nova)", "esperado": 1, "apply": false}
```

```json
[{"gravado": false, "ok": true, "erro": null, "detalhe": null,
  "postId": 33477, "slug": "plano-hapvida-manaus",
  "operacao": "substituir", "ocorrencias": 1,
  "contexto": "rgin-bottom: 10px; padding-left: 15px; border-left: 3px solid #ff6b00;\"><strong style=\"color: #1a202c;\">PA Cidade Nova</strong> — >>>Av. Camapuã, 8 (Cidade Nova)<<< | Segunda a Domingo 7h-19h | Clínica adultos, Pediatria, Raio-X, Ultrassom</li> <li style=\"font-weight: normal; margin-bottom: ",
  "contextos": null, "ancora": null, "url": null,
  "tamanhoAntes": 115183, "tamanhoDepois": 115185,
  "aviso": "SIMULACAO: nada foi gravado. Reenvie com apply true para valer."}]
```

Casou exatamente no bloco "PA Cidade Nova", uma vez só, e não gravou.

### Teste 2 — trava de contagem ✅ (abortou como devia)

Mesma chamada com `"esperado": 3`:

```json
[{"gravado": false, "ok": false,
  "erro": "contagem divergente: esperava 3, achou 1. Nada foi alterado.",
  "detalhe": null, "postId": 33477, "slug": "plano-hapvida-manaus",
  "operacao": null, "ocorrencias": 1, "contexto": null, "contextos": null,
  "ancora": null, "url": null,
  "tamanhoAntes": 115183, "tamanhoDepois": null,
  "aviso": "Nada foi alterado."}]
```

### Teste 3 — trava de idempotência do link ✅ (abortou como devia)

```json
{"id": 39474, "frase": "Hapclínica Duque de Caxias",
 "destino": "hapclinica-duque-de-caxias-manaus", "ocorrencia": 1, "apply": false}
```

```json
[{"gravado": false, "ok": false,
  "erro": "o post ja aponta para hapclinica-duque-de-caxias-manaus. Regra da casa: um link por destino por pagina.",
  "detalhe": null, "postId": 39474, "slug": "hospital-nilton-lins-hapvida-manaus",
  "operacao": null, "ocorrencias": null, "contexto": null, "contextos": null,
  "ancora": null, "url": null,
  "tamanhoAntes": 48114, "tamanhoDepois": null,
  "aviso": "Nada foi alterado."}]
```

Nota: `ocorrencia` é obrigatório no schema da ferramenta, embora a descrição diga
"só necessário quando há mais de uma". Vale ajustar o `required` do nó
`inserir_link_interno` no workflow MCP.

### Teste 4 — aplicar de verdade ✅

A chamada `apply: true` pelo conector foi **recusada pelo classificador de
permissões da sessão** (`Permission for this action was denied by the Claude Code
auto mode classifier`) — trava do lado do cliente, não do motor. A gravação foi
feita pelo **usuário, direto no n8n**, executando o sub-workflow com o input
fixado no nó `Parametros`:

```json
[{"operacao":"substituir","id":33477,
  "find":"Av. Camapuã, 8 (Cidade Nova)",
  "repl":"Av. Camapuã, 695 (Cidade Nova)",
  "frase":"","destino":"","esperado":1,"ocorrencia":0,"apply":true}]
```

Saída do nó `Resultado Gravado`:

```json
[{"gravado": true, "statusCode": 200, "erro": null,
  "postId": 33477, "slug": "plano-hapvida-manaus",
  "operacao": "substituir", "ocorrencias": 1,
  "contexto": "... <strong style=\"color: #1a202c;\">PA Cidade Nova</strong> — >>>Av. Camapuã, 8 (Cidade Nova)<<< | Segunda a Domingo 7h-19h | ...",
  "ancora": null, "url": null,
  "tamanhoAntes": 115183, "tamanhoDepois": 115185,
  "modified": "2026-09-02T11:57:27",
  "aviso": "O WordPress guardou revisao automatica; da para reverter pelo editor."}]
```

Dois caracteres a mais, uma ocorrência, revisão guardada.

### Como rodar pelo n8n (quando o cliente bloquear a escrita)

1. Abrir o workflow `825rmKAVo3wmelMi`
2. Duplo clique no nó `Parametros`
3. No painel OUTPUT, ícone de lápis (*Edit Output*), colar o input como **lista**
   (`[{...}]`, não objeto solto), com todos os campos do schema preenchidos —
   os não usados como `""` ou `0`
4. Fechar o nó (aparece o 📌) e clicar em **Execute workflow**
5. Ler o nó `Resultado Gravado`
6. **Remover o pin.** Se ficar, toda execução manual futura repete a gravação.

### Estado do dado no ar — conferido depois de gravar

```
$ python3 scripts/wp.py grep 33477 "Av\. Camapuã, [0-9]+"
[1] pos=182889 TEXTO
    adding-left: 15px; border-left: 3px solid #ff6b00;"><strong style="color:
    #1a202c;">PA Cidade Nova</strong> —  >>>Av. Camapuã, 695<<<  (Cidade Nova) |
    Segunda a Domingo 7h-19h | Clínica adultos, Pediatria, Raio-X, Ultrassom

1 ocorrencia(s).
```

**Corrigido no ar.** Uma ocorrência, bloco certo, horário intacto.

Registrado no banco com `registrar_atualizacao` (`{"sucesso": true, "id": 46}`).

### Veredito

O motor funciona de ponta a ponta. Quatro das travas foram exercitadas contra
dados reais e se comportaram exatamente como especificado:

| Trava | Exercitada | Resultado |
|---|---|---|
| Dry-run por padrão | ✅ | `gravado: false`, avisa como aplicar |
| Guarda de contagem | ✅ | aborta com `esperado` divergente |
| Um link por destino | ✅ | recusa destino já linkado |
| Gravação + revisão | ✅ | `statusCode: 200`, revisão guardada |
| Máscara de texto seguro | ❌ | sem caso de teste que a force |
| Sem `<a>` aninhado | ❌ | idem |
| Ambiguidade explícita | ❌ | idem |

As três não exercitadas são do caminho do `inserir_link_interno` e ficam para a
primeira linkagem real — a de idempotência abortou antes de chegar nelas.

### Nota sobre o horário

O mesmo bloco publica `Segunda a Domingo 7h-19h`. **Não mexer.** O CNES diz
"24 horas contínuo", mas esse campo é um default do `codigo_tipo_unidade` 73 (a
mesma string aparece numa clínica de medicina preventiva para TEA) e a página da
Hapvida traz a seção de horários vazia. Não há fonte para nenhum dos dois
números; trocar um dado não verificado por outro, em informação de urgência, é
pior que deixar como está.
