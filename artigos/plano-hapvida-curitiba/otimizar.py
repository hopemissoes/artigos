# -*- coding: utf-8 -*-
"""Otimizações da FASE 0 aplicadas ao artigo de Curitiba (v7.4).
Cada bloco cita o ACHADO que o motiva. Nenhum dado novo sem fonte no state file."""
import re, sys
s = open('artigo.html', encoding='utf-8').read()
orig = s
def sub(velho, novo, n=1, obrig=True):
    global s
    c = s.count(velho)
    if obrig and c < 1:
        sys.exit("NAO ENCONTRADO: %r" % velho[:90])
    s = s.replace(velho, novo, n)
    return c

P17 = 'style="text-align: justify!important; font-size: 17px; line-height: 1.9; margin-bottom: 16px;"'
GRIFO = ('class="destaque-laranja-suave" style="background-image: linear-gradient(120deg,'
 'rgba(255,107,0,0.22) 0%,rgba(255,133,51,0.22) 100%); background-repeat: no-repeat; '
 'background-position: 0 50%; background-size: 100% 100%; padding: 2px 6px; '
 'transition: background-size 1.2s ease-out;"')

# ── ACHADO 7 · dado YMYL sem fonte: contagem de leitos, salas e UTI ──────────
# checkpoint_verificar reprova contagem de leitos/salas/UTI. Regra do editor-chefe:
# SUAVIZAR, nunca apagar a tag mantendo a afirmação.
sub('O "flagship" da rede. 10 leitos UTI, 5 salas cirúrgicas, PS adulto e pediátrico 24h, '
    'centro de diagnóstico completo.',
    'O "flagship" da rede: UTI, centro cirúrgico, pronto-socorro adulto e pediátrico 24h e '
    'centro de diagnóstico no mesmo endereço.')
sub('O complexo opera com 10 leitos de UTI, 5 salas cirúrgicas, centro de diagnóstico integrado '
    'e pronto-socorro adulto e pediátrico 24h.',
    'O complexo opera com UTI, centro cirúrgico, centro de diagnóstico integrado e '
    'pronto-socorro adulto e pediátrico 24h.')

# ── ACHADO 7 · superlativo "única maternidade" sem fonte primária ────────────
# Substituído pelo fato defensável: o parto acontece na rede própria.
sub('Única maternidade própria de operadora em Curitiba. Obstetrícia 24h, UTI Neonatal com '
    '15 leitos (10 intensivos + 5 semi-intensivos).',
    'Também chamado de Hospital Santa Brígida no cadastro da rede. Obstetrícia 24h e UTI '
    'Neonatal na própria estrutura — o parto não depende de hospital credenciado.')
sub('A Maternidade Brígida é a única maternidade própria de operadora privada em Curitiba. '
    'Unimed e outras operadoras utilizam hospitais credenciados como Pequeno Príncipe e '
    'Santa Cruz para partos — na Hapvida, gestantes são atendidas integralmente na própria '
    'rede, com obstetrícia 24h e UTI Neonatal dedicada.',
    'A Maternidade Brígida — Hospital Santa Brígida no cadastro da rede — concentra o parto '
    'dentro da estrutura própria, na Rua Guilherme Pugsley, 1705, no Água Verde. A gestante '
    'faz pré-natal, parto e o pós no mesmo prontuário, sem passar por hospital de terceiros.')
sub('Apenas a Maternidade Brígida (Água Verde), única maternidade própria de operadora em '
    'Curitiba. UTI Neonatal com 15 leitos (10 intensivos + 5 semi-intensivos). Carência de '
    '300 dias para parto.',
    'A Maternidade Brígida, na Rua Guilherme Pugsley, 1705, no Água Verde, com obstetrícia '
    '24h e UTI Neonatal na própria estrutura. Carência de 300 dias para parto.')
sub('estrutura hospitalar completa com a única maternidade de operadora na cidade',
    'estrutura hospitalar própria com maternidade e UTI Neonatal no Água Verde')
sub('centro oncológico e a única maternidade de operadora na cidade',
    'centro oncológico e maternidade com UTI Neonatal na própria rede')

# ── ACHADO 7 · números da Unimed vindos de concorrente, não reconferidos ─────
sub('Enquanto concorrentes como Unimed operam majoritariamente com rede credenciada '
    '(4.700 médicos cooperados e 54 hospitais terceiros), a Hapvida',
    'Enquanto concorrentes como a Unimed operam majoritariamente com rede credenciada, '
    'a Hapvida')
sub('4.700 médicos, 54 hospitais', 'Rede credenciada ampla')

# ── ACHADO 4 · o "19+" passa a ser contável: 19 unidades NOMEADAS com endereço ─
sub('são 3 hospitais 24h, mais de 19 centros clínicos e a única maternidade de operadora da cidade.',
    'são <strong style="color: #ff8533;">3 hospitais 24h, 3 prontos atendimentos e 19 unidades '
    'próprias no total</strong>, cada uma com endereço aberto neste guia.')
sub('3 hospitais 24h, 19+ centros clínicos, centro oncológico e diagnóstico completo',
    '19 unidades próprias com endereço: 3 hospitais 24h, 3 prontos atendimentos, centro '
    'oncológico e diagnóstico completo')
sub('3 hospitais 24h, 19+ centros clínicos, centro oncológico e maternidade com UTI Neonatal na própria rede.',
    '3 hospitais 24h, 3 prontos atendimentos, centro oncológico e maternidade com UTI '
    'Neonatal — 19 unidades próprias ao todo.')
s = s.replace('19+ centros clínicos', '19 unidades próprias')
s = s.replace('19+ centros', '19 unidades próprias')

# ── ACHADO 4 · as 3 unidades do catálogo que faltavam no artigo ──────────────
# consultar_rede ids 478, 481, 482. "Clínica São Lourenço" já ranqueia em 4,67
# no GSC (6 impressões) num artigo que não a citava.
CARD = ('<div style="flex: 1 1 300px!important; box-sizing: border-box!important; background: #fff; '
 'border: 1px solid #e2e8f0; border-radius: 20px; padding: 28px 22px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">'
 '<div style="display: flex!important; align-items: center!important; gap: 12px!important; margin-bottom: 12px;">'
 '<div style="width: 40px; height: 40px; background: #2563eb; border-radius: 10px; display: flex!important; '
 'align-items: center!important; justify-content: center!important; color: #fff; font-size: 14px; '
 'font-weight: 800; flex-shrink: 0!important;">%s</div>'
 '<h3 style="font-size: 17px; font-weight: 800; color: #1a202c; margin: 0;">%s</h3></div>'
 '<p style="text-align: justify!important; font-size: 14px; line-height: 1.7; color: #718096; '
 'margin: 0 0 8px 0;">%s</p>'
 '<p style="text-align: justify!important; font-size: 14px; line-height: 1.7; color: #4a5568; '
 'margin: 0;">%s</p></div>')
NOVAS = ('<p style="text-align: justify!important; font-size: 16px; font-weight: 800; color: #1a202c; '
 'margin-bottom: 12px;">Três unidades que quase ninguém lista</p>'
 '<div class="grid3" style="display: flex!important; flex-wrap: wrap!important; gap: 16px!important; '
 'margin-bottom: 20px;">'
 + CARD % ('SL', 'Clínica São Lourenço',
   'Rua Coronel Brasilino Moura, 80 - São Lourenço, Curitiba',
   'Atendimento ambulatorial no São Lourenço, a poucos minutos do Boa Vista e do Juvevê — '
   'a alternativa de quem não quer descer até o Centro.')
 + CARD % ('BSA', 'Clínica Barão do Serro Azul',
   'Rua Barão do Serro Azul, 449 - São Francisco, Curitiba',
   'Segunda unidade no São Francisco, no mesmo bairro do Hospital Ônix Mateus Leme. '
   'Concentra consulta e retorno perto do hospital de referência.')
 + CARD % ('CO', 'Centro Clínico Colombo',
   'Rua Roberto Lambach Falavinha, 294 - Maracanã, Colombo',
   'Fica dentro de Colombo, não em Curitiba. Quem mora lá não precisa vir à capital '
   'para consulta e exame de rotina.')
 + '</div>')

# ── ACHADO 6 · bloco de pronto atendimento — a busca está em posição 2,29 ────
PA = ('<p style="text-align: justify!important; font-size: 16px; font-weight: 800; color: #1a202c; '
 'margin-bottom: 12px;">Onde fica o pronto atendimento da Hapvida em Curitiba</p>'
 '<p ' + P17 + '>Três unidades da rede própria operam como pronto atendimento na cidade, e são '
 'elas que respondem quando o problema não pode esperar consulta agendada: '
 '<span ' + GRIFO + '>Clínica Mercês, na Av. Manoel Ribas, 552, que funciona 24 horas</span>; '
 'Centro Clínico Boqueirão, na Av. Marechal Floriano Peixoto, 7477; e Clínica Pinheiro, na '
 'Av. Winston Churchill, 1654, no Pinheirinho. O pronto-socorro hospitalar adulto e pediátrico '
 'fica no Hospital Ônix Mateus Leme, no São Francisco.</p>'
 '<p ' + P17 + '>A diferença importa na hora de sair de casa: o pronto atendimento resolve o '
 'caso de menor complexidade perto de você, e o pronto-socorro do hospital é o que tem '
 'retaguarda de internação. As regras de urgência e emergência da operadora estão no '
 '<a style="color: #2563eb; text-decoration: none; font-weight: 600;" '
 'href="https://tabelaplanos.com.br/urgencia-e-emergencia-hapvida/">guia de urgência e '
 'emergência Hapvida</a>.</p>')

ANCORA = ('<p style="text-align: justify!important; font-size: 16px; font-weight: 800; color: #1a202c; '
          'margin-bottom: 12px;">Mais de 30 Especialidades Médicas Disponíveis</p>')
sub(ANCORA, PA + NOVAS + ANCORA)

# ── ACHADO 5 · a tabela mandava Colombo à capital tendo unidade na própria cidade ─
sub('Colombo / Campo Largo / Outros', 'Campo Largo / Almirante Tamandaré / Outros')
sub('>Araucária<', '>Colombo<', 1, obrig=False)
s = s.replace('CC Araucária', 'CC Colombo', 1)

# ── ACHADO 8 · links: tira o redirect e os destinos saturados, põe subutilizado ─
sub('https://tabelaplanos.com.br/coparticipacao-hapvida/',
    'https://tabelaplanos.com.br/tabela-precos-hapvida-coparticipacao-guia-completo/')
qv = 'https://tabelaplanos.com.br/programa-qualivida-hapvida/'
assert s.count(qv) == 3
i = s.find(qv); j = s.find(qv, i + 1)
s = s[:j] + 'https://tabelaplanos.com.br/plano-hapvida-sao-jose-dos-pinhais/' + s[j + len(qv):]
k = s.find(qv, i + 1)
s = s[:k] + 'https://tabelaplanos.com.br/plano-hapvida-londrina/' + s[k + len(qv):]

open('artigo.html', 'w', encoding='utf-8').write(s)
print('bytes: %d -> %d (%+d)' % (len(orig), len(s), len(s) - len(orig)))
