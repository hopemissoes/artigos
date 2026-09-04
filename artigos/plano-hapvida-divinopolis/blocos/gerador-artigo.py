# -*- coding: utf-8 -*-
H2 = lambda t,s: (f'<h2 style="font-size:clamp(24px,4vw,30px);font-weight:900;color:#1a202c;margin-bottom:8px;">{t}</h2>'
    f'<p style="text-align:justify!important;font-size:18px;font-weight:500;color:#718096;margin-bottom:12px;">{s}</p>'
    '<div style="width:60px;height:4px;background:linear-gradient(90deg,#ff6b00,#ff8533);border-radius:2px;margin-bottom:28px;"></div>')
P  = lambda t: f'<p style="text-align:justify!important;font-size:18px;color:#4a5568;line-height:1.7;margin-bottom:16px;">{t}</p>'
H3 = lambda t: f'<h3 style="font-size:19px;font-weight:800;color:#1a202c;margin:14px 0 10px 0;">{t}</h3>'
G  = lambda t: ('<span class="destaque-laranja-suave" style="background-image:linear-gradient(120deg,rgba(255,107,0,0.22) 0%,rgba(255,133,51,0.22) 100%);'
    'background-repeat:no-repeat;background-position:0 50%;background-size:100% 100%;padding:2px 6px;transition:background-size 1.2s ease-out;">'+t+'</span>')
def BOX(letra,rotulo,txt,badge=True):
    b=(f'<span style="width:28px!important;height:28px!important;min-width:28px!important;max-width:28px!important;flex-shrink:0!important;'
       f'background:#2563eb!important;border-radius:8px!important;display:inline-flex!important;align-items:center!important;justify-content:center!important;'
       f'color:#fff!important;font-size:14px!important;font-weight:800!important;line-height:1!important;font-family:Arial,Helvetica,sans-serif!important;'
       f'text-align:center!important;box-sizing:border-box!important;padding:0!important;margin:0!important;vertical-align:middle!important;">{letra}</span>') if badge else ''
    return ('<div style="background:linear-gradient(135deg,#eff6ff 0%,#dbeafe 100%);border:1px solid #bfdbfe;border-radius:12px;padding:24px 28px;margin-bottom:24px;">'
      '<div class="box-row" style="display:flex!important;align-items:center!important;gap:10px!important;margin-bottom:12px!important;line-height:1!important;flex-wrap:nowrap!important;">'
      +b+f'<span style="font-size:14px;font-weight:700;color:#1e40af;text-transform:uppercase;letter-spacing:1px;line-height:1.2;">{rotulo}</span></div>'
      f'<p style="text-align:justify!important;font-size:18px;line-height:1.7;color:#1e40af;margin:0;">{txt}</p></div>')
SEC = lambda i,bg,inner: f'<section style="background:{bg};padding:20px 10px;border-radius:20px;margin-bottom:4px;" id="{i}">{inner}</section>'
def card(badge,cor,titulo,desc,faixa,faixacor,bgfaixa,basis="220px",borda="1px solid #e2e8f0"):
    return (f'<div style="flex:1 1 {basis}!important;box-sizing:border-box!important;background:#fff;border:{borda};border-radius:20px;padding:28px 22px;">'
      f'<div style="width:36px;height:36px;background:{cor};border-radius:10px;display:flex!important;align-items:center!important;justify-content:center!important;'
      f'color:#fff;font-size:16px;font-weight:800;margin-bottom:14px;">{badge}</div>'
      f'<h3 style="font-size:17px;font-weight:800;color:#1a202c;margin-bottom:8px;">{titulo}</h3>'
      f'<p style="text-align:justify!important;font-size:14px;color:#4a5568;line-height:1.6;margin-bottom:12px;">{desc}</p>'
      f'<div style="background:{bgfaixa};border-radius:8px;padding:10px 14px;font-size:13px;color:{faixacor};font-weight:600;">{faixa}</div></div>')
def toc_item(num,href,txt):
    return ('<div class="toc-item" style="display:flex!important;align-items:center!important;gap:10px!important;padding:0!important;margin:0!important;">'
      '<span class="toc-badge" style="min-width:28px;height:28px;flex-shrink:0!important;background:#ff6b00;border-radius:8px;display:flex!important;'
      f'align-items:center!important;justify-content:center!important;color:#fff;font-size:13px;font-weight:700;">{num}</span>'
      f'<a href="{href}" style="color:#1a202c;font-weight:600;font-size:15px;text-decoration:none;">{txt}</a></div>')
def faq(n,q,a):
    return ('<details style="border:1px solid #e2e8f0;border-radius:10px;margin-bottom:12px;">'
      '<summary style="padding:16px 20px;font-size:18px;font-weight:600;color:#1a202c;cursor:pointer;display:flex!important;'
      'justify-content:space-between!important;align-items:center!important;list-style:none;">'
      f'<span>{n}. {q}</span><span style="color:#ff6b00;font-size:20px;font-weight:300;transition:transform 0.3s;">+</span></summary>'
      '<div style="padding:14px 20px;font-size:14px;color:#4a5568;line-height:1.7;background:#fafbfc;border-top:1px solid #e2e8f0;">'
      f'<p style="text-align:justify!important;margin:0;">{a}</p></div></details>')
open('/tmp/helpers_ok','w').write('ok')

FORM = '<div id="cotacao-1" style="margin-bottom:4px;">[elementor-template id="11215"]</div>'
FORM2 = '<div style="margin-bottom:4px;">[elementor-template id="11215"]</div>'
SELOS = ('<div class="v5-trust" style="display:flex!important;flex-wrap:wrap!important;justify-content:center!important;gap:10px!important;margin:10px 0 24px 0;">'
 '<span style="font-size:12px;color:#64748b;font-weight:600;border:1px solid #e2e8f0;border-radius:999px;padding:6px 12px;background:#fff;">Hospital registrado no CNES sob o codigo 2159376</span>'
 '<span style="font-size:12px;color:#64748b;font-weight:600;border:1px solid #e2e8f0;border-radius:999px;padding:6px 12px;background:#fff;">DRV Corretora: mais de 10 anos especialista Hapvida</span>'
 '<span style="font-size:12px;color:#64748b;font-weight:600;border:1px solid #e2e8f0;border-radius:999px;padding:6px 12px;background:#fff;">Rede conferida no Guia Medico oficial em 01/09/2026</span></div>')

# ---------------------------------------------------------------- LEAD-HEROI
hero = ('<div class="v5-hero-conv" style="background:linear-gradient(135deg,#1a1a2e,#16213e);border-radius:20px;padding:28px 24px;margin-bottom:4px;">'
 '<div style="font-size:12px;font-weight:700;color:#ff8533;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">Plano Hapvida em Divinopolis</div>'
 '<div style="font-size:34px;font-weight:900;color:#fff;line-height:1.1;margin-bottom:18px;">A partir de <span style="color:#ff8533;">[divinopolis_menorvalor]</span>/mes</div>'
 '<p style="text-align:justify!important;font-size:18px;line-height:1.7;color:#e2e8f0;margin-bottom:16px;">'
 'O plano Hapvida em Divinopolis se apoia numa rede propria concentrada: hospital, centro clinico e servico de imagem ficam no '
 '<strong style="color:#ff8533;">mesmo numero da Rua Pedro Ferreira do Amaral, no Padre Liberio</strong>, e ha uma unidade de medicina '
 'preventiva no Centro. Sao quatro unidades proprias na cidade, e os planos comecam a partir de [divinopolis_menorvalor] por mes.</p>'
 '<div class="v5-hero-metricas" style="display:flex!important;flex-wrap:wrap!important;gap:24px!important;margin-top:20px;padding-top:18px;border-top:1px solid rgba(255,255,255,0.15);">'
 '<div><div style="font-size:20px;font-weight:900;color:#fff;">4</div><div style="font-size:12px;color:#94a3b8;">unidades proprias na cidade</div></div>'
 '<div><div style="font-size:20px;font-weight:900;color:#fff;">24h</div><div style="font-size:12px;color:#94a3b8;">plantao continuo no hospital</div></div>'
 '<div><div style="font-size:20px;font-weight:900;color:#fff;">20</div><div style="font-size:12px;color:#94a3b8;">municipios na regiao imediata</div></div></div></div>')

# ---------------------------------------------------------------- S2 a (PRECOS + TABELA)
s2a = SEC('precos','#fff',
 H2('O preco do plano Hapvida em Divinopolis, faixa a faixa','Os planos comecam a partir de [divinopolis_menorvalor] por mes em Divinopolis, com valores por faixa etaria definidos pela tabela do grupo das demais pracas — a mesma que vale para o interior mineiro, e nao a de Belo Horizonte. A tabela vigente esta logo abaixo.')
 + P('Divinopolis nao esta no grupo tarifario de Sao Paulo e Belo Horizonte, e isso muda o valor. A cidade entra na tabela das '
     'demais pracas, a mesma que vale para o interior mineiro. ' + G('A tabela abaixo e a vigente') + ', renderizada pelo sistema no '
     'momento em que voce abre a pagina.')
 + P('Vale saber o que voce esta comprando aqui: em Divinopolis a estrutura propria e um complexo unico, entao a mensalidade '
     'compra acesso a um endereco que resolve consulta, exame e internacao no mesmo lugar, e nao a uma rede espalhada por bairros.')
 + '[divinopolis_menortabela]'
 + '<p style="text-align:justify!important;font-size:12px;color:#94a3b8;font-style:italic;margin-top:12px;margin-bottom:0;">Valores por faixa etaria conforme tabela vigente. Sujeitos a alteracao por modalidade, acomodacao e condicoes comerciais.</p>')

# ---------------------------------------------------------------- SUMARIO
toc = ('<section style="background:linear-gradient(135deg,#fafbfc 0%,#f0f4f8 100%);padding:20px 10px;border-radius:20px;margin-bottom:4px;border:1px solid #e2e8f0;">'
 '<div class="toc-list" style="display:flex!important;flex-direction:column!important;gap:10px!important;padding:0!important;margin:0!important;">'
 '<div class="toc-item" style="display:flex!important;align-items:center!important;gap:10px!important;padding:0!important;margin:0!important;">'
 '<span style="min-width:28px;height:28px;flex-shrink:0!important;background:#ff6b00;border-radius:8px;display:flex!important;align-items:center!important;'
 'justify-content:center!important;color:#fff;font-size:14px;font-weight:700;">&equiv;</span>'
 '<span style="font-size:17px;font-weight:800;color:#1a202c;">Neste Guia Voce Vai Encontrar</span></div>'
 + toc_item(1,'#precos','O preco do plano, faixa a faixa')
 + ('<div class="toc-item" style="display:flex!important;align-items:center!important;gap:10px!important;padding:0!important;margin:0!important;">'
    '<span class="toc-badge" style="min-width:28px;height:28px;flex-shrink:0!important;background:#ff6b00;border-radius:8px;display:flex!important;'
    'align-items:center!important;justify-content:center!important;color:#fff;font-size:13px;font-weight:700;">$</span>'
    '<a href="#cotacao-1" style="display:inline-block;color:#fff!important;font-weight:800;font-size:15px;text-decoration:none;padding:6px 14px;'
    'background:linear-gradient(135deg,#ff6b00,#e85d00);border-radius:6px;box-shadow:0 4px 14px rgba(255,107,0,0.35);">Faca uma Cotacao</a></div>')
 + toc_item(2,'#por-que-divinopolis','Por que Divinopolis e um caso diferente')
 + toc_item(3,'#planos-disponiveis','Como escolher o plano nesta cidade')
 + toc_item(4,'#rede-divinopolis','A rede propria da Hapvida em Divinopolis')
 + toc_item(5,'#cobertura-bairros','De qual bairro voce chega mais rapido')
 + toc_item(6,'#cenario-saude','O mercado de saude de Divinopolis')
 + toc_item(7,'#como-contratar','O que decidir antes de assinar')
 + toc_item(8,'#faq','Perguntas frequentes de quem mora aqui')
 + toc_item(9,'#conclusao','Conclusao')
 + '</div></section>')
open('/tmp/part1_ok','w').write('ok')

# ---------------------------------------------------------------- S2 b (analise + copart)
s2b = SEC('analise-preco','#fff',
 SELOS
 + P('Uma leitura pratica da tabela: a curva sobe pouco ate a faixa dos 30 e acelera depois dos 44 anos, que e o comportamento '
     'padrao das dez faixas da ANS. Para uma familia de Divinopolis, o que costuma decidir o orcamento nao e a faixa do titular, e sim ' + G('quantos dependentes entram acima dos 44') + '.')
 + BOX('!','Importante','O valor da tabela e a mensalidade. Em plano com coparticipacao, cada consulta ou exame usado tem uma '
       'cobranca a parte, que entra na fatura do mes seguinte. Somar as duas coisas antes de comparar com outra operadora e o '
       'unico jeito de comparar direito.')
 + H3('Coparticipacao na pratica em Divinopolis')
 + P('Divinopolis usa a tabela das demais pracas, entao a consulta eletiva sai por [demais_capitais_consultas_eletivas] e o exame '
     'simples por [demais_capitais_exames_simples]. O detalhe local importa: como consulta, exame de imagem e internacao ficam no '
     'mesmo complexo do Padre Liberio, o beneficiario tende a concentrar o uso na rede propria.')
 + P('Isso muda a conta na ponta do lapis. Quem usa muito a rede propria da cidade sente mais o efeito da coparticipacao do que '
     'quem so tem o plano por seguranca. A mecanica completa, com os dois modelos e os cenarios de uso, esta no '
     '<a href="https://tabelaplanos.com.br/tabela-precos-hapvida-coparticipacao-guia-completo/" style="color:#ff6b00;font-weight:600;">'
     'guia de valores de coparticipacao da Hapvida</a>.'))

# ---------------------------------------------------------------- S1
figura = ('<figure style="margin: 0 0 24px 0; padding: 0;"><img style="max-width: 70%; height: auto; border-radius: 12px; border: 1px solid #e2e8f0; '
 'display: block; margin: 0 auto;" title="Plano Hapvida Divinopolis: o complexo Santa Monica no Padre Liberio" src="[URL_DA_IMAGEM]" '
 'alt="Fachada de unidade de saude representando o plano Hapvida em Divinopolis, cidade onde hospital, centro clinico e servico de imagem da '
 'operadora ficam no mesmo endereco do bairro Padre Liberio" width="1080" height="1080" />'
 '<figcaption style="text-align: center; font-size: 14px; color: #718096; margin-top: 10px; font-style: italic;">'
 'Em Divinopolis a rede propria nao esta espalhada: esta concentrada num complexo unico.</figcaption></figure>')

s1 = SEC('por-que-divinopolis','#f8f9fa',
 H2('Por que Divinopolis e um caso diferente','Divinopolis tem 231.091 habitantes e e sede de uma regiao imediata de 20 municipios, entao a cidade atende muito mais gente do que a propria populacao. E por isso que, aqui, ter estrutura propria pesa mais do que ter lista longa de credenciados.')
 + P('Divinopolis tem 231.091 habitantes pelo Censo 2022 e e sede da regiao intermediaria e da regiao imediata que levam o nome dela, '
     'no Oeste de Minas. Na pratica, e ' + G('a cidade para onde a regiao vai quando precisa de saude') + ' — e isso pressiona a rede '
     'privada de um jeito que cidade do mesmo tamanho sem funcao de polo nao conhece.')
 + figura
 + BOX('R','Resumo Rapido','Rede propria concentrada num complexo unico no Padre Liberio, mais uma unidade de medicina preventiva no '
       'Centro. Hospital com plantao continuo de 24 horas registrado no CNES. Tabela de precos do grupo das demais pracas, nao a de '
       'Belo Horizonte.')
 + P('A economia sustenta essa demanda: o PIB municipal foi de R$ 8,33 bilhoes em 2021, segundo o IBGE. E uma praca de industria '
     'metalurgica, confeccao e comercio, com massa de trabalhadores com carteira, que e o publico natural do plano coletivo empresarial.')
 + ('<div class="grid4" style="display:flex!important;flex-wrap:wrap!important;gap:12px!important;margin-bottom:24px;">'
    '<div style="flex:1 1 160px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;padding:20px 16px;text-align:center;">'
    '<div class="v5-countup" data-v5-num="231091" style="font-size:28px;font-weight:900;color:#1a202c;margin-bottom:4px;">231.091</div>'
    '<div style="font-size:13px;color:#718096;">Habitantes (Censo 2022)</div></div>'
    '<div style="flex:1 1 160px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;padding:20px 16px;text-align:center;">'
    '<div style="font-size:28px;font-weight:900;color:#1a202c;margin-bottom:4px;">R$ 8,33 bi</div><div style="font-size:13px;color:#718096;">PIB municipal (2021)</div></div>'
    '<div style="flex:1 1 160px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;padding:20px 16px;text-align:center;">'
    '<div class="v5-countup" data-v5-num="20" style="font-size:28px;font-weight:900;color:#1a202c;margin-bottom:4px;">20</div>'
    '<div style="font-size:13px;color:#718096;">Municipios na regiao imediata</div></div>'
    '<div style="flex:1 1 160px!important;box-sizing:border-box!important;background:#ff6b00;border:none;border-radius:20px;padding:20px 16px;text-align:center;">'
    '<div style="font-size:28px;font-weight:900;color:#fff;margin-bottom:4px;">[divinopolis_menorvalor]</div>'
    '<div style="font-size:13px;color:rgba(255,255,255,0.85);">A partir de</div></div></div>')
 + P('Ser polo tem um efeito colateral que ninguem conta: a fila de exame e de consulta da cidade nao e so dos 231 mil moradores. '
     'Por isso, aqui, ' + G('ter estrutura propria vale mais do que ter lista grande de credenciados') + '. Dados demograficos e '
     'economicos em <a href="https://cidades.ibge.gov.br/brasil/mg/divinopolis/panorama" rel="nofollow noopener" target="_blank" '
     'style="color:#ff6b00;font-weight:600;">IBGE Cidades</a>.')
 + BOX('','DICA DRV','Na nossa experiencia atendendo o Oeste de Minas, a duvida que mais aparece nao e o preco: e onde '
       'a pessoa vai ser atendida. Em Divinopolis a resposta e curta, e vale conferir se ela serve para a sua rotina antes de '
       'assinar qualquer proposta.',badge=False))
open('/tmp/part2_ok','w').write('ok')

# ---------------------------------------------------------------- S3
s3 = SEC('planos-disponiveis','#fff8f3',
 H2('Como escolher o plano Hapvida em Divinopolis','Como a rede propria da cidade e uma so e todo mundo chega ao mesmo complexo do Padre Liberio, a escolha do plano em Divinopolis se decide por acomodacao em internacao e por modelo de coparticipacao, e nao por qual pedaco da rede voce alcanca.')
 + P('Numa capital, escolher plano e escolher qual pedaco da rede voce alcanca. Em Divinopolis nao e: a rede propria e uma so, e '
     'todo mundo chega no mesmo complexo. ' + G('O que muda de verdade e a acomodacao em internacao e o modelo de coparticipacao') + '.')
 + ('<div class="grid3" style="display:flex!important;flex-wrap:wrap!important;gap:16px!important;margin-bottom:24px;">'
    + card('AM','#ff6b00','Ambulatorial com coparticipacao','Consulta, exame e terapia na rede propria, com pagamento por uso. '
      'E a modalidade que a tabela desta pagina renderiza e a porta de entrada mais barata na cidade.',
      'Indicado para: quem quer custo mensal baixo','#ff6b00','#fff8f3')
    + card('AH','#2563eb','Ambulatorial mais hospitalar','Acrescenta internacao. Em Divinopolis, a internacao acontece no proprio '
      'complexo do Padre Liberio, que tem centro cirurgico registrado no CNES.','Indicado para: familia com risco cirurgico','#2563eb','#eff6ff')
    + card('PJ','#2563eb','Coletivo por CNPJ','A via de contratacao mais usada numa praca industrial. As regras de vidas minimas e '
      'de carencia mudam em relacao ao contrato de pessoa fisica.','Indicado para: empresa instalada na cidade','#2563eb','#eff6ff')
    + '</div>')
 + P('A modalidade ambulatorial e a base de quase toda a oferta de entrada, e e onde mora a maior confusao de quem compara plano '
     'so pelo preco. O que ela cobre e o que ela nao cobre esta detalhado no '
     '<a href="https://tabelaplanos.com.br/o-que-e-plano-ambulatorial-2/" style="color:#ff6b00;font-weight:600;">guia do plano '
     'ambulatorial da Hapvida</a>.')
 + BOX('!','Importante','A disponibilidade de cada linha comercial varia por praca e muda com o tempo. Antes de assinar, confirme na '
       'cotacao quais produtos estao abertos para Divinopolis na data — esta pagina descreve as modalidades e nao promete um catalogo fixo.'))

# ---------------------------------------------------------------- S4
s4 = SEC('rede-divinopolis','#fff',
 H2('A rede propria da Hapvida em Divinopolis','A Hapvida tem quatro unidades proprias em Divinopolis: hospital, centro clinico e servico de imagem na Rua Pedro Ferreira do Amaral, 33, no Padre Liberio, mais uma unidade de medicina preventiva na Avenida Sete de Setembro, 951, no Centro.')
 + P('A rede propria da operadora em Divinopolis, conforme consta no Guia Medico oficial em 01/09/2026, esta concentrada no bairro '
     'Padre Liberio, com uma unidade de medicina preventiva no Centro. ' + G('Nao ha rede espalhada por bairro nesta cidade') + ' — '
     'ha um complexo e um ponto de prevencao.')
 + H3('O complexo Santa Monica, no Padre Liberio')
 + ('<div style="background:#fff;border:2px solid #ff6b00;border-radius:20px;padding:28px 24px;margin-bottom:20px;box-shadow:0 2px 8px rgba(0,0,0,0.04);">'
    '<div style="display:flex!important;align-items:center!important;gap:12px!important;margin-bottom:14px;">'
    '<div style="width:40px;height:40px;background:#ff6b00;border-radius:10px;display:flex!important;align-items:center!important;'
    'justify-content:center!important;color:#fff;font-size:16px;font-weight:800;">HP</div>'
    '<h3 style="font-size:18px;font-weight:800;color:#1a202c;margin:0;">Hospital e Maternidade Santa Monica</h3></div>'
    '<p style="text-align:justify!important;font-size:14px;color:#4a5568;line-height:1.6;margin-bottom:12px;">Hospital geral proprio, '
    'registrado no CNES sob o codigo 2159376, com centro cirurgico e turno de atendimento continuo de 24 horas por dia, inclusive '
    'sabados, domingos e feriados. E a unidade que sustenta a urgencia e a internacao do plano na cidade.</p>'
    '<div style="background:#fff8f3;border-radius:8px;padding:10px 14px;font-size:13px;color:#ff6b00;font-weight:600;">'
    'Rua Pedro Ferreira do Amaral, 33 - Padre Liberio</div></div>')
 + ('<div class="grid2" style="display:flex!important;flex-wrap:wrap!important;gap:16px!important;margin-bottom:24px;">'
    + card('CC','#2563eb','Centro Clinico Santa Monica','Ambulatorio de consultas eletivas, no mesmo endereco do hospital. Funciona de '
      'segunda a quinta das 07h as 18h e na sexta ate as 17h.','Rua Pedro Ferreira do Amaral, 33 - Padre Liberio','#2563eb','#eff6ff','300px')
    + card('BI','#2563eb','Bioimagem Hospital Santa Monica','Servico proprio de imagem e diagnostico, dentro do complexo hospitalar. '
      'E o que permite fazer o exame no mesmo lugar da consulta.','Rua Pedro Ferreira do Amaral, 33 - Padre Liberio','#2563eb','#eff6ff','300px')
    + '</div>')
 + H3('A unidade fora do complexo')
 + ('<div class="grid2" style="display:flex!important;flex-wrap:wrap!important;gap:16px!important;margin-bottom:24px;">'
    + card('MP','#2563eb','Unidade de medicina preventiva no Centro','Unica unidade propria fora do Padre Liberio. Consta no Guia '
      'Medico oficial e tambem no nosso catalogo de rede, com nomes diferentes nas duas listas e o mesmo endereco.',
      'Avenida Sete de Setembro, 951 - Centro','#2563eb','#eff6ff','300px')
    + '</div>')
 + P('Fora dessas quatro, o atendimento passa por prestadores credenciados da cidade, que sao contratados e mudam com mais frequencia '
     'do que a rede propria. Nao listamos nenhum aqui sem confirmacao em fonte primaria — a diferenca entre proprio e credenciado esta '
     'no <a href="https://tabelaplanos.com.br/rede-credenciada-hapvida/" style="color:#ff6b00;font-weight:600;">guia da rede '
     'credenciada</a>, e a lista valida e sempre a do Guia Medico.')
 + BOX('!','Importante','Ao procurar as unidades de Divinopolis no site nacional da Hapvida, use o portal de Minas Gerais. O servico '
       'de imagem da cidade aparece, no filtro do portal nacional, sob o rotulo de outra cidade mineira, ainda que o endereco no corpo '
       'da pagina seja o de Divinopolis. Filtrar por cidade la pode fazer voce concluir que a unidade nao existe.')
 + P('Esse cuidado vale principalmente para exame de imagem, que e o servico mais procurado depois da consulta. Em Divinopolis o '
     'servico funciona dentro do complexo do Padre Liberio, e nao em endereco separado, o que reduz o risco de agendar no lugar '
     'errado. Registro publico das unidades em '
     '<a href="https://cnes.datasus.gov.br/" rel="nofollow noopener" target="_blank" style="color:#ff6b00;font-weight:600;">CNES/DataSUS</a>.'))
open('/tmp/part3_ok','w').write('ok')

# ---------------------------------------------------------------- S5
linhas_bairro = [
 ("Padre Liberio","Complexo Santa Monica","Hospital, ambulatorio e imagem no proprio bairro",True),
 ("Centro","Unidade de medicina preventiva","Prevencao no Centro; consulta e exame no Padre Liberio",False),
 ("Santa Clara","Complexo Santa Monica","Bairro com maior concentracao de servicos de saude depois do Centro",False),
 ("Niteroi","Complexo Santa Monica","Deslocamento pelo eixo Centro ate o Padre Liberio",False),
 ("Sao Jose","Complexo Santa Monica","Deslocamento pelo eixo Centro ate o Padre Liberio",False),
 ("Bom Pastor","Complexo Santa Monica","Deslocamento pelo eixo Centro ate o Padre Liberio",False),
 ("Catalao","Complexo Santa Monica","Deslocamento pelo eixo Centro ate o Padre Liberio",False),
 ("Liberdade","Complexo Santa Monica","Deslocamento pelo eixo Centro ate o Padre Liberio",False),
 ("Afonso Pena, Sidil e Tiete","Complexo Santa Monica","Bairros com rede publica proxima; a rede propria do plano segue no Padre Liberio",False),
 ("Interlagos, Esplanada e Serra Verde","Complexo Santa Monica","Bairros mais afastados do eixo central; conte o deslocamento na decisao",False),
]
tab = ('<div style="overflow-x:auto;margin-bottom:16px;"><table style="width:100%;border-collapse:collapse;font-size:15px;">'
 '<thead><tr style="background:linear-gradient(135deg,#1a1a2e,#16213e);">'
 '<th style="padding:12px 14px;color:#fff;text-align:left;font-weight:800;">Bairro ou regional</th>'
 '<th style="padding:12px 14px;color:#fff;text-align:left;font-weight:800;">Unidade propria de referencia</th>'
 '<th style="padding:12px 14px;color:#fff;text-align:left;font-weight:800;">O que considerar</th></tr></thead><tbody>')
for b,u,o,dest in linhas_bairro:
    bg = '#fff8f3' if dest else '#fff'
    peso = '800' if dest else '600'
    tab += (f'<tr style="background:{bg};border-bottom:1px solid #f1f5f9;">'
            f'<td style="padding:11px 14px;color:#1a202c;font-weight:{peso};">{b}</td>'
            f'<td style="padding:11px 14px;color:#4a5568;">{u}</td>'
            f'<td style="padding:11px 14px;color:#4a5568;">{o}</td></tr>')
tab += '</tbody></table></div>'

raiox = ('<div style="margin-bottom:24px;"><div style="font-size:18px;font-weight:700;color:#1a202c;margin-bottom:16px;">Raio-X da Cobertura</div>'
 '<div style="display:flex!important;align-items:flex-start!important;gap:10px!important;margin-bottom:12px;">'
 '<div style="width:14px;height:14px;flex-shrink:0!important;background:#ff6b00;border-radius:50%;margin-top:3px;"></div>'
 '<div><div style="font-size:14px;font-weight:700;color:#1a202c;">Cobertura propria completa</div>'
 '<p style="text-align:justify!important;font-size:13px;color:#718096;margin:4px 0 0;">Padre Liberio e Centro. Consulta, exame de imagem, '
 'internacao e prevencao resolvem dentro da cidade, em estrutura da propria operadora.</p></div></div>'
 '<div style="display:flex!important;align-items:flex-start!important;gap:10px!important;margin-bottom:12px;">'
 '<div style="width:14px;height:14px;flex-shrink:0!important;background:#d45500;border-radius:50%;margin-top:3px;"></div>'
 '<div><div style="font-size:14px;font-weight:700;color:#1a202c;">Demais bairros de Divinopolis</div>'
 '<p style="text-align:justify!important;font-size:13px;color:#718096;margin:4px 0 0;">Cobertos pelo mesmo complexo, com deslocamento. '
 'Nao ha unidade propria de bairro, entao a distancia ate o Padre Liberio entra na conta de quem mora longe do eixo central.</p></div></div>'
 '<div style="display:flex!important;align-items:flex-start!important;gap:10px!important;margin-bottom:12px;">'
 '<div style="width:14px;height:14px;flex-shrink:0!important;background:#e2e8f0;border-radius:50%;margin-top:3px;"></div>'
 '<div><div style="font-size:14px;font-weight:700;color:#1a202c;">Municipios vizinhos</div>'
 '<p style="text-align:justify!important;font-size:13px;color:#718096;margin:4px 0 0;">Divinopolis e o polo de saude da regiao, mas usar '
 'a rede daqui morando em outro municipio depende da abrangencia contratada. Confirme isso na cotacao, nao presuma.</p></div></div></div>')

s5 = SEC('cobertura-bairros','#f8f9fa',
 H2('De qual bairro voce chega mais rapido','O CNES registra estabelecimentos de saude em 57 bairros de Divinopolis, mas a rede propria do plano tem apenas dois enderecos: o complexo do Padre Liberio e o ponto do Centro. Para quem mora fora desse eixo, o deslocamento entra na decisao de contratar.')
 + P('O CNES registra estabelecimentos de saude em 57 bairros de Divinopolis, com forte concentracao no Centro. A rede propria do '
     'plano, porem, nao acompanha essa dispersao: ' + G('ela tem um endereco principal e um secundario') + '. A tabela abaixo traduz '
     'isso para a rotina de quem mora em cada regiao.')
 + tab
 + '<p style="text-align:justify!important;font-size:12px;color:#94a3b8;font-style:italic;margin-top:0;margin-bottom:20px;">Bairros conforme registro de estabelecimentos do CNES/DataSUS para o municipio de Divinopolis. A coluna de referencia indica a unidade propria da operadora, nao a unidade mais proxima em linha reta.</p>'
 + raiox
 + P('Quem mora nos bairros mais afastados do eixo central sente essa geografia principalmente em consulta de rotina e em exame '
     'agendado, que sao os atendimentos de maior frequencia. Para urgencia, o plantao de 24 horas do hospital resolve na propria '
     'cidade, sem depender de deslocamento para outra praca.')
 + P('Procedimento de alta complexidade que a cidade nao comporta costuma seguir para Belo Horizonte, onde a operadora tem rede '
     'propria bem maior — o mapa de la esta no <a href="https://tabelaplanos.com.br/plano-hapvida-belo-horizonte/" '
     'style="color:#ff6b00;font-weight:600;">guia do plano Hapvida em Belo Horizonte</a>.'))

# ---------------------------------------------------------------- S6
versus = ('<div class="grid2" style="display:flex!important;flex-wrap:wrap!important;gap:16px!important;margin-bottom:24px;">'
 '<div style="flex:1 1 300px!important;box-sizing:border-box!important;background:#fff;border:2px solid #ff6b00;border-radius:20px;overflow:hidden;">'
 '<div style="background:linear-gradient(135deg,#ff6b00,#e85d00);padding:14px 18px;font-size:17px;font-weight:900;color:#fff;">Hapvida em Divinopolis</div>'
 '<div style="padding:6px 18px 14px 18px;">'
 '<div style="padding:10px 0;border-bottom:1px solid #f1f5f9;"><div style="font-size:12px;color:#718096;font-weight:600;">Estrutura propria na cidade</div>'
 '<div style="font-size:15px;color:#1a202c;font-weight:800;">Hospital, ambulatorio e imagem</div></div>'
 '<div style="padding:10px 0;border-bottom:1px solid #f1f5f9;"><div style="font-size:12px;color:#718096;font-weight:600;">Distribuicao dos enderecos</div>'
 '<div style="font-size:15px;color:#1a202c;font-weight:800;">Concentrada: Padre Liberio e Centro</div></div>'
 '<div style="padding:10px 0;"><div style="font-size:12px;color:#718096;font-weight:600;">Internacao na propria cidade</div>'
 '<div style="font-size:15px;color:#1a202c;font-weight:800;">Sim, com centro cirurgico no CNES</div></div></div></div>'
 '<div style="flex:1 1 300px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;overflow:hidden;">'
 '<div style="background:linear-gradient(135deg,#1a1a2e,#16213e);padding:14px 18px;font-size:17px;font-weight:900;color:#fff;">Unimed em Divinopolis</div>'
 '<div style="padding:6px 18px 14px 18px;">'
 '<div style="padding:10px 0;border-bottom:1px solid #f1f5f9;"><div style="font-size:12px;color:#718096;font-weight:600;">Estrutura propria na cidade</div>'
 '<div style="font-size:15px;color:#4a5568;font-weight:700;">Nucleos de atencao e especialidades</div></div>'
 '<div style="padding:10px 0;border-bottom:1px solid #f1f5f9;"><div style="font-size:12px;color:#718096;font-weight:600;">Distribuicao dos enderecos</div>'
 '<div style="font-size:15px;color:#4a5568;font-weight:700;">Tres pontos proprios, todos no Centro</div></div>'
 '<div style="padding:10px 0;"><div style="font-size:12px;color:#718096;font-weight:600;">Modelo de internacao</div>'
 '<div style="font-size:15px;color:#4a5568;font-weight:700;">Apoiado em hospital da cidade</div></div></div></div></div>')

s6 = SEC('cenario-saude','#fff8f3',
 H2('O mercado de saude de Divinopolis','Divinopolis tem hospitais gerais de perfis distintos registrados no CNES, e o Santa Monica e o unico ligado a uma operadora verticalizada. A Unimed concorre na cidade com tres pontos proprios no Centro, de perfil ambulatorial e ocupacional.')
 + P('Divinopolis tem hospitais gerais de perfis bem distintos registrados no CNES: um hospital universitario ligado a UFSJ, casas '
     'com forte vinculo comunitario e o Santa Monica. ' + G('Desses, so o Santa Monica pertence a uma operadora verticalizada') + '. Essa e a diferenca estrutural que separa a Hapvida do resto da praca.')
 + versus
 + P('A comparacao acima nao e sobre qualidade de medicina, e sim sobre desenho. A Unimed opera em Divinopolis com tres pontos '
     'proprios registrados no CNES, todos no Centro: um nucleo de atencao a saude, um nucleo de especialidades e uma unidade de '
     'medicina ocupacional. E um modelo de porta ambulatorial no centro da cidade.')
 + P('A Hapvida faz o contrario: concentra tudo, inclusive internacao, num complexo fora do Centro. Para o morador, isso vira uma '
     'escolha pratica: resolver perto de casa no Centro, ou resolver tudo num lugar so. ' + G('Nao existe resposta certa, existe '
     'perfil de uso') + '.')
 + BOX('!','Importante','Este comparativo usa criterios verificaveis em registro publico: presenca de estrutura propria, distribuicao '
       'dos enderecos e modelo de internacao. Ele nao classifica operadora como melhor ou pior, e nao substitui a consulta ao Guia '
       'Medico de cada uma antes de decidir.')
 + P('O contraste fica mais claro quando se olha outra cidade mineira de porte parecido e fora da regiao metropolitana: o caso de '
     '<a href="https://tabelaplanos.com.br/plano-hapvida-uberlandia/" style="color:#ff6b00;font-weight:600;">Uberlandia</a> mostra '
     'como a mesma operadora se organiza quando a praca comporta mais de um endereco proprio.'))
open('/tmp/part4_ok','w').write('ok')

# ---------------------------------------------------------------- S7
s7 = SEC('como-contratar','#f8f9fa',
 H2('O que decidir antes de assinar em Divinopolis','Contratar o plano Hapvida em Divinopolis exige duas checagens que a cidade impoe: se a rota ate o complexo do Padre Liberio cabe na sua rotina, e qual abrangencia o contrato cobre para quem mora nos 20 municipios da regiao imediata.')
 + P('Contratar aqui tem uma pergunta a mais do que em capital: ' + G('a rota ate o Padre Liberio cabe na sua rotina?') + ' Se cabe, '
     'a estrutura concentrada joga a favor, porque consulta, exame e internacao saem no mesmo endereco. Se nao cabe, o plano vira '
     'fonte de atrito logo no primeiro agendamento.')
 + P('A segunda pergunta e sobre abrangencia. Divinopolis e sede de uma regiao imediata com 20 municipios, e quem mora em volta '
     'costuma assumir que o contrato feito na cidade vale para a regiao. Isso depende da abrangencia contratada e precisa ser '
     'confirmado na cotacao, item por item, antes da assinatura.')
 + BOX('P','Portabilidade','Quem ja tem plano em outra operadora e quer migrar sem recomecar carencia pode ter direito a '
       'portabilidade, dentro das regras da ANS. O prazo minimo no plano de origem, a janela de aniversario do contrato e a '
       'compatibilidade de faixa de preco sao definidos em norma nacional: confirme os tres antes de pedir o cancelamento do plano atual.')
 + P('As regras gerais de contratacao, documentacao e prazos sao nacionais, valem igual em qualquer praca e por isso nao se repetem '
     'aqui. O que muda em Divinopolis vem antes delas: a rota ate o Padre Liberio e a abrangencia que o contrato cobre para quem '
     'mora nos municipios vizinhos.')
 + P('Um recurso que muda a conta em cidade de rede concentrada e o atendimento a distancia: ele resolve parte das consultas de '
     'rotina sem deslocamento ate o Padre Liberio. Como funciona e quando vale a pena esta no '
     '<a href="https://tabelaplanos.com.br/teleconsulta-hapvida/" style="color:#ff6b00;font-weight:600;">guia da teleconsulta</a>.')
 + BOX('!','Importante','Todo plano de saude no Brasil segue a Lei 9.656/98 e a regulamentacao da ANS, incluindo prazos maximos de '
       'carencia e cobertura obrigatoria de urgencia e emergencia apos 24 horas. Nenhuma condicao comercial local pode reduzir esse '
       'piso legal. Consulte a <a href="https://www.gov.br/ans/pt-br" rel="nofollow noopener" target="_blank" '
       'style="color:#1e40af;font-weight:700;text-decoration:underline;">ANS</a> em caso de duvida.')
 + P('A DRV Corretora trabalha com Hapvida ha mais de dez anos e faz a cotacao com a tabela vigente da praca, sem custo para quem '
     'pede. O papel aqui e conferir se o desenho da rede de Divinopolis serve ao seu caso antes de voce assinar.'))

# ---------------------------------------------------------------- FAQ
perguntas = [
 ("Quais unidades proprias a Hapvida tem em Divinopolis?",
  "Sao quatro, conforme o Guia Medico oficial consultado em 01/09/2026: o Hospital e Maternidade Santa Monica, o Centro Clinico Santa "
  "Monica e a Bioimagem, os tres na Rua Pedro Ferreira do Amaral, 33, no Padre Liberio, mais uma unidade de medicina preventiva na "
  "Avenida Sete de Setembro, 951, no Centro. Fora dessas, o atendimento passa por prestadores credenciados."),
 ("O Hospital Santa Monica faz parte da rede propria da Hapvida?",
  "Sim. Ele e o hospital geral proprio da operadora na cidade, registrado no CNES sob o codigo 2159376, com centro cirurgico e turno "
  "de atendimento continuo de 24 horas por dia, inclusive fins de semana e feriados. E a unidade que sustenta a urgencia e a internacao "
  "do plano em Divinopolis."),
 ("O plantao do Padre Liberio vale em feriado e fim de semana?",
  "Vale. O CNES registra para o Hospital e Maternidade Santa Monica, codigo 2159376, turno de atendimento continuo de 24 horas por dia, "
  "inclusive sabado, domingo e feriado. Nao ha, na pesquisa desta pagina, confirmacao de pronto atendimento proprio autonomo em outro "
  "endereco da cidade: as demais unidades proprias tem horario comercial. Confirme o plantao vigente no Guia Medico antes de sair de casa."),
 ("O Hospital Santa Monica de Divinopolis atende gestante pela Hapvida?",
  "Aqui e preciso separar o nome do registro. A unidade se chama Hospital e Maternidade Santa Monica, mas o cadastro dela no CNES nao "
  "registra centro obstetrico nem centro neonatal, e a lista oficial de especialidades do bloco cirurgico nao traz obstetricia. Antes de "
  "contratar pensando em parto na cidade, confirme a cobertura obstetrica diretamente no Guia Medico e na operadora."),
 ("Da para fazer a consulta e o exame de imagem no mesmo endereco?",
  "Da. No complexo do Padre Liberio, na Rua Pedro Ferreira do Amaral, 33, o centro clinico e o servico de imagem dividem o endereco do "
  "hospital, entao consulta e exame saem sem segundo deslocamento. Em boa parte das outras pracas a operadora distribui esses servicos "
  "por enderecos diferentes, desenho que aparece no "
  "<a href=\'https://tabelaplanos.com.br/laboratorios-hapvida-capitais/\' style=\'color:#ff6b00;font-weight:600;\'>panorama de "
  "laboratorios da Hapvida</a>."),
 ("Qual guia medico devo consultar para ver a rede de Divinopolis?",
  "Use o portal da Hapvida de Minas Gerais. No filtro por cidade do portal nacional, o servico de imagem de Divinopolis aparece sob o "
  "rotulo de outra cidade mineira, ainda que o endereco no corpo da pagina seja o daqui. Quem filtra so pelo portal nacional pode "
  "concluir que a unidade nao existe."),
 ("Qual e o valor de entrada do plano Hapvida para quem mora em Divinopolis?",
  "Os planos comecam a partir de [divinopolis_menorvalor] por mes, e a tabela completa por faixa etaria esta no topo desta pagina. "
  "Divinopolis usa a tabela do grupo das demais pracas, nao a de Sao Paulo e Belo Horizonte, entao valores vistos em paginas de capital "
  "nao servem de referencia aqui."),
 ("Quanto se paga de coparticipacao por consulta em Divinopolis?",
  "A consulta eletiva sai por [demais_capitais_consultas_eletivas] e o exame simples por [demais_capitais_exames_simples], valores do "
  "grupo tarifario das demais pracas — o mesmo que vale para varias cidades do interior, nao um preco exclusivo de Divinopolis. A "
  "coparticipacao entra na fatura do mes seguinte ao uso."),
 ("O plano contratado em Divinopolis cobre atendimento em Belo Horizonte?",
  "Depende da abrangencia contratada, que e definida em contrato e nao pela cidade onde voce assina. Confirme esse item na cotacao "
  "antes de fechar, principalmente se voce ja sabe que vai precisar de procedimento de alta complexidade fora da cidade."),
 ("Quem mora na regiao de Divinopolis pode usar a rede da cidade?",
  "Divinopolis e sede de uma regiao imediata de 20 municipios e funciona como polo de saude para eles. Isso e geografia, nao cobertura "
  "automatica. O direito de usar a rede daqui morando em outro municipio vem da abrangencia do seu contrato, e precisa ser confirmado "
  "caso a caso na cotacao. Onde a operadora tem rede propria esta no "
  "<a href=\'https://tabelaplanos.com.br/hapvida-cidades/\' style=\'color:#ff6b00;font-weight:600;\'>mapa de cidades atendidas "
  "pela Hapvida</a>."),
 ("A Hapvida tem alguma unidade no Centro de Divinopolis?",
  "Tem uma: a unidade de medicina preventiva da Avenida Sete de Setembro, 951. Ela consta tanto no Guia Medico oficial quanto no nosso "
  "catalogo de rede, com nomes diferentes nas duas listas e o mesmo endereco. Consulta, exame e internacao seguem no Padre Liberio."),
 ("Preciso ir ate o Padre Liberio para tudo ou resolvo consulta no Centro?",
  "Para consulta eletiva, exame de imagem e internacao, o endereco e o complexo do Padre Liberio. O ponto do Centro tem perfil de "
  "medicina preventiva. Quem mora nos bairros mais afastados do eixo central deve contar esse deslocamento na decisao de contratar."),
 ("Cirurgia eletiva pelo plano Hapvida e feita em Divinopolis ou fora dela?",
  "O CNES confirma centro cirurgico no Hospital Santa Monica, e a lista oficial da unidade cita clinica medica, pediatria, ortopedia, "
  "ginecologia, neurologia, urologia, bucomaxilo e cirurgia geral e plastica. Procedimento fora dessa lista tende a ser encaminhado "
  "para outra praca, conforme a abrangencia do contrato."),
 ("A Unimed de Divinopolis tem rede propria como a do Padre Liberio?",
  "Os registros publicos mostram desenhos diferentes. A Unimed opera na cidade com tres pontos proprios no Centro, de perfil "
  "ambulatorial e ocupacional. A Hapvida concentra num complexo unico fora do Centro que inclui internacao. Sao modelos distintos, e a "
  "escolha depende de onde voce mora e de como usa o plano."),
 ("Empresa com CNPJ em Divinopolis pode contratar o plano empresarial?",
  "Sim, e numa praca industrial e de confeccao como esta o coletivo empresarial e a via mais usada. As regras de vidas minimas, "
  "documentacao e carencia do contrato coletivo sao nacionais e mudam em relacao ao contrato de pessoa fisica. Confira o "
  "<a href=\'https://tabelaplanos.com.br/como-contratar-hapvida/\' style=\'color:#ff6b00;font-weight:600;\'>passo a passo de "
  "contratacao da Hapvida</a> antes de reunir documento."),
]
faq_html = ('<section style="background:#fff;padding:20px 10px;border-radius:20px;margin-bottom:4px;border:1px solid #e2e8f0;" id="faq">'
 '<div style="display:inline-block;background:#ff6b00;color:#fff;font-size:12px;font-weight:700;padding:4px 12px;border-radius:6px;'
 'text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;">Perguntas Frequentes</div>'
 + H2('Perguntas de quem mora em Divinopolis','Quinze perguntas respondidas com o que as fontes primarias sustentam sobre Divinopolis: rede propria, valores do grupo das demais pracas, plantao de 24 horas e os pontos em que o registro publico nao confirma o que o nome da unidade sugere.')
 + ''.join(faq(i+1,q,a) for i,(q,a) in enumerate(perguntas)) + '</section>')
open('/tmp/part5_ok','w').write('ok')

# ---------------------------------------------------------------- CONCLUSAO
conclusao = ('<section style="background:linear-gradient(135deg,#f8fafc 0%,#f1f5f9 100%);padding:20px 10px;border-radius:20px;'
 'margin-bottom:4px;border-top:1px solid #e2e8f0;" id="conclusao">'
 + H2('Vale a pena o plano Hapvida em Divinopolis?','O plano Hapvida compensa em Divinopolis para quem circula pelo eixo Centro e Padre Liberio e quer consulta, exame e internacao no mesmo endereco. Compensa menos para quem mora longe desse eixo ou contrata pensando especificamente em parto na cidade.')
 + ('<div class="grid4" style="display:flex!important;flex-wrap:wrap!important;gap:12px!important;margin-bottom:24px;">'
    '<div style="flex:1 1 160px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;'
    'padding:20px 16px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.04);"><div style="font-size:28px;font-weight:900;color:#1a202c;'
    'margin-bottom:4px;">4</div><div style="font-size:13px;color:#718096;">Unidades proprias</div></div>'
    '<div style="flex:1 1 160px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;'
    'padding:20px 16px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.04);"><div style="font-size:28px;font-weight:900;color:#1a202c;'
    'margin-bottom:4px;">1</div><div style="font-size:13px;color:#718096;">Complexo resolve consulta, exame e internacao</div></div>'
    '<div style="flex:1 1 160px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;'
    'padding:20px 16px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.04);"><div style="font-size:28px;font-weight:900;color:#1a202c;'
    'margin-bottom:4px;">24h</div><div style="font-size:13px;color:#718096;">Plantao continuo no hospital</div></div>'
    '<div style="flex:1 1 160px!important;box-sizing:border-box!important;background:#ff6b00;border:none;border-radius:20px;'
    'padding:20px 16px;text-align:center;"><div style="font-size:28px;font-weight:900;color:#fff;margin-bottom:4px;">[divinopolis_menorvalor]</div>'
    '<div style="font-size:13px;color:rgba(255,255,255,0.85);">A partir de</div></div></div>')
 + P('Em Divinopolis, o plano Hapvida entrega uma coisa que a maioria das operadoras da praca nao entrega: consulta, exame de imagem e '
     'internacao dentro de estrutura propria, no mesmo endereco. ' + G('Isso e forca para quem valoriza resolver tudo num lugar so') +
     ' e limitacao para quem esperava unidade perto de casa em cada bairro.')
 + P('O plano compensa mais para quem mora no eixo Centro e Padre Liberio ou circula por ele, para familia que usa consulta e exame com '
     'frequencia, e para empresa da cidade que quer beneficio com internacao resolvida localmente. Compensa menos para quem mora longe '
     'do eixo central e nao quer deslocamento de rotina, e para quem contrata pensando especificamente em parto na cidade, item que o '
     'registro publico nao confirma.')
 + P('Os planos comecam a partir de <strong style="color:#ff6b00;">[divinopolis_menorvalor]</strong> por mes. A DRV Corretora monta a '
     'cotacao com a tabela vigente e sem custo. O mais util e pedir a simulacao ja sabendo de qual bairro voce sai.')
 + '<p style="text-align:justify!important;font-size:12px;color:#94a3b8;font-style:italic;margin-top:20px;margin-bottom:0;">Fontes: Guia '
   'Medico oficial Hapvida e portal Hapvida NDI Minas (consulta em 01/09/2026), CNES/DataSUS (estabelecimento 2159376), IBGE (Censo 2022, '
   'PIB municipal 2021 e regiao imediata 310065) e ANS. Dados atualizados em [mes_atual] de [ano_atual]. Precos sujeitos a alteracao '
   'conforme faixa etaria, modalidade e condicoes comerciais vigentes.</p></section>')

STICKY = ('<div class="v5-sticky-cta" style="position:fixed!important;bottom:0!important;left:0!important;right:0!important;z-index:99999!important;'
 'background:linear-gradient(135deg,#ff6b00,#e85d00)!important;box-shadow:0 -4px 16px rgba(0,0,0,0.18)!important;padding:10px 14px!important;'
 'align-items:center!important;justify-content:center!important;gap:10px!important;">'
 '<span style="color:#fff;font-size:14px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">Hapvida em Divinopolis a partir de <strong>[divinopolis_menorvalor]</strong></span>'
 '<a class="acao-abrir-popup" href="#" style="flex-shrink:0!important;display:inline-block;background:#fff;color:#e85d00!important;font-size:14px;'
 'font-weight:800;padding:8px 16px;border-radius:8px;text-decoration:none;">Cotar agora</a></div>')

STYLE = open('/tmp/style_block.txt').read()
SCRIPT = open('/tmp/script_block.txt').read()
SCRIPT5 = open('/tmp/script5_block.txt').read()

art = ('<article style="max-width:820px;margin:0 auto;">'
 + hero + s2a + FORM + toc + s2b + s1 + s3 + s4 + s5 + s6
 + FORM2 + s7 + faq_html + FORM2 + conclusao + STICKY + STYLE + SCRIPT + SCRIPT5 + '</article>')
open('/home/user/artigos/artigos/plano-hapvida-divinopolis/artigo.html','w',encoding='utf-8').write(art)
print('artigo.html escrito:',len(art),'caracteres')
