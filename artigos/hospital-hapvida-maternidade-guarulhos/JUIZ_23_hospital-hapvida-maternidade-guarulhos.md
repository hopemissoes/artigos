modelo: opus
lente: P-A suficiencia e verdade
rodada: 2
state_file_sha256: 926b6e77294c8d674a7f599d6485cfa01b34d0668a3fd0021cdc1894c6506438

> Rodada 1 (sha256 f84b59101f37d233310bb5e45a5a88398f45bd689dee8356bb29b4fffdae8109) fechou **BLOQUEADO**
> com 6 🔴 e 6 🟡. Este documento substitui aquele veredito. O que segue julga o arquivo corrigido e a
> terceira coleta (`fontes/ci1-rodada3.json`, `fontes/ci1-rodada2-fontes-primarias.md` seção 5), sem
> crédito pelo esforço: só conta o que a correção resolveu.

---

## 1. Percurso do esqueleto — quem sustenta cada seção agora

| Seção | Item que a sustenta | Veredito |
|---|---|---|
| **Lead** | ficha CNES 9255826 + decisão de keyword-ponte | 🟢 |
| **HS1** | renomeação (CNES + 4 veiculações) · Sala Lilás com fonte setorial (Saúde Business 13/11/2025) · tradução dos códigos · quem foi a homenageada | 🟢 |
| **HS2** | CNES: 4 PS registrados, 2 salas de acolhimento com classificação de risco, sala de estabilização, sala de repouso pediátrica, 13 de alojamento conjunto, 5 salas de cirurgia, 16 incubadoras · protocolo da Sala Lilás · reconciliação com o Rosário escrita | 🟡 falta a segunda reconciliação (achado 13) |
| **HS3** | complemento "1 037", CEP, divergência de bairro, coordenadas, eixo viário com fonte, canais de agendamento | 🟡 escrevível — mas 5 dos 12 itens não têm evidência salva (achado 14) |
| **HS4** | produtos de Guarulhos (banco) · Ambulatorial não cobre internação · isenção de coparticipação em internação · proibições dos pillars | 🟡 escrevível como inferência declarada, não como fato (achado 15) |
| **FAQ (10)** | 10 de 10 com fonte nomeada ao lado; as 3 queimadas e as 4 sem fonte saíram | 🟢 |
| **Conclusão** | fio condutor + diferenciais 1 e 3 | 🟢 |

Resolvidos de verdade na rodada 2: **1** (PS: a promessa virou "digo quais PS constam no registro e digo que o
horário não consta em fonte nenhuma"), **4** (FAQ reescrita, 10 perguntas com fonte), **5** (duas listas
aplicadas, lista B declarada indisponível e a consequência de escrita escrita, inclusive a proibição de
afirmar ausência), **6** (leitos reclassificados como uma cadeia de divulgação, com o tratamento exato),
**7** (datas), **8** (bairro, complemento, CEP, coordenadas), **9** (superlativo com fonte setorial),
**10** (FORBIDDEN de 12 → 20, com tomografia, colonoscopia e as variantes de 24 horas), **11** (IBGE virou
`[VERIFICAR]` e ficou fora), **12** (par duplicado sumiu).

Os achados 5 e 6 deixaram de ser buraco e viraram o melhor material do arquivo: a seção 4 hoje ensina o
redator a escrever sem afirmar o que não se sabe. Não é elogio, é constatação de que a categoria de erro
morreu.

**Restam dois 🔴 — um herdado por meio-conserto (2) e um novo, criado pela própria correção.**

---

## 2. As quatro notas (0-10)

| Dimensão | R1 | **R2** | Por quê |
|---|---|---|---|
| **Suficiência por seção** | 5 | **7** | Nenhuma seção está mais órfã e a FAQ está inteira. Mas a HS3 segue com 12 itens contra 164/97/114, e cinco deles não têm evidência salva; a HS4 se sustenta numa dedução. |
| **Verdade e fonte** | 6 | **7** | Os dois piores vícios morreram (procedência inflada dos leitos, duas listas ausentes). Nasceu um pior no lugar: material novo de HS3 atribuído ao CNES que não está em nenhuma fonte salva. Mais duas contagens de fonte otimistas. |
| **Originalidade (substituição)** | 8 | **8** | Inalterada, e agora honesta: o arquivo admite que o próprio artigo de cidade já traz "(ex-Hospital e Maternidade GRU)". Encolhe o ganho, não o elimina. |
| **Valor comercial** | 6 | **7** | O MUST-MATCH "contato/como agendar" foi resolvido sem o telefone, o que é melhor que o concorrente. Mas a única frase que move a compra — qual plano abre a porta deste hospital — é inferência, e é a peça pior sustentada do artigo. |

Três dimensões abaixo de 8 e dois 🔴.

---

## 3. Achados

- severidade: 🔴
  achado: O bloco de referências a pé da HS3 é atribuído ao CNES, não está no CNES, e não existe em nenhuma fonte salva — só o título "Unidades Próximas" foi capturado, o conteúdo nunca.
  trecho: "- referências a pé, do próprio CNES: serviço de hemoterapia na mesma Av. Tiradentes a **0,1 km**;\n  Hospital da Criança 12 de Outubro na Av. Paulo Faccini a **0,2 km**; consultórios na Rua Antônio Vita a\n  0,1-0,2 km — fonte: bloco \"Unidades Próximas\" do espelho do CNES"
  volta para: Agente 6 (conferente de fatos) — coleta do Agente 3
  correção: Procurei em `ci1-rodada3.json`, `ci1-extracao-n8n.json` e na transcrição da rodada 2: não há "Vita", não há "12 de Outubro", não há "0,1 km", não há bloco de unidades próximas com conteúdo — o extrator salvou o H3 "Unidades Próximas" e mais nada. Três problemas somados: a fonte está rotulada errado dentro do próprio bullet ("do próprio CNES" × "do espelho do CNES" — são coisas diferentes, e o registro federal não publica distância); distância de agregador é cálculo de widget, não dado de registro; e o Hospital da Criança 12 de Outubro é unidade municipal, não da Hapvida — citá-lo a "0,2 km" numa página de hospital da operadora mistura rede pública e rede própria na cabeça de quem lê. **Ou o bloco sai inteiro, ou volta com a página salva em `fontes/` e a fonte nomeada pelo que ela é.** Enquanto estiver assim, é o único material "prático" da HS3 e o redator vai usá-lo.

- severidade: 🔴
  achado: O artigo novo vai dizer que o registro federal lista PS traumato-ortopédico enquanto o nosso próprio artigo publicado manda a ortopedia de urgência fora do horário comercial para a capital — e o state file trata a FAQ 9 do de cidade só como "queimada", sem nenhuma regra de reconciliação.
  trecho: "Queimadas (não repetir, nem reformuladas): \"O Hospital Keila Ferreira tem maternidade e UTI neonatal?\" ·\n\"Qual a diferença entre o Hospital Keila Ferreira e as clínicas?\" · \"A Hapvida tem pronto-atendimento 24h na cidade?\" ·"
  volta para: CI-2 / Agente 5 (é o mesmo tipo de conserto já feito para o Rosário)
  correção: O HTML publicado em `fontes/artigo-cidade-guarulhos.html` responde: "O Hospital Keila Ferreira opera com pronto-atendimento para urgências e emergências. Para atendimento especializado **fora do horário comercial**, como ortopedia de urgência, o beneficiário pode acessar o pronto-socorro Hapvida em SP capital". Lado a lado com "o CNES registra PS traumato-ortopédico (140-016)", o leitor em emergência recebe duas orientações diferentes do mesmo site sobre para onde levar uma fratura de madrugada — o dano é maior que o de doorway. Escrever a reconciliação obrigatória nos mesmos moldes da que já existe para o Rosário: **ter o serviço registrado no CNES ≠ ter plantão da especialidade a qualquer hora**; dizer o que o registro lista, dizer que o horário não é publicado, e manter na mesma passagem o encaminhamento à capital com o link para `pronto-socorro-hapvida-sp`, que o plano de links já prevê para a HS2. E registrar como pendência que a frase "fora do horário comercial" do artigo de cidade também não tem fonte.

- severidade: 🟡
  achado: A regra que liga produto a esta unidade é dedução do agente, marcada como defensibilidade 1, e a seção 8 não registra que nenhuma fonte mapeia produto → hospital.
  trecho: "- regra que liga produto a esta unidade: o hospital é **rede própria**, então entra nos planos que incluem\n  internação em rede própria (Nosso Plano e Mix)."
  volta para: Agente 6
  correção: As duas pontas são sólidas — os produtos vêm do banco e "Ambulatorial não cobre internação" é segmentação da ANS. O "então" no meio é inferência, e o guia oficial (lista B) que confirmaria está declarado indisponível na seção 4 do próprio arquivo. Pesa a favor que o artigo de cidade já publica o fluxo ("caso precise de internação ou procedimento cirúrgico, é direcionado ao Hospital Keila Ferreira"), mas isso é a nossa fonte confirmando a nossa fonte. Três consertos: rebaixar a defensibilidade e rotular como **inferência**, não como dado de banco; acrescentar à seção 8 "nenhuma fonte lida mapeia produto → esta unidade — o guia oficial é SPA"; e travar a forma de escrita — a HS4 diz que plano com internação usa a rede própria e que o hospital próprio de Guarulhos é este, e **manda conferir a rede do plano específico no guia médico**, nunca "o plano X dá acesso". Escrito como fato, isto vira 🔴 no painel do Estágio 5.

- severidade: 🟡
  achado: O mesmo arquivo que de-rateou corretamente os leitos por virem de uma cadeia única conta "4 fontes" para o 24h da Sala Lilás, que vem da mesma cadeia.
  trecho: "· \"24 horas\" está proibido para o PRONTO-SOCORRO. A Sala Lilás tem 24h confirmado por escrito em 4\n       fontes"
  volta para: Agente 6
  correção: Nas fontes salvas, duas veiculações trazem o 24h ("funciona 24 horas por dia e conta com equipe multiprofissional disponível em tempo integral" e "O grupo informa que espaço está disponível 24 horas por dia"), com a redação da mesma divulgação; Saúde Business e Jornal Exempplar não dizem horário nos trechos capturados. Corrigir para "a mesma divulgação da Hapvida, reproduzida por dois veículos" e escrever o 24h da Sala Lilás **atribuído** — é o padrão que o arquivo já aplicou aos leitos, e ele não pode valer só para o número que incomoda.

- severidade: 🟡
  achado: A FAQ de agendamento aponta para "o 0800 nacional", que não existe como número único — a fonte capturada traz dois 0800 por região.
  trecho: "- Como agendar consulta ou exame no Hospital e Maternidade Guarulhos? — fonte: canais oficiais publicados no\n  rodapé de hapvida.com.br (app, área do beneficiário, agendamento de consultas e exames e o 0800 nacional)."
  volta para: Agente 6
  correção: O rodapé lido diz "0800 280 9130 Norte e Nordeste para telefones fixos · 0800 018 3456 Sul, Sudeste e Centro-Oeste | 24h por dia". Para Guarulhos vale o segundo. Trazer o número certo e a região para o state file — senão o redator escreve "o 0800 nacional" (que não existe) ou escolhe um dos dois no chute, que é exatamente o erro dos dois telefones da unidade que este arquivo passou duas rodadas evitando. Atenção à colisão com a trava: o "24h por dia" aqui é do call center, e a expressão não pode encostar no pronto-socorro.

- severidade: 🟡
  achado: O quinto diferencial continua ancorado no acesso pela Dutra, que a seção 16 declara queimado pelo artigo de cidade e que a coleta nova não renovou.
  trecho: "- titulo: Quem vem de fora da cidade — âncora: a Av. Tiradentes e o acesso pela Dutra, no eixo central"
  volta para: Agente 5
  correção: A própria seção 16 diz "12 km do Aeroporto GRU, 15-25 min pela Dutra | Já é do de cidade (FAQ 12). Só pode voltar como ângulo de acesso, com dado novo" — e a rodada 3 não trouxe dado novo de acesso (ônibus não confirmado, estacionamento não confirmado). Trocar a âncora pelo que a coleta realmente rendeu (o complemento 1 037 e a divergência de bairro, que são o que faz alguém errar o caminho) ou derrubar o diferencial. É o mesmo item que a trava E vem marcando nas duas rodadas.

- severidade: 🟡
  achado: Fontes novas entram no state file por apelido, sem URL e com a data da coleta no lugar da data de publicação.
  trecho: "Joi (16/09/2026). Quem procura pelo bairro errado no mapa não acha. É material de HS3, não erro a esconder."
  volta para: Agente 6
  correção: "Joi" é `oitapecericano.com.br`, veículo regional que reproduz a divulgação, e 16/09/2026 é o dia em que nós lemos, não em que ele publicou. O redator e o auditor do Estágio 5 trabalham pelo state file, não pela pasta `fontes/`: trazer URL e data de publicação de Saúde Business, Jornal Exempplar e Joi para a seção 1 ou para a seção 7. Vale em especial para a FAQ "Quem foi Keila Ferreira" — o detalhe do casamento com o bispo Samuel Ferreira aparece só nesse veículo, e biografia de pessoa real recém-falecida se escreve atribuída ou não se escreve.

- severidade: 🟢
  achado: O tratamento dos 113 leitos ficou do jeito que a rodada 1 pediu, e mais: o arquivo passou a nomear a cadeia de divulgação como cadeia.
  trecho: "fonte: **uma única cadeia de divulgação** reproduzida por 4 veículos (Guarulhos Todo Dia 11/11/2025,\n  Click Guarulhos 12/11/2025, Jornal Exempplar e Joi) com a mesma frase — **não são 4 fontes independentes**."
  volta para: —
  correção: Nada. Só manter: mais veículo repetindo o mesmo release não vira mais fonte, e o arquivo agora ensina isso ao redator dentro do próprio item.

- severidade: 🟢
  achado: A regra das duas listas virou regra de escrita, inclusive a parte que quase ninguém escreve — a proibição de afirmar ausência.
  trecho: "**nunca** afirma ausência (\"não há outra unidade em X\") — ausência no catálogo não é prova de ausência na\n  rede."
  volta para: —
  correção: Nada.

- severidade: 🟢
  achado: A FAQ passou a ter fonte nomeada por pergunta, e as quatro perguntas boas sem dado foram para pauta futura em vez de irem para o artigo.
  trecho: "as quatro substitutas sem fonte (o que levar, visita, acompanhante, estacionamento) também\nsaíram — pergunta sem dado não entra, mesmo sendo boa pergunta."
  volta para: —
  correção: Nada.

---

**Para o portão humano, em uma linha:** travou em dois pontos que se resolvem editando o state file, sem
nova coleta — apagar (ou salvar a página de) o bloco de distâncias da HS3 que não está em fonte nenhuma, e
escrever a regra que impede o artigo de contradizer a FAQ 9 do nosso artigo de cidade sobre para onde vai
uma urgência ortopédica fora do horário comercial.

VEREDITO: BLOQUEADO
