# -*- coding: utf-8 -*-
"""Converte as 4 seções de conteúdo NACIONAL em bridge + link, conforme a ação já
catalogada no banco (consultar_overlaps_doorway) para BH, SP, Fortaleza e Londrina."""
import re, sys
s = open('artigo.html', encoding='utf-8').read()
orig = s
P = ('<p style="text-align: justify!important; font-size: 18px; line-height: 1.9; '
     'margin-bottom: 16px;">')
A = '<a style="color: #2563eb; text-decoration: none; font-weight: 600;" href="%s">%s</a>'

def sub(v, n, obrig=True):
    global s
    if obrig and v not in s: sys.exit("NAO ENCONTRADO: %r" % v[:110])
    s = s.replace(v, n, 1)

def secao(sid):
    m = re.search(r'<section id="%s".*?</section>' % sid, s, re.S)
    if not m: sys.exit("secao %s nao achada" % sid)
    return m

def troca_na_secao(sid, velho, novo):
    global s
    m = secao(sid)
    sec = m.group(0)
    if velho not in sec: sys.exit("em #%s NAO achei %r" % (sid, velho[:90]))
    s = s[:m.start()] + sec.replace(velho, novo, 1) + s[m.end():]

def bloco(sec, ini, tag='div'):
    """Recorta um <div> equilibrado a partir de um índice dentro da seção."""
    prof, i = 0, ini
    for mm in re.finditer(r'<%s\b|</%s>' % (tag, tag), sec[ini:], re.I):
        prof += 1 if mm.group(0).lower().startswith('<' + tag) else -1
        if prof == 0:
            return sec[ini:ini + mm.end()]
    sys.exit("bloco nao fechou")

# ══════════════════════════════════════════════════════════════════════════
# 1 · #tecnologia — banco: "ELIMINAR — 1 frase no artigo + link pillar".
#     A seção inteira sobrevive à troca da cidade. Sai; vira bridge na S7.
# ══════════════════════════════════════════════════════════════════════════
m = secao('tecnologia')
ini = s.rfind('<!--', 0, m.start())
s = s[:ini] + s[m.end():]
sub('<div class="toc-item" style="display: flex!important; align-items: center!important; '
    'gap: 10px!important; padding: 0!important; margin: 0!important;"><span class="toc-badge" '
    'style="min-width: 28px; height: 28px; flex-shrink: 0!important; background: #ff6b00; '
    'border-radius: 8px; display: flex!important; align-items: center!important; '
    'justify-content: center!important; color: #fff; font-size: 13px; font-weight: bold;">10</span>'
    '<a style="color: #1a202c; font-weight: 600; font-size: 15px; text-decoration: none;" '
    'href="#tecnologia">Tecnologia e Teleconsulta</a></div>\n', '')

# a bridge entra na seção de contratação, ancorada no que é de Curitiba
BRIDGE_TEC = (P + 'Depois de contratado, o acompanhamento é digital: como a rede de Curitiba é '
  'própria, o exame feito no NotreLabs da Av. Nossa Senhora da Luz aparece no prontuário do '
  'médico do Hospital Ônix Mateus Leme sem pedido de cópia. Agendamento, autorização e '
  'teleconsulta ficam no app — o funcionamento detalhado está no '
  + A % ('https://tabelaplanos.com.br/teleconsulta-hapvida/', 'guia de teleconsulta da Hapvida')
  + '.</p>')
m = secao('contratacao')
fim = m.end() - len('</section>')
s = s[:fim] + BRIDGE_TEC + s[fim:]

# ══════════════════════════════════════════════════════════════════════════
# 2 · #carencias — banco: "Carências Oficiais (ANS) — tabela idêntica" = risco ALTO.
#     Saem os cards de prazo ANS, o box genérico de portabilidade e a lista Qualivida.
# ══════════════════════════════════════════════════════════════════════════
m = secao('carencias'); sec = m.group(0)
g = re.search(r'<div class="grid5"[^>]*>', sec)
cards = bloco(sec, g.start())                    # os 5 cards 24h/30d/180d/300d/24m
sec = sec.replace(cards, '', 1)
i = sec.find('border-left:4px solid')
if i < 0:
    i = sec.find('background: linear-gradient(135deg,#eff6ff', sec.find('Portabilidade') - 3000)
ini_box = sec.rfind('<div', 0, sec.find('Portabilidade'))
sec = sec.replace(bloco(sec, ini_box), '', 1)     # box "P Portabilidade" (regra ANS genérica)
j = sec.find('Todos os beneficiários têm acesso ao Programa Qualivida')
if j < 0: sys.exit("trecho Qualivida nao achado")
ini_q = sec.rfind('<p', 0, j)
fim_q = sec.rfind('</p>') + 4                     # da abertura do Qualivida até o fim da seção
resto = sec[ini_q:sec.rfind('</section>')]
NOVO_FIM = (P + 'Quem migra de outra operadora em Curitiba costuma entrar por portabilidade: '
  'com dois anos de plano anterior e a carta de permanência em dia, a carência não recomeça. '
  'Os prazos oficiais, as isenções para PME e MEI e as situações especiais estão no '
  + A % ('https://tabelaplanos.com.br/plano-de-saude-hapvida-carencia/',
         'guia de carências e portabilidade') + '. O '
  + A % ('https://tabelaplanos.com.br/programa-qualivida-hapvida/', 'Programa Qualivida')
  + ', de medicina preventiva, atende em Curitiba no Centro de Qualidade de Vida, na Rua XV '
    'de Novembro, 556, e não tem carência.</p>')
sec = sec[:ini_q] + NOVO_FIM + sec[sec.rfind('</section>'):]
s = s[:m.start()] + sec + s[m.end():]

# o link de carências que já existia no meio da seção vira texto (URL 1x por artigo)
troca_na_secao('carencias',
  A % ('https://tabelaplanos.com.br/plano-de-saude-hapvida-carencia/',
       'Guia Completo de Carências Hapvida'),
  'guia oficial de carências')

# ══════════════════════════════════════════════════════════════════════════
# 3 · #tipos-planos — banco: "vira S3 com produtos locais reais, não modalidades ANS".
#     Os 3 cards eram segmentação ANS pura. Trocados pelas formas de contratação
#     realmente vendidas em Curitiba (campo `produtos` do artigo no banco).
# ══════════════════════════════════════════════════════════════════════════
CARD = ('<div style="flex: 1 1 220px!important; box-sizing: border-box!important; background: #fff; '
 'border: %s; border-radius: 20px; padding: 28px 22px;">'
 '<div style="width: 40px; height: 40px; background: %s; border-radius: 10px; display: flex!important; '
 'align-items: center!important; justify-content: center!important; color: #fff; font-size: 16px; '
 'font-weight: 800; margin-bottom: 12px;">%s</div>'
 '<h3 style="font-size: 17px; font-weight: 800; color: #1a202c; margin: 0 0 8px 0;">%s</h3>'
 '<p style="text-align: justify!important; font-size: 14px; line-height: 1.7; color: #4a5568; '
 'margin: 0 0 12px 0;">%s</p>'
 '<div style="background: %s; border-radius: 8px; padding: 8px 12px; font-size: 13px; color: %s; '
 'font-weight: bold;">%s</div></div>')
m = secao('tipos-planos'); sec = m.group(0)
g = re.search(r'<div class="grid3"[^>]*>', sec)
antigos = bloco(sec, g.start())
novos = ('<div class="grid3" style="display: flex!important; flex-wrap: wrap!important; '
 'gap: 16px!important; margin-bottom: 20px;">'
 + CARD % ('2px solid #ff6b00', '#ff6b00', 'EMP', 'Empresarial (CNPJ ou MEI)',
   'A porta de entrada mais barata em Curitiba, a partir de 2 vidas. É por aqui que entra a '
   'maior parte das empresas do Batel e da Cidade Industrial, sob a marca GNDISul.',
   '#fff8f3', '#ff6b00', 'Melhor preço na praça')
 + CARD % ('1px solid #e2e8f0', '#2563eb', 'ADE', 'Por adesão',
   'Via entidade de classe — CAEEPP, Mais Comerciários e ASPROFI operam no Paraná. Valor '
   'intermediário, sem exigir CNPJ próprio.',
   '#eff6ff', '#2563eb', 'Para profissional filiado')
 + CARD % ('1px solid #e2e8f0', '#2563eb', 'PF', 'Individual ou familiar',
   'Contratação direta, sem vínculo com empresa ou entidade. Valor mais alto e declaração de '
   'saúde obrigatória, mas é o único que ninguém pode cancelar por desligamento.',
   '#eff6ff', '#2563eb', 'Para quem não tem CNPJ')
 + '</div>')
sec = sec.replace(antigos, novos, 1)
sec = sec.replace('Modalidades por abrangência e tipo de contratação',
                  'As três formas de contratar em Curitiba, e para quem cada uma serve', 1)
sec = sec.replace('A Hapvida oferece planos segmentados por abrangência de cobertura e tipo de '
  'contratação. Todos os planos incluem alguma modalidade de coparticipação. Confira as três '
  'principais modalidades disponíveis em Curitiba:',
  'Em Curitiba a Hapvida vende sob a marca GNDISul, e o que muda o preço não é só a cobertura: '
  'é o vínculo pelo qual você entra. As três portas abaixo atendem a mesma rede própria — os '
  '3 hospitais e as 19 unidades — mas custam valores diferentes.', 1)
s = s[:m.start()] + sec + s[m.end():]

# ══════════════════════════════════════════════════════════════════════════
# 4 · #coparticipacao — mecânica nacional sai; o ângulo local fica.
#     Sai também o preço fixo da Unimed (a skill proíbe R$ hardcoded) e o
#     market share de 33%, que está em `nao_encontrado` no state file.
# ══════════════════════════════════════════════════════════════════════════
troca_na_secao('coparticipacao',
 'Esse é um dos diferenciais competitivos mais relevantes no mercado curitibano: a Unimed '
 'Curitiba, que detém 33% do mercado, não opera no modelo de coparticipação da mesma forma — '
 'seus planos têm mensalidades a partir de R$ 160 sem taxa por uso, mas sem a flexibilidade '
 'de escolher entre parcial e total.',
 'É um diferencial de praça: a Unimed Curitiba, principal concorrente local, não trabalha o '
 'modelo de coparticipação da mesma maneira, então quem usa pouco o plano não consegue lá a '
 'troca de mensalidade menor por taxa de uso.')
troca_na_secao('coparticipacao',
 'Na Hapvida/Clinipam, essa escolha existe e pode representar economia significativa dependendo '
 'do perfil de uso. Internações e cirurgias são sempre isentas de coparticipação, independente '
 'da modalidade escolhida.',
 'Na Hapvida/Clinipam essa escolha existe, e o que decide não é a regra — é a sua distância até '
 'a unidade.')
sub('Internações e cirurgias são SEMPRE isentas de coparticipação',
    'Em Curitiba, a conta muda conforme o bairro', False)

open('artigo.html', 'w', encoding='utf-8').write(s)
print('bytes: %d -> %d (%+d)' % (len(orig), len(s), len(s) - len(orig)))
