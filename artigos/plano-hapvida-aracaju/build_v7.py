# -*- coding: utf-8 -*-
"""Reformata o artigo de Aracaju (ordem v6) para a ordem v7.4.
Nao reescreve conteudo: recorta os blocos existentes e os remonta na ordem
canonica preco-primeiro + lead-heroi. As unicas edicoes de texto sao as
apontadas em EDICOES (transicoes quebradas pela reordenacao, ano fixo e
limpeza do wpautop no <style>/<script>)."""
import re

SRC = 'artigos/plano-hapvida-aracaju/fontes/artigo-original-v6.html'
OUT = 'artigos/plano-hapvida-aracaju/artigo.html'
s = open(SRC, encoding='utf-8').read()

# ------------------------------------------------------------------ recortes
ART_OPEN = s[0:144]
TOC_OLD  = s[2295:10770]
S1       = s[10770:17360]
PRECO    = s[17360:20858]          # secao de preco, sem o formulario
FORM1    = s[20858:20989]          # comentario + div do 1o [elementor-template]
TIPOS    = s[20989:27245]
COPART   = s[27245:31945]
REDE     = s[31945:44911]
HOSP     = s[44911:52614]
COBERT   = s[52614:60503]
COMPAR   = s[60503:66949]          # inclui o 2o [elementor-template] (CTA inter)
CARENC   = s[66949:71754]
TECNO    = s[71754:76589]
CONTRAT  = s[76589:82400]
FAQ      = s[82400:101535]         # inclui o 3o [elementor-template] (CTA final)
CONCL    = s[101535:105857]
TAIL     = s[105857:]

# ------------------------------------------------------- 1. LEAD-HEROI v7.4
# Passagem citavel e metricas saem do lead original e da S1 (10 pontos, 2007,
# 130 leitos no Grageru). Nenhum dado novo.
def metrica(n, rot):
    return ('<div><div style="font-size:20px;font-weight:900;color:#fff;">%s</div>'
            '<div style="font-size:12px;color:#94a3b8;">%s</div></div>' % (n, rot))

HEROI = (
 '<div class="v5-hero-conv" style="background:linear-gradient(135deg,#1a1a2e,#16213e);'
 'border-radius:20px;padding:28px 24px;margin-bottom:4px;">'
 '<div style="font-size:12px;font-weight:700;color:#ff8533;text-transform:uppercase;'
 'letter-spacing:1px;margin-bottom:6px;">Plano Hapvida em Aracaju</div>'
 '<div style="font-size:34px;font-weight:900;color:#fff;line-height:1.1;margin-bottom:18px;">'
 'A partir de <span style="color:#ff8533;">[aracaju_menorvalor]</span>/mês</div>'
 '<p style="text-align:justify!important;font-size:18px;line-height:1.7;color:#e2e8f0;'
 'margin-bottom:16px;">O plano Hapvida em Aracaju começa em '
 '<strong style="color:#ff8533;">[aracaju_menorvalor]</strong> por mês e é o menor '
 'valor entre as operadoras que vendem plano pessoa física na capital sergipana. '
 'A rede própria soma <strong style="color:#ff8533;">7 unidades com endereço</strong>, '
 'ancorados no Hospital e Maternidade Gabriel Soares, no Centro, em operação desde 2007 '
 '— com um novo hospital de 130 leitos anunciado no bairro Grageru.</p>'
 '<div class="v5-hero-metricas" style="display:flex!important;flex-wrap:wrap!important;'
 'gap:24px!important;margin-top:20px;padding-top:18px;border-top:1px solid rgba(255,255,255,0.15);">'
 + metrica('7', 'unidades próprias na cidade')
 + metrica('2007', 'Hospital Gabriel Soares, no Centro')
 + metrica('130', 'leitos do novo hospital, no Grageru')
 + '</div></div>\n')

# ------------------------------------------- 2. S2↑a — H2 + contexto + TABELA
# Corta a secao de preco no shortcode da tabela: o que vem depois dele
# (box Importante + paragrafo final) desce para a S2↑b, depois do sumario.
i_tab = PRECO.index('[aracaju_menortabela]') + len('[aracaju_menortabela]')
PRECO_A = PRECO[:i_tab] + '\n</section>\n'
resto   = PRECO[i_tab:]
resto   = resto[:resto.rindex('</section>')]          # tira o fecho antigo

# ano fixo -> shortcode (Regra 5b)
PRECO_A = PRECO_A.replace('Tabela de Preços Hapvida Aracaju 2026',
                          'Tabela de Preços Hapvida Aracaju [ano_atual]')

# transicao quebrada pela reordenacao: depois da analise vem a coparticipacao
resto = resto.replace(
    'A seguir, detalhamos cada tipo de plano disponível na capital sergipana.',
    'A seguir, você vê quanto custa cada uso do plano nas duas modalidades de '
    'coparticipação praticadas em Aracaju.')

PRECO_B = ('<section style="background: #fff; padding: 20px 10px; border-radius: 20px; '
           'margin-bottom: 4px;">\n' + resto.lstrip('\n') + '\n</section>\n')

# --------------------------------------- 3. formulario id="cotacao-1" pós-sumário
FORM1 = ('<!-- 1º Formulário — [v7.5] colado na TABELA, antes do sumário -->\n'
         '<div id="cotacao-1" style="margin-bottom: 4px;">[elementor-template id="11215"]</div>\n')

# ------------------------------------------------ 4. SUMÁRIO reordenado + CTA
_partes = TOC_OLD.split('<div class="toc-item"')
cab = _partes[0]
_itens = ['<div class="toc-item"' + x[:x.index('</div>') + len('</div>')] for x in _partes[1:]]
cabecalho_item = next(i for i in _itens if 'href=' not in i)
por_href = {}
for it in _itens:
    m = re.search(r'href="(#[^"]+)"', it)
    if m:
        por_href[m.group(1)] = it

ORDEM = ['#precos', 'CTA', '#coparticipacao', '#por-que-aracaju', '#tipos-planos',
         '#rede-propria', '#hospital-gabriel-soares', '#cobertura-regional',
         '#comparativo', '#carencias', '#tecnologia', '#contratacao', '#faq', '#conclusao']

BADGE = ('<span class="toc-badge" style="min-width: 28px; height: 28px; flex-shrink: 0!important; '
         'background: %s; border-radius: 8px; display: flex!important; align-items: center!important; '
         'justify-content: center!important; color: #fff; font-size: 13px; font-weight: bold;">%s</span>')
# Item de cotacao = BOTAO, conforme o template de `components.md` (TOC):
# badge "$" + link com fundo laranja em gradiente, texto branco, padding,
# border-radius e sombra. Texto laranja sozinho nao cumpre a regra 9.
CTA_ITEM = ('<div class="toc-item" style="display: flex!important; align-items: center!important; '
            'gap: 10px!important; padding: 0!important; margin: 0!important;">'
            + (BADGE % ('#ff6b00', '$')) +
            '<a href="#cotacao-1" style="display:inline-block;color:#fff!important;font-weight:800;'
            'font-size:15px;text-decoration:none;padding:6px 14px;'
            'background:linear-gradient(135deg,#ff6b00,#e85d00);border-radius:6px;'
            'box-shadow:0 4px 14px rgba(255,107,0,0.35);">Faça uma Cotação</a></div>')

novos, n = [], 0
for chave in ORDEM:
    if chave == 'CTA':
        novos.append(CTA_ITEM)
        continue
    it = por_href[chave]
    n += 1
    it = re.sub(r'(<span class="toc-badge"[^>]*>)\d+(</span>)', r'\g<1>%d\g<2>' % n, it)
    novos.append(it)

TOC = (cab + cabecalho_item + '\n' + '\n'.join(novos) + '\n</div>\n</section>\n')
TOC = TOC.replace('Tabela de Preços Hapvida Aracaju 2026',
                  'Tabela de Preços Hapvida Aracaju [ano_atual]')

# ------------------------------- 5. S1 recebe a fonte demográfica que vinha no lead
FONTE = ('<p style="text-align: justify!important; font-size: 14px; line-height: 1.7; '
         'color: #64748b; margin-bottom: 0;">Fonte demográfica: '
         '<a style="color: #2563eb; text-decoration: underline;" '
         'href="https://www.ibge.gov.br/cidades-e-estados/se/aracaju.html" target="_blank" '
         'rel="nofollow noopener">IBGE Cidades — Aracaju</a>.</p>\n')
S1 = S1[:S1.rindex('</section>')] + FONTE + '</section>\n'

# -------------------------------------- 6. conclusão: H2 deixa de ser H2 de preço
CONCL = CONCL.replace('Hapvida em Aracaju — Menor Preço, Rede em Expansão e Cobertura Nacional',
                      'Hapvida em Aracaju — Rede em Expansão e Cobertura Nacional')

# ------------------------------------------ 7. <style>/<script>: limpar o wpautop
# O original foi colado no editor visual: o wpautop injetou <br /> dentro do
# <style> e do <script> (o que quebra a folha de estilo e o JS inteiro) e
# embaralhou os comentarios de bloco. Aqui o rodape e remontado a partir do
# conteudo real, sem <br /> e com os comentarios refeitos.
TAIL = TAIL.replace('<br />\n', '\n').replace('<br />', '')
css = TAIL[TAIL.index('html{scroll-behavior'):TAIL.index('</style>')]
js  = TAIL[TAIL.index("document.addEventListener('DOMContentLoaded'"):TAIL.index('</script>')]
TAIL = ('<!-- ══════════════════════════════════════════════ -->\n'
        '<!-- BLOCO STYLE FINAL -->\n'
        '<!-- ══════════════════════════════════════════════ -->\n'
        '<style>\n' + css.strip() + '\n</style>\n'
        '<!-- ══════════════════════════════════════════════ -->\n'
        '<!-- BLOCO SCRIPT FINAL — INTERSECTION OBSERVER + FIX COTAÇÃO -->\n'
        '<!-- ══════════════════════════════════════════════ -->\n'
        '<script>\n' + js.strip() + '\n</script>\n\n</article>')

# ---- 8. <p> de corpo na tipografia da skill (18px / line-height 1.7) --------
def tipografia(x):
    return x.replace('font-size: 17px; line-height: 1.9;', 'font-size: 18px; line-height: 1.7;')

PRECO_A, PRECO_B, COPART, S1, TIPOS = map(tipografia, (PRECO_A, PRECO_B, COPART, S1, TIPOS))
REDE, HOSP, COBERT, COMPAR = map(tipografia, (REDE, HOSP, COBERT, COMPAR))
CARENC, TECNO, CONTRAT, FAQ, CONCL = map(tipografia, (CARENC, TECNO, CONTRAT, FAQ, CONCL))

# ---- 9. quebra de <p> acima de 480 chars (checkpoint_paragrafos) -----------
# Quebra em fronteira de frase. Nenhuma palavra e alterada, acrescentada ou
# removida: so entra o fecha/abre <p>.
QUEBRA_P = '</p>\n<p style="text-align: justify!important; font-size: 18px; line-height: 1.7; margin-bottom: 16px;">'

def quebrar(x, frase):
    """Fecha o <p> logo depois de `frase` e abre outro."""
    assert x.count(frase) == 1, frase[:50]
    return x.replace(frase, frase.rstrip() + QUEBRA_P)

TIPOS = quebrar(TIPOS, 'incluindo referências locais como o Hospital Primavera no Jardins. ')
TIPOS = quebrar(TIPOS, 'enquanto o Mix inclui hospitais e clínicas credenciados. ')
REDE  = quebrar(REDE, 'está concentrada no Hospital Gabriel Soares, no Centro. ')
HOSP  = quebrar(HOSP, 'endocrinologia, ginecologia/obstetrícia e pediatria. ')
CONCL = quebrar(CONCL, 'conseguem entregar com o mesmo custo. ')

# ---- 10. break visual na HS do Gabriel Soares (checkpoint_ritmo_visual) ----
# A quebra do <p> de especialidades deixou 6 <p> seguidos. Entra um H3 no ponto
# em que a secao muda de assunto (do hospital atual para o novo do Grageru).
H3_GRAGERU = ('<h3 style="font-size:19px;font-weight:800;color:#1a202c;margin:14px 0 8px 0;">'
              'O novo hospital do Grageru</h3>\n')
alvo = '<p style="text-align: justify!important; font-size: 18px; line-height: 1.7; margin-bottom: 16px;">O anúncio do novo hospital no Grageru'
assert HOSP.count(alvo) == 1
HOSP = HOSP.replace(alvo, H3_GRAGERU + alvo)

# ---- 11. nota de atualizacao: ano fixo -> shortcode (Regra 5b) -------------
assert CONCL.count('Dados de preços atualizados em 2026.') == 1
CONCL = CONCL.replace('Dados de preços atualizados em 2026.',
                      'Dados de preços atualizados em [mes_atual] de [ano_atual].')

# ---- 12. grifos animados: repor o que saiu do lead e subir para o minimo ----
# A v7.4 manda compensar no corpo o grifo que sai do heroi (sobre navy o grifo
# suave some). O original tinha 6 e o minimo da skill e 10. Aqui so se envolve
# texto que JA existe — nenhuma palavra e alterada.
GRIFO_INI = ('<span class="destaque-laranja-suave" style="background-image: '
             'linear-gradient(120deg,rgba(255,107,0,0.22) 0%,rgba(255,133,51,0.22) 100%); '
             'background-repeat: no-repeat; background-position: 0 50%; background-size: 100% 100%; '
             'padding: 2px 6px; transition: background-size 1.2s ease-out;">')

def grifar(bloco, trecho):
    assert bloco.count(trecho) == 1, trecho[:60]
    return bloco.replace(trecho, GRIFO_INI + trecho + '</span>')

S1     = grifar(S1, 'o mercado aracajuano é essencialmente um jogo de três players')
TIPOS  = grifar(TIPOS, 'o Hospital Primavera (referência no bairro Jardins) aparece como credenciado para planos Mix')
COBERT = grifar(COBERT, 'A rede própria da Hapvida em Aracaju está concentrada no eixo Centro–São José')
COMPAR = grifar(COMPAR, 'três opções com rede local: Hapvida, Unimed Sergipe e Plamed')
CONCL  = grifar(CONCL, 'menor mensalidade entre as operadoras que vendem plano individual')

# ---- 13. CORRECOES DA FASE 0 — achados 1 a 10 do RELATORIO-MELHORIAS ---------
# Base: consultar_rede (catalogo, 7 unidades) + consultar_saturacao_destinos +
# checkpoint_onpage + checkpoint_verificar. Nada aqui e estimativa.

def troca(bloco, de, para, n=1):
    assert bloco.count(de) == n, "esperava %d ocorrencia de: %s" % (n, de[:70])
    return bloco.replace(de, para)

# --- 13.1 contagem da rede: 10 -> 7 (achado 1) --------------------------------
TOC = troca(TOC, 'Rede Própria — 10 Pontos de Atendimento Mapeados',
                 'Rede Própria — 7 Unidades Mapeadas por Bairro')
REDE = troca(REDE, 'Rede Própria Hapvida em Aracaju — 10 Pontos de Atendimento',
                   'Rede Própria Hapvida em Aracaju — 7 Unidades por Bairro')
REDE = troca(REDE, '1 hospital, 4 clínicas e 4 centros diagnósticos distribuídos em 5 bairros da capital',
                   '1 hospital, 5 clínicas e 1 centro de diagnóstico distribuídos em 4 bairros da capital')
S1 = troca(S1, 'com ~10 unidades próprias', 'com 7 unidades próprias')
COBERT = troca(COBERT, 'As 10 unidades se distribuem em apenas 5 bairros',
                       'As 7 unidades se distribuem em apenas 4 bairros')
COPART = troca(COPART,
    'fica a menos de 2 km de 7 pontos de atendimento (hospital + 3 clínicas + 3 diagnósticos)',
    'fica a menos de 2 km de 6 das 7 unidades próprias (o hospital, quatro clínicas e o centro de diagnóstico)')
FAQ = troca(FAQ, 'expandiu a rede com 4 Hapclínicas, 4 centros de diagnóstico',
                 'expandiu a rede com cinco clínicas e um centro de diagnóstico próprio')
CONCL = troca(CONCL, 'rede própria com hospital 24h, 4 clínicas especializadas e 4 centros de diagnóstico',
                     'rede própria com hospital 24h, cinco clínicas e um centro de diagnóstico')
CONCL = troca(CONCL, '~10', '7')

# --- 13.2 os dois "Diagnósticos" sao servico, nao unidade (achado 1) ----------
# Os dois cards duplicam o endereco do hospital e da Hapclinica Aracaju. O que
# eles descreviam ja esta no texto das duas unidades ("parque diagnostico
# completo" e "laboratorio integrado"), entao nada de informacao se perde.
def card_dx(nome):
    """Recorta o card inteiro contando profundidade de <div> (o ultimo card do
    grid nao tem um proximo card para servir de delimitador)."""
    import re as _re
    i = REDE.index('>' + nome + '</h3>')
    ini = REDE.rindex('<div style="flex: 1 1 220px!important;', 0, i)
    prof = 0
    for m in _re.finditer(r'<div\b|</div>', REDE[ini:]):
        prof += 1 if m.group(0).startswith('<div') else -1
        if prof == 0:
            fim = ini + m.end()
            while REDE[fim:fim + 1] == '\n':
                fim += 1
            return REDE[ini:fim]
    raise ValueError('card nao fechou: ' + nome)

for nome in ('Diagnóstico Aracaju', 'Diagnóstico Gabriel Soares'):
    alvo = card_dx(nome)
    REDE = REDE.replace(alvo, '', 1)

# --- 13.3 unidade que faltava: Clinica Sao Jose, Tv. Juca Barreto (achado 2) --
# Catalogo id 176. So afirmo o que o catalogo traz: existe, e propria, fica no
# Sao Jose. Especialidades nao constam do catalogo — nao invento.
CARD_JUCA = (
 '<div style="flex: 1 1 220px!important; box-sizing: border-box!important; background: #fff; '
 'border: 1px solid #e2e8f0; border-radius: 20px; padding: 20px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">\n'
 '<div style="display: flex!important; align-items: center!important; gap: 8px!important; margin-bottom: 10px;">\n'
 '<div style="width: 28px; height: 28px; flex-shrink: 0!important; background: #2563eb; border-radius: 8px; '
 'display: flex!important; align-items: center!important; justify-content: center!important; color: #fff; '
 'font-size: 11px; font-weight: 800;">HC</div>\n'
 '<h3 style="font-size: 14px; font-weight: bold; color: #1a202c; margin: 0;">Clínica São José — Juca Barreto</h3>\n'
 '</div>\n'
 '<p style="font-size: 13px; line-height: 1.6; color: #4a5568; margin-bottom: 8px;">Sétima unidade própria da '
 'operadora na capital, a poucos quarteirões da Hapclínica Aracaju. As especialidades atendidas variam — '
 'confirme no Guia Médico oficial antes de agendar.</p>\n\n'
 '<div style="font-size: 12px; color: #718096;">Tv. Juca Barreto, 177 — São José</div>\n'
 '</div>\n')
_i = REDE.index('>Vida &amp; Imagem Centro</h3>')
_ini = REDE.rindex('<div style="flex: 1 1 220px!important;', 0, _i)
REDE = REDE[:_ini] + CARD_JUCA + REDE[_ini:]

# ---- 14. LINKS, BRIDGE DE TECNOLOGIA, H2 COM SECUNDARIA, DRV, FAQ -----------
# Achados 8, 9, 10, 11 e 12 do RELATORIO-MELHORIAS.

def A(url, texto):
    return '<a style="color: #2563eb; text-decoration: underline;" href="%s">%s</a>' % (url, texto)

def Aext(url, texto):
    return ('<a style="color: #2563eb; text-decoration: underline;" href="%s" '
            'target="_blank" rel="nofollow noopener">%s</a>' % (url, texto))

BASE = 'https://tabelaplanos.com.br/'

# --- 14.1 H2 passam a carregar keyword secundaria (achado 10) -----------------
HOSP = troca(HOSP, 'Hospital Gabriel Soares — 18 Anos de Operação no Centro de Aracaju',
                   'Hospital Hapvida Gabriel Soares — 18 Anos no Centro de Aracaju')
TOC = troca(TOC, 'Hospital Gabriel Soares — Referência Desde 2007',
                 'Hospital Hapvida Gabriel Soares — Referência Desde 2007')
COBERT = troca(COBERT, 'Cobertura por Região — Onde a Hapvida Atende em Aracaju',
                       'Cobertura por Região — Onde Ficam as Clínicas Hapvida em Aracaju')
TOC = troca(TOC, 'Cobertura por Região — Onde a Hapvida Atende',
                 'Cobertura por Região — Onde Ficam as Clínicas Hapvida')

# --- 14.2 links internos, priorizando destinos SUBUTILIZADOS (achado 8) -------
HOSP = troca(HOSP,
    'concentrando internações, cirurgias, partos e atendimentos de emergência',
    'concentrando internações, cirurgias, partos e ' +
    A(BASE + 'urgencia-e-emergencia-hapvida/', 'atendimentos de urgência e emergência'))
HOSP = troca(HOSP,
    'os beneficiários são encaminhados para a rede credenciada.',
    'os beneficiários são encaminhados para a rede credenciada. Já a coleta laboratorial de '
    'rotina fica na estrutura própria, como nas demais praças atendidas pela operadora — '
    'veja o ' + A(BASE + 'laboratorios-hapvida-capitais/', 'mapa dos laboratórios Hapvida por capital') + '.')
COBERT = troca(COBERT,
    'cobrindo uma faixa de aproximadamente 3 km entre o Centro histórico e os bairros adjacentes ao sul.',
    'cobrindo uma faixa de aproximadamente 3 km entre o Centro histórico e os bairros adjacentes '
    'ao sul — uma concentração maior que a de outras capitais, como mostra o levantamento de ' +
    A(BASE + 'clinicas-hapvida-por-capital/', 'clínicas Hapvida por capital') + '.')
COMPAR = troca(COMPAR,
    'Cada uma opera com modelo diferente',
    'É um mercado bem mais estreito que o de ' +
    A(BASE + 'plano-hapvida-maceio/', 'Maceió, a capital vizinha') +
    '. Cada uma opera com modelo diferente')
CONCL = troca(CONCL,
    'mas o anúncio do novo hospital de 130 leitos no Grageru sinaliza que a operadora está investindo para resolver os principais gargalos.',
    'mas o anúncio do novo hospital de 130 leitos no Grageru sinaliza que a operadora está '
    'investindo para resolver os principais gargalos — o mesmo movimento que já ocorreu em '
    + A(BASE + 'plano-hapvida-salvador2/', 'Salvador') + '.')

# --- 14.3 link externo nº 2: ANS (achado 8) ----------------------------------
CARENC = troca(CARENC,
    'A portabilidade é especialmente relevante no contexto de Aracaju',
    'As regras de prazo e de portabilidade são as da ' +
    Aext('https://www.gov.br/ans/pt-br', 'ANS') +
    ', iguais em todo o país. A portabilidade é especialmente relevante no contexto de Aracaju')

# --- 14.4 seção "Tecnologia e Atendimento Digital" vira bridge (achado 9) -----
# A tabela de migração da skill lista essa seção como ELIMINADA (100% nacional) e
# o banco a cataloga como overlap de risco médio. O que havia de local (o Qualivida
# operado na unidade da Gentil Tavares) foi preservado dentro da S7.
TECNO = ''
TOC_TECNO = [x for x in novos if '#tecnologia' in x]
assert len(TOC_TECNO) == 1
TOC = TOC.replace(TOC_TECNO[0] + '\n', '')
_k = [0]
def _renum_toc(m):
    _k[0] += 1
    return '%s%d</span>' % (m.group(1), _k[0])
TOC = re.sub(r'(<span class="toc-badge"[^>]*>)\d+</span>', _renum_toc, TOC)
BRIDGE_TEC = (
 '<p style="text-align: justify!important; font-size: 18px; line-height: 1.7; margin-bottom: 0;">'
 'Para quem mora na Zona de Expansão, na zona norte ou nos municípios da região metropolitana, '
 'os canais digitais evitam boa parte do deslocamento até o Centro: agendamento nas Hapclínicas '
 'de Aracaju, resultados do Vida &amp; Imagem e o programa Qualivida — operado presencialmente '
 'na unidade da Av. Gentil Tavares, no Getúlio Vargas — ficam no aplicativo. Como funciona a '
 + A(BASE + 'teleconsulta-hapvida/', 'teleconsulta 24h da Hapvida') + ' está no guia dedicado.</p>\n')
CONTRAT = CONTRAT[:CONTRAT.rindex('</section>')] + BRIDGE_TEC + '</section>\n'

# --- 14.5 menções à DRV: 13 -> 3 (achado 11) ---------------------------------
# Ficam: a Dica DRV da coparticipação (a mais operacional), o subtítulo da S7 e a
# conclusão. As outras duas caixas viram callout — o conteúdo permanece.
CALLOUT_INI = ('<div style="border-left:4px solid #ff6b00;padding:16px 20px;margin-bottom:20px;'
               'background:#fff8f3;border-radius:0 8px 8px 0;">'
               '<p style="text-align:justify!important;font-size:18px;color:#1a202c;line-height:1.6;'
               'margin:0;font-weight:600;font-style:italic;">')

def caixa_drv(bloco):
    import re as _re
    i = bloco.index('DICA DRV')
    ini = bloco.rindex('<div style="background: linear-gradient(135deg,#eff6ff', 0, i)
    prof = 0
    for m in _re.finditer(r'<div\b|</div>', bloco[ini:]):
        prof += 1 if m.group(0).startswith('<div') else -1
        if prof == 0:
            return ini, ini + m.end()
    raise ValueError('caixa DICA DRV nao fechou')

def drv_para_callout(bloco):
    import re as _re
    ini, fim = caixa_drv(bloco)
    caixa = bloco[ini:fim]
    corpo = _re.findall(r'<p[^>]*>(.*?)</p>', caixa, _re.S)[-1].strip()
    return bloco[:ini] + CALLOUT_INI + corpo + '</p></div>\n' + bloco[fim:]

S1 = drv_para_callout(S1)          # caixa do reajuste ANS 2025
CARENC = drv_para_callout(CARENC)  # caixa da migração Plamed
S1 = troca(S1, '<!-- Box Dica DRV (sem badge, apenas label) -->\n', '')
CARENC = troca(CARENC, '<!-- Box Dica DRV -->\n', '')
CARENC = troca(CARENC, ' Fale com a DRV para simular o cenário.', '')
CONTRAT = troca(CONTRAT,
    ' Pela DRV Corretora, o processo é acompanhado do início ao fim, com orientação sobre o melhor plano para o seu perfil.',
    '')
CONTRAT = troca(CONTRAT,
    'Preencha o formulário nesta página ou entre em contato com a DRV.',
    'Preencha o formulário nesta página.')
CONTRAT = troca(CONTRAT, ' A DRV acompanha o processo e comunica o resultado em até 48 horas.', '')
FAQ = troca(FAQ, ' O processo é feito via sistema da ANS e a DRV Corretora auxilia em cada etapa.',
                 ' O processo é feito via sistema da ANS.')

# --- 14.6 FAQ: 18 -> 15, cortando as três nacionais (achado 12) --------------
def tira_faq(bloco, pergunta):
    ini = bloco.index('<details', bloco.index(pergunta) - 1200)
    fim = bloco.index('</details>', ini) + len('</details>')
    while bloco[fim:fim + 1] == '\n':
        fim += 1
    novo = bloco[:ini] + bloco[fim:]
    assert pergunta not in novo, pergunta
    return novo

for q in ('Qual a diferença entre Nosso Plano e Mix em Aracaju?',
          'Como funciona a coparticipação total da Hapvida em Aracaju?',
          'A Hapvida tem plano empresarial em Aracaju a partir de quantas vidas?',
          'Qual o telefone da Hapvida em Aracaju?'):
    FAQ = tira_faq(FAQ, q)

# --- 14.7 links restantes na FAQ + tirar a URL de carência repetida ----------
REDE = troca(REDE, 'brinquedoteca e laboratório pediátrico para coleta infantil.',
    'brinquedoteca e laboratório pediátrico para coleta infantil. Veja a '
    + A(BASE + 'hapvida-rede-pediatrica/', 'rede pediátrica da Hapvida') + '.')
FAQ = troca(FAQ, ' <a href="https://tabelaplanos.com.br/plano-de-saude-hapvida-carencia">'
                 'Veja as regras completas.</a>', '')

# renumerar as perguntas que sobraram
import re as _re
_n = [0]
def _renum(m):
    _n[0] += 1
    return '%s%d. ' % (m.group(1), _n[0])
FAQ = _re.sub(r'(<span>)\d+\. ', _renum, FAQ)

# ---- 15. DADO YMYL: telefone e contagem de leitos (achado 14) ---------------
# checkpoint_verificar.py reprova telefone e "N leitos" por serem dados que
# mudam e que fonte secundaria nao confirma. Decisao, item a item:
#   · 130 leitos (Grageru)  -> FICA. E anuncio publico, datado (dez/2025), com
#     fonte registrada no state file, e e o dado prospectivo central do artigo.
#     A trava continua acusando — a decisao esta documentada no 00-ESTADO.md.
#   · 56 / 74 / 145 / 186 leitos -> SAEM. Nao ha fonte primaria: 56 e a capacidade
#     do Gabriel Soares em 2007, 74 e 145 sao hospitais de outras pracas e 186 e
#     uma soma projetada a partir do 56.
#   · telefones -> SAEM (mudam, e o CTA do artigo e o formulario).

REDE = troca(REDE, '>56 leitos</span>', '>Desde 2007</span>')
REDE = troca(REDE, ' | (79) 4002-3633', '')
HOSP = troca(HOSP, 'e nasceu com 56 leitos hospitalares, pronto-socorro separado',
                   'e nasceu com pronto-socorro separado')
HOSP = troca(HOSP, 'Primeira unidade da Hapvida em Sergipe. 56 leitos, PS 24h adulto/pediátrico',
                   'Primeira unidade da Hapvida em Sergipe. PS 24h adulto/pediátrico')
HOSP = troca(HOSP, 'Mais que dobra a capacidade hospitalar da Hapvida em Aracaju (de 56 para ~186 leitos).',
                   'Mais que dobra a capacidade hospitalar própria da Hapvida em Aracaju.')
HOSP = troca(HOSP, 'já inaugurou hospitais em Fortaleza (74 leitos), Manaus (145 leitos) e São Paulo',
                   'já inaugurou hospitais em Fortaleza, Manaus e São Paulo')
COMPAR = troca(COMPAR, 'Gabriel Soares (56 leitos) + Grageru (130, em implantação)',
                       'Gabriel Soares + Grageru (130 leitos, em implantação)')

# ---- 16. parágrafos que estouraram 480 chars com as edições acima -----------
HOSP = quebrar(HOSP, 'além de centro cirúrgico e maternidade. ')
COBERT = quebrar(COBERT, 'como mostra o levantamento de <a style="color: #2563eb; text-decoration: underline;" '
                         'href="https://tabelaplanos.com.br/clinicas-hapvida-por-capital/">clínicas Hapvida '
                         'por capital</a>. ')
CARENC = quebrar(CARENC, 'a migração entre elas é comum. ')

# ---- 17. ritmo visual da seção do Gabriel Soares ---------------------------
# A quebra do parágrafo de estrutura deixou 5 <p> seguidos (a linha do tempo no
# meio é quebra visual legítima, mas o tokenizador do script não a reconhece).
H3_ESTRUTURA = ('<h3 style="font-size:19px;font-weight:800;color:#1a202c;margin:14px 0 8px 0;">'
                'Estrutura e especialidades</h3>\n')
_alvo = ('<p style="text-align: justify!important; font-size: 18px; line-height: 1.7; '
         'margin-bottom: 16px;">O Gabriel Soares atende mais de 30 especialidades')
assert HOSP.count(_alvo) == 1
HOSP = HOSP.replace(_alvo, H3_ESTRUTURA + _alvo)

# ---- 18. repetição de "130 leitos" (10x) — fica o número onde ele informa ----
# Mantido no herói, na linha do tempo, no parágrafo do Grageru, na tabela
# comparativa e na FAQ que responde a pergunta direta. Nas outras cinco vezes o
# número não acrescenta nada e vira tique de repetição.
S1 = troca(S1, 'acaba de anunciar um novo hospital de 130 leitos no Grageru',
               'acaba de anunciar um novo hospital no Grageru')
COBERT = troca(COBERT, 'Medicina Preventiva no Getúlio Vargas + novo hospital de 130 leitos no Grageru',
                       'Medicina Preventiva no Getúlio Vargas + novo hospital no Grageru')
CARENC = troca(CARENC, 'quem está de olho no novo hospital de 130 leitos no Grageru',
                       'quem está de olho no novo hospital do Grageru')
CONCL = troca(CONCL, 'mas o anúncio do novo hospital de 130 leitos no Grageru sinaliza',
                     'mas o anúncio do novo hospital do Grageru sinaliza')
FAQ = troca(FAQ, 'em dezembro de 2025, anunciou um novo hospital de 130 leitos no Grageru. São quase duas décadas',
                 'em dezembro de 2025, anunciou um novo hospital no Grageru. São quase duas décadas')

# ---- 19. seção de coparticipação: parede de texto -> leitura escaneável -------
# Diagnostico: 5 <p> de corpo seguidos (~2.400 caracteres) e so entao uma caixa.
# Pior: tres deles (P4-P6) vieram com classes orfas do chat
# ("font-claude-response-body break-words ...") e SEM estilo inline — nao herdavam
# nem o justificado, nem o 18px, nem o line-height, e por isso os checkpoints de
# paragrafo e ritmo nao os enxergavam.
#
# O que entra de quebra visual: dois cards (total x parcial), uma faixa de tres
# valores por uso, um H3 e uma lista de decisao por bairro. Nenhum fato novo — o
# texto e o mesmo, reorganizado e encurtado. A MECANICA nacional da coparticipacao
# continua fora (territorio do pillar; o banco a cataloga como overlap de risco
# alto); aqui fica so o VALOR e o criterio local, que a v7 permite na city.

P_CORPO = ('<p style="text-align: justify!important; font-size: 18px; line-height: 1.7; '
           'margin-bottom: 16px;">')
GRIFO = ('<span class="destaque-laranja-suave" style="background-image: '
         'linear-gradient(120deg,rgba(255,107,0,0.22) 0%,rgba(255,133,51,0.22) 100%); '
         'background-repeat: no-repeat; background-position: 0 50%; background-size: 100% 100%; '
         'padding: 2px 6px; transition: background-size 1.2s ease-out;">')

def card_modalidade(sigla, titulo, texto, rodape):
    return ('<div style="flex: 1 1 300px!important; box-sizing: border-box!important; background: #fff; '
            'border: 1px solid #e2e8f0; border-radius: 20px; padding: 20px 18px; '
            'box-shadow: 0 2px 8px rgba(0,0,0,0.04);">'
            '<div style="display: flex!important; align-items: center!important; gap: 10px!important; '
            'margin-bottom: 10px;">'
            '<div style="width: 28px; height: 28px; flex-shrink: 0!important; background: #2563eb; '
            'border-radius: 8px; display: flex!important; align-items: center!important; '
            'justify-content: center!important; color: #fff; font-size: 11px; font-weight: 800;">'
            + sigla + '</div>'
            '<h3 style="font-size: 16px; font-weight: 800; color: #1a202c; margin: 0;">' + titulo + '</h3>'
            '</div>'
            '<p style="text-align: justify!important; font-size: 14px; line-height: 1.7; color: #4a5568; '
            'margin-bottom: 10px;">' + texto + '</p>'
            '<div style="font-size: 13px; font-weight: 700; color: #ff6b00;">' + rodape + '</div>'
            '</div>')

def valor(rotulo, shortcode):
    return ('<div style="flex: 1 1 160px!important; box-sizing: border-box!important; '
            'background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 14px 16px;">'
            '<div style="font-size: 20px; font-weight: 900; color: #ff6b00;">' + shortcode + '</div>'
            '<div style="font-size: 13px; color: #718096;">' + rotulo + '</div></div>')

def item(texto):
    return ('<li style="display:flex;align-items:flex-start;gap:10px;padding:8px 0;font-size:18px;'
            'color:#4a5568;line-height:1.7;">'
            '<span style="color:#ff6b00;font-weight:800;flex-shrink:0;">▸</span>'
            '<span>' + texto + '</span></li>')

MIOLO_COPART = (
 # abertura citável (leva o grifo que estava no parágrafo antigo)
 P_CORPO + 'Em Aracaju, escolher entre coparticipação total e parcial pesa mais no valor final do '
 'que a faixa etária nas faixas jovens. A total tem ' + GRIFO +
 'a menor mensalidade do mercado sergipano</span> e cobra por uso; a parcial inverte — '
 'mensalidade um pouco maior e copay menor a cada consulta ou exame.</p>\n'

 # cards: total × parcial
 '<div class="grid2" style="display: flex!important; flex-wrap: wrap!important; gap: 16px!important; '
 'margin-bottom: 20px;">'
 + card_modalidade('CT', 'Coparticipação total',
     'A menor mensalidade da praça. Em troca, você paga uma taxa a cada consulta, exame ou '
     'procedimento realizado.',
     'Compensa para quem usa pouco')
 + card_modalidade('CP', 'Coparticipação parcial',
     'Mensalidade um pouco maior, com o valor por uso reduzido. O gasto fica mais previsível '
     'mês a mês.',
     'Compensa para quem usa com frequência')
 + '</div>\n'

 # o dado forte e local: a isenção
 + P_CORPO + 'Nas duas modalidades, internações, cirurgias e partos no Hospital Gabriel Soares são '
 'isentos de coparticipação — maternidade e UTI neonatal incluídas. Com o hospital do Grageru, '
 'a isenção passa a valer para uma rede com o dobro da capacidade própria atual.</p>\n'

 # faixa de valores por uso
 '<p style="text-align: justify!important; font-size: 15px; font-weight: 700; color: #1a202c; '
 'margin-bottom: 10px;">O que se paga por uso na coparticipação total, em Aracaju:</p>\n'
 '<div class="grid3" style="display: flex!important; flex-wrap: wrap!important; gap: 12px!important; '
 'margin-bottom: 20px;">'
 + valor('Consulta eletiva', '[demais_capitais_consultas_eletivas]')
 + valor('Exame simples', '[demais_capitais_exames_simples]')
 + valor('Demais terapias', '[demais_capitais_demais_terapias]')
 + '</div>\n'
 '<p style="text-align: justify!important; font-size: 14px; line-height: 1.7; color: #64748b; '
 'margin-bottom: 20px;">Aracaju segue a Tabela 1 da Hapvida (demais capitais), com valores '
 'inferiores aos de São Paulo e Belo Horizonte. A lista completa de procedimentos está no guia '
 'de coparticipação.</p>\n'

 # decisão por bairro
 '<h3 style="font-size:19px;font-weight:800;color:#1a202c;margin:14px 0 8px 0;">'
 'Qual escolher, pelo seu bairro</h3>\n'
 '<ul style="list-style:none;padding:0;margin:0 0 20px 0;">'
 + item('<strong>Centro, São José ou Suíssa</strong> — a menos de 2 km de 6 das 7 unidades '
        'próprias. Uso frequente, a parcial tende a compensar.')
 + item('<strong>Zona Norte, Zona de Expansão ou região metropolitana</strong> — Nossa Senhora '
        'do Socorro, Barra dos Coqueiros e São Cristóvão dependem do Centro para quase tudo. '
        'Uso esporádico, a total sai melhor.')
 + '</ul>\n'

 # comparação local
 + P_CORPO.replace('margin-bottom: 16px;', 'margin-bottom: 20px;')
 + 'Comparar com as concorrentes exige atenção: a Unimed Sergipe vende linhas sem coparticipação, '
 'com mensalidade mais alta — parece mais caro de saída, mas dispensa o pagamento por uso. '
 'A Plamed trabalha com modelos mistos, conforme a linha.</p>\n'
)

_i = COPART.index('margin-bottom: 28px;"></div>') + len('margin-bottom: 28px;"></div>')
_j = COPART.index('<div style="background: linear-gradient(135deg,#eff6ff')
COPART = COPART[:_i] + '\n' + MIOLO_COPART + COPART[_j:]

# ------------------------------------------------------------------ montagem
partes = [ART_OPEN, HEROI, PRECO_A, FORM1, TOC, PRECO_B, COPART, S1, TIPOS,
          REDE, HOSP, COBERT, COMPAR, CARENC, TECNO, CONTRAT, FAQ, CONCL, TAIL]
out = ''.join(partes)
open(OUT, 'w', encoding='utf-8').write(out)
print('escrito:', OUT, len(out), 'chars (original:', len(s), ')')
