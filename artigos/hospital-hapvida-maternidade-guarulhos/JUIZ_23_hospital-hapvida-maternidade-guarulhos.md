modelo: opus
lente: P-A suficiencia e verdade
rodada: 1
state_file_sha256: f84b59101f37d233310bb5e45a5a88398f45bd689dee8356bb29b4fffdae8109

---

## 1. Percurso do esqueleto — quem sustenta cada seção

| Seção | Item da pesquisa que a sustenta | Veredito |
|---|---|---|
| **Lead / passagem citável** | ficha CNES 9255826 lida (nome novo, mesmo CNPJ, mesmo endereço) + decisão de keyword-ponte (seção 2) | 🟢 sustentada |
| **HS1 — o que faz este hospital diferente** | renomeação 10-11/11/2025 (CNES + 2 veículos locais) · 1ª Sala Lilás · tradução dos códigos 112-004 / 162-002 / 140-013 / 140-016 · diferenciais 1, 2 e 3 (seção 14) | 🟢 sustentada (com ressalva de fonte na Sala Lilás) |
| **HS2 — experiência do paciente** | CNES: 4 tipos de PS, 2 salas de acolhimento com classificação de risco, sala de estabilização, sala de repouso pediátrica, brinquedoteca, 16 incubadoras, 8 berços aquecidos · protocolo da Sala Lilás (imprensa) | 🟡 parcial — o eixo prometido (PS 24h, o que levar, visita, acompanhante) **não tem dado** |
| **HS3 — como chegar e informações práticas** | apenas o endereço (CNES + catálogo) e "Av. Tiradentes é eixo central", cuja fonte é **o nosso próprio artigo de cidade** | 🔴 **órfã** |
| **HS4 — quais planos dão acesso** | nenhum item mapeia produto → acesso a esta unidade. Há hub link, coparticipação por shortcode e números canônicos — nada sobre quem entra neste hospital | 🔴 **órfã** |
| **FAQ (12 + 4 substitutas)** | 8 têm dado atrás (nome, endereço, Sala Lilás, PS pediátrico, imagem, coparticipação); 5 não têm nenhum | 🔴 38% órfãs |
| **Conclusão** | fio condutor da seção 15 + diferenciais 1 e 3 | 🟢 sustentada |

A trava mecânica já dissera o mesmo em número: HS3 com **7 itens** contra 150 / 90 / 81 das outras três.

---

## 2. As quatro notas (0-10)

| Dimensão | Nota | Por quê, em uma linha |
|---|---|---|
| **Suficiência por seção** | **5** | Metade do esqueleto (HS3, HS4 e 5 das 16 FAQ) não tem dado próprio nomeado; a pesquisa dá para escrever HS1 e meia HS2. |
| **Verdade e fonte** | **6** | A espinha primária é boa (CNES lido, catálogo, DataForSeo) e as armadilhas óbvias estão travadas — mas há uma alegação de procedência falsa num número YMYL, uma fonte auto-referencial sustentando seção, e a regra das duas listas não foi aplicada em nenhuma unidade. |
| **Originalidade (substituição)** | **8** | Renomeação, Sala Lilás, CNES 9255826, as 5 unidades e a queda de 58% do nome antigo morrem todos ao trocar a praça. |
| **Valor comercial** | **6** | A ponte de keyword (9.900 + 3.600) é achado de verdade, mas a única seção que converte (HS4) está vazia e os dois pillars de dinheiro estão saturados, sem substituto de conversão. |

**Regra de parada:** libera com as 4 ≥ 8 e zero 🔴. Duas notas abaixo de 8 e seis 🔴.

---

## 3. Achados

- severidade: 🔴
  achado: A brecha nº 2 do CI-2 e a matriz de cobertura prometem que NÓS respondemos o pronto-socorro 24h, enquanto a seção 8 e o FORBIDDEN_TOKENS dizem que isso não pode ser afirmado — o redator vai ler a promessa antes de ler a proibição.
  trecho: "| PS 24h — responde? | não | não | não | não | **\"ligue para confirmar\"** | **responde (HS2)** |"
  volta para: CI-2 (e Agente 5 para a FAQ da seção 12)
  correção: Reescrever a célula da matriz e a brecha 2 para o que a pesquisa realmente entrega — "responde com o que o registro federal mostra (PS geral, obstétrico, pediátrico e traumato-ortopédico) e diz explicitamente que o CNES não registra horário" — e tirar da seção 12 a pergunta "O pronto-socorro do Hospital e Maternidade Guarulhos funciona 24 horas?", que a própria seção 16 já derrubou por overlap com a FAQ 9 do artigo de cidade.

- severidade: 🔴
  achado: A HS3 — justamente a seção que a própria pesquisa diz que disputa com o local_pack — não tem material: sobra o endereço, que o anti-doorway limita a uma aparição, e uma âncora cuja fonte é o nosso próprio artigo publicado.
  trecho: "acessibilidade / vias: Av. Tiradentes é eixo central de Guarulhos; proximidade da Rod. Presidente Dutra\n  citada no artigo de cidade já publicado — fonte: artigo de cidade (dado da casa), a reancorar"
  volta para: Agente 2/3 (recoletar)
  correção: Pela rota 4 (n8n), que leu 7 páginas, coletar o que existe e é público: linhas e corredor da Av. Tiradentes (EMTU / Prefeitura de Guarulhos), a página oficial da unidade e as coordenadas -23.46507433 / -46.53342107 já capturadas em `fontes/`. Sem isso, a HS3 vira parágrafo de endereço repetido — doorway garantido. Reancorar em fonte externa a menção da Dutra, ou deixá-la cair.

- severidade: 🔴
  achado: A HS4 é MUST-MATCH (dois concorrentes cobrem) e a pesquisa não tem um único item que ligue produto Hapvida a acesso a esta unidade — nem do catálogo, nem do guia oficial.
  trecho: "| Quais planos dão acesso | cobre mal | cobre (com concorrentes juntos) | cobre mal | não | não | cobre (HS4) |"
  volta para: Agente 2/3 (recoletar) + Agente 6
  correção: Puxar do banco a relação de produtos que incluem a unidade (ou a regra ambulatorial × hospitalar aplicada a ela) e registrar o resultado. Se não existir no catálogo, o item tem de aparecer na seção 8 (`nao_encontrado`) — hoje ele não aparece nem lá nem em lugar nenhum — e a HS4 tem de ser redesenhada para o que se pode afirmar (a porta de entrada, o encaminhamento pela rede própria), não para o que se prometeu na matriz.

- severidade: 🔴
  achado: Cinco das dezesseis FAQ finais não têm nenhum dado atrás — quatro delas o próprio state file declara bloqueadas, e ainda assim as prescreve como substitutas obrigatórias.
  trecho: "Estas quatro dependem de fonte viva (site oficial / CNES / regimento da unidade) e hoje estão bloqueadas pelo egress."
  volta para: Agente 5 (síntese) + Agente 4
  correção: FAQ prescrita sem fonte é convite a invenção em bloco de YMYL. Ou se coleta a regra da unidade (rota 4), ou se troca as quatro por perguntas que a ficha CNES sustenta (PS pediátrico, sala de estabilização, alojamento conjunto, UTI neonatal, endoscopia). A sexta órfã, "Preciso de encaminhamento para ser atendido no Hospital e Maternidade Guarulhos?", não tem nenhum item de pesquisa sobre encaminhamento ou autorização — cai ou ganha fonte.

- severidade: 🔴
  achado: A regra das duas listas não foi aplicada a nenhuma das cinco unidades: só existe a lista do catálogo, e o catálogo está comprovadamente desatualizado justamente na unidade que é o objeto do artigo.
  trecho: "**Regra das duas listas:** catálogo (5 unidades) × guia oficial (não lido nesta sessão — egress)."
  volta para: Agente 2/3 (recoletar)
  correção: A rota 4 voltou a funcionar depois desta anotação — refazer a segunda lista e preencher `no_catalogo` / `no_guia_oficial` unidade a unidade. A divergência de nome já achada tem de virar `[VERIFICAR]` explícito (não há um único `[VERIFICAR]` no arquivo inteiro), e o dado único nº 5 ("5 unidades próprias conferidas uma a uma") não pode ir ao artigo apoiado só num catálogo que erra o nome da unidade nº 1.

- severidade: 🔴
  achado: O número YMYL de leitos é apresentado como confirmado por duas fontes independentes, mas os dois veículos reproduzem a mesma divulgação da operadora, com a mesma frase — é uma fonte, não duas, e a regra das 2 fontes para dado estrutural não está satisfeita.
  trecho: "fonte: Guarulhos Todo Dia 11/11/2025 e Click Guarulhos 12/11/2025 (duas fontes independentes, mesmo número)."
  volta para: Agente 6 (conferente de fatos)
  correção: Trocar a linha de procedência por "duas veiculações da mesma divulgação da Hapvida (nov/2025) — uma cadeia de informação, não duas". **Como pode entrar no artigo:** uma única frase, atribuída e datada ("segundo a divulgação da Hapvida em novembro de 2025"), fora do lead, fora do title/meta, fora de qualquer H2, e **nunca misturada à lista traduzida do CNES** — porque a ficha federal lida não traz contagem total de leitos, só 8 de RN patológico e 13 de alojamento conjunto, e o leitor não pode sair achando que o registro oficial confirma 113/30/10. Nada de comparação ou superlativo construído em cima dele ("o maior", "mais leitos que"). Se o editor não conseguir sustentar a atribuição em uma frase, o número sai: a estrutura verificável do artigo é a do CNES.

- severidade: 🟡
  achado: A seção 11 afirma que a CI-1 não foi realizada, contradizendo a seção 5, o checkpoint e o 00-ESTADO.md — o state file se desmente sobre a própria execução.
  trecho: "coletado_em: —           # concorrentes (CI-1 não realizada)"
  volta para: Agente 6
  correção: Atualizar para `coletado_em: 2026-09-16  # concorrentes (CI-1 rota 4 / n8n, execuções 33231 e 33232)`.

- severidade: 🟡
  achado: O endereço — dado central da HS3 e do lead — carrega uma divergência de bairro entre a ficha CNES e o site da operadora que não foi registrada, e o state file descartou o complemento que explica uma das buscas relacionadas medidas.
  trecho: "logradouro: TIRADENTES, 1015, JARDIM GUARULHOS, CEP 07090000, GUARULHOS/SP"
  volta para: Agente 6
  correção: O cabeçalho e a seção 4 dizem "Jardim Santa Edwirges" (site da operadora) e a ficha CNES diz "JARDIM GUARULHOS" — registrar como `[VERIFICAR]` e definir qual vai ao artigo. E trazer para a seção 3 o complemento "1 037" que consta da ficha lida: ele responde a related_search "Avenida tiradentes 1037 guarulhos" e é, hoje, o único material de HS3 que a pesquisa realmente possui.

- severidade: 🟡
  achado: O diferencial mais forte do artigo — "a primeira Sala Lilás da Hapvida" — é superlativo de ineditismo sustentado só por imprensa local que reproduz a divulgação, e a notícia oficial da operadora estava na SERP e não foi lida.
  trecho: "titulo: A primeira Sala Lilás da Hapvida — âncora: inaugurada nesta unidade em 10/11/2025, 24h, aberta\n  inclusive a mulheres sem convênio"
  volta para: CI-1
  correção: Ler pela rota 4 a página oficial `gndi.com.br/w/noticias/o-hospital-e-maternidade-guarulhos-agora-se-chama-hospital-keila-ferreira` (o checkpoint CI-1 já a marca como não lida) e ancorar ali "primeira", "24h" e "aberta a mulheres sem convênio". Sem isso, o "1ª/inédita" entra atribuído à operadora ou não entra.

- severidade: 🟡
  achado: O FORBIDDEN_TOKENS não cobre os exames que a divulgação atribui ao hospital e que o inventário de equipamentos do CNES não confirma.
  trecho: "- pronto-socorro 24 horas\n- PS 24h\n- ONA"
  volta para: Agente 6
  correção: A matéria fala em "tomografia, raio-X, ultrassom, endoscopia e colonoscopia"; a ficha lida lista Raio X (3), Ultrassom Ecógrafo (1) e Endoscópio digestivo (3) — **não há tomógrafo**. Acrescentar "tomografia" e "tomógrafo" à lista, ou marcá-los como afirmáveis apenas sob atribuição à Hapvida. Acrescentar também as variantes de horário que hoje escapam da trava ("funciona 24 horas", "aberto 24 horas", "atendimento ininterrupto"), já que só a Sala Lilás tem 24h por escrito e a proximidade das duas frases no texto é o erro mais provável deste artigo.

- severidade: 🟡
  achado: Um item afirmado como posicionamento da cidade continua marcado como não conferido dentro do próprio state file, sem virar `[VERIFICAR]`.
  trecho: "posicao: 2ª cidade mais populosa de SP e maior cidade brasileira que não é capital — fonte: IBGE (a confirmar na leitura da página)"
  volta para: Agente 3
  correção: Confirmar no IBGE ou remover. "A confirmar" não é estado permitido num state file aprovado — ou tem fonte, ou é `[VERIFICAR]`, ou não existe.

- severidade: 🟡
  achado: Duas FAQ da seção 12 são a mesma pergunta e serão respondidas pelo mesmo e único item da pesquisa.
  trecho: "- O Hospital e Maternidade Guarulhos mudou de nome?\n- O Hospital e Maternidade Guarulhos é o mesmo Hospital Keila Ferreira?"
  volta para: Agente 5
  correção: Manter uma (a segunda é a formulação que o buscador usa) e liberar o lugar para uma pergunta que a ficha CNES sustente sozinha.

- severidade: 🟢
  achado: A trava de nomes cobre o erro real encontrado na terceira fonte de imprensa.
  trecho: "- Hospital Bispa Keila Ferreira"
  volta para: —
  correção: Nada. O Guarulhos Online publicou exatamente esse nome, o CNES e os outros dois veículos dizem "Hospital Keila Ferreira", e a pesquisa decidiu pelo CNES antes de escrever. É o ponto mais bem-feito do arquivo.

- severidade: 🟢
  achado: Os dois telefones divergentes estão simultaneamente em `nao_encontrado` e no FORBIDDEN_TOKENS, nas duas grafias que aparecem nas fontes.
  trecho: "- telefone da unidade — onde foi procurado: CNES (11 3155-2000) e site da operadora ((11) 2463-8610).\n  Dois números diferentes na mesma unidade → não entra no artigo."
  volta para: —
  correção: Nada. Só registrar que a related_search "Hospital hapvida guarulhos telefone" fica deliberadamente sem resposta — decisão certa, e o artigo deve dizer por que, em vez de silenciar.

---

VEREDITO: BLOQUEADO
