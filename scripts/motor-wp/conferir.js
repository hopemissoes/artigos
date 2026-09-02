const req = $('Parametros').first().json || {};
const rota = $('Rota').first().json || {};
const resp = $input.first().json || {};
const SITE = 'https://tabelaplanos.com.br';
const API = SITE + '/wp-json/wp/v2/posts';
const falha = (erro, extra) => [{ json: Object.assign({ ok: false, aplicar: false, erro: erro }, extra || {}) }];
const txt = (v) => (v === undefined || v === null) ? '' : String(v).trim();

const OPS = ['substituir', 'link', 'conteudo', 'meta_title', 'meta_description', 'buscar', 'listar', 'criar', 'auditar_links'];
const op = txt(req.operacao);
if (OPS.indexOf(op) === -1) {
  return falha('operacao desconhecida: "' + op + '". Use uma de: ' + OPS.join(', ') + '.');
}

if (resp.statusCode !== 200) {
  const d = typeof resp.body === 'string' ? resp.body : JSON.stringify(resp.body || {});
  return falha('HTTP ' + resp.statusCode + ' ao consultar ' + (rota.urlBusca || '(sem url)'), { detalhe: d.slice(0, 400) });
}
const corpo = resp.body;

if (op === 'listar') {
  if (!Array.isArray(corpo)) return falha('a listagem nao voltou como lista', { detalhe: JSON.stringify(corpo || {}).slice(0, 400) });
  return [{ json: { ok: true, aplicar: false, operacao: op, total: corpo.length, dados: corpo.map(a => ({
    id: a.id,
    titulo: (a.title && (a.title.raw || a.title.rendered)) || null,
    slug: a.slug, link: a.link, status: a.status, data: a.date, modificado: a.modified
  })) } }];
}

if (op === 'auditar_links') {
  return [{ json: { ok: true, aplicar: false, operacao: op,
    total: Array.isArray(corpo) ? corpo.length : null, dados: corpo } }];
}

if (op === 'criar') {
  const titulo = txt(req.titulo);
  const conteudo = typeof req.conteudo === 'string' ? req.conteudo : '';
  const slug = txt(req.slug);
  if (!titulo.length) return falha('parametro titulo ausente ou vazio');
  if (!conteudo.length) return falha('parametro conteudo ausente ou vazio');
  const st = txt(req.status);
  const status = ['draft', 'publish', 'pending', 'private'].indexOf(st) !== -1 ? st : 'draft';
  const lista = Array.isArray(corpo) ? corpo : [];
  const dup = lista.filter(a => a && (slug
    ? a.slug === slug
    : txt((a.title && (a.title.raw || a.title.rendered)) || '').toLowerCase() === titulo.toLowerCase()));
  if (dup.length) {
    return falha('ja existe artigo com esse ' + (slug ? 'slug' : 'titulo') + ': id ' + dup[0].id + ' (status ' + dup[0].status + '). Nada foi criado.',
      { dados: dup.map(a => ({ id: a.id, slug: a.slug, status: a.status, link: a.link })) });
  }
  const body = { title: titulo, content: conteudo, status: status };
  if (slug.length) body.slug = slug;
  if (txt(req.resumo).length) body.excerpt = txt(req.resumo);
  const meta = {};
  if (txt(req.meta_titulo).length) meta.rank_math_title = txt(req.meta_titulo);
  if (txt(req.meta_descricao).length) meta.rank_math_description = txt(req.meta_descricao);
  if (Object.keys(meta).length) body.meta = meta;
  const cats = txt(req.categorias).split(',').map(s => Number(s.trim())).filter(n => !isNaN(n) && n > 0);
  if (cats.length) body.categories = cats;
  return [{ json: {
    ok: true, aplicar: req.apply === true, operacao: op,
    postId: null, slug: slug || null, titulo: titulo, status: status,
    tamanhoAntes: 0, tamanhoDepois: conteudo.length,
    urlSalvar: API, corpoSalvar: JSON.stringify(body),
    resumoAcao: 'criar "' + titulo + '" como ' + status + ' (' + conteudo.length + ' caracteres de corpo)'
  } }];
}

const post = corpo || {};
if (!post || !post.id) {
  return falha('post ' + req.id + ' nao encontrado ou resposta sem id', { detalhe: JSON.stringify(post).slice(0, 400) });
}
const metaAtual = post.meta || {};
const base = { postId: post.id, slug: post.slug };

if (op === 'buscar') {
  return [{ json: Object.assign({}, base, { ok: true, aplicar: false, operacao: op, dados: {
    id: post.id,
    titulo: (post.title && (post.title.raw || post.title.rendered)) || null,
    slug: post.slug, link: post.link, status: post.status,
    data: post.date, modificado: post.modified,
    resumo: (post.excerpt && (post.excerpt.raw || post.excerpt.rendered)) || '',
    rank_math_title: metaAtual.rank_math_title || '',
    rank_math_description: metaAtual.rank_math_description || '',
    tamanhoConteudo: (post.content && typeof post.content.raw === 'string') ? post.content.raw.length : null,
    conteudo: (post.content && (post.content.raw || post.content.rendered)) || ''
  } }) }];
}

if (op === 'meta_title' || op === 'meta_description') {
  const campo = op === 'meta_title' ? 'rank_math_title' : 'rank_math_description';
  const novo = txt(req.valor);
  if (!novo.length) return falha('parametro valor ausente ou vazio', base);
  const atual = metaAtual[campo] || '';
  if (atual === novo) {
    return falha('o campo ' + campo + ' ja tem exatamente esse valor. Nada a fazer.', Object.assign({ campo: campo, valorAtual: atual }, base));
  }
  const body = { meta: {} };
  body.meta[campo] = novo;
  return [{ json: Object.assign({}, base, {
    ok: true, aplicar: req.apply === true, operacao: op,
    campo: campo, valorAtual: atual, valorNovo: novo,
    urlSalvar: API + '/' + post.id, corpoSalvar: JSON.stringify(body),
    resumoAcao: campo + ': "' + atual + '" -> "' + novo + '" (' + novo.length + ' caracteres)'
  }) }];
}

if (!post.content || typeof post.content.raw !== 'string') {
  return falha('a resposta nao trouxe content.raw; context=edit exige credencial valida e a credencial nao autenticou', base);
}
const html = post.content.raw;
base.tamanhoAntes = html.length;

if (op === 'conteudo') {
  const novo = typeof req.conteudo === 'string' ? req.conteudo : '';
  if (!novo.length) return falha('parametro conteudo ausente ou vazio', base);
  const body = { content: novo };
  if (txt(req.resumo).length) body.excerpt = txt(req.resumo);
  return [{ json: Object.assign({}, base, {
    ok: true, aplicar: req.apply === true, operacao: op, tamanhoDepois: novo.length,
    urlSalvar: API + '/' + post.id, corpoSalvar: JSON.stringify(body),
    resumoAcao: 'SOBRESCREVER o corpo inteiro: ' + html.length + ' -> ' + novo.length + ' caracteres. Para trocar um trecho, use substituir.'
  }) }];
}

const OPACOS = ['script','style','a','h1','h2','h3','h4','h5','h6','title','textarea','iframe','code','pre'];

function mascaraSegura(s) {
  const n = s.length;
  const safe = new Uint8Array(n).fill(1);
  const prof = {};
  OPACOS.forEach(t => { prof[t] = 0; });
  const dentro = () => OPACOS.some(t => prof[t] > 0);
  const re = /<!--[\s\S]*?-->|<(\/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(\/?)>/g;
  let m, pos = 0;
  while ((m = re.exec(s)) !== null) {
    if (dentro()) { for (let i = pos; i < m.index; i++) safe[i] = 0; }
    for (let i = m.index; i < m.index + m[0].length; i++) safe[i] = 0;
    pos = m.index + m[0].length;
    if (m[0].slice(0, 4) === '<!--') continue;
    const fecha = m[1];
    const nome = (m[2] || '').toLowerCase();
    const auto = m[3];
    if (OPACOS.indexOf(nome) !== -1 && !auto) {
      if (fecha) { prof[nome] = Math.max(0, prof[nome] - 1); } else { prof[nome] = prof[nome] + 1; }
    }
  }
  if (dentro()) { for (let i = pos; i < n; i++) safe[i] = 0; }
  const sc = /\[[^\]\n]{1,120}\]/g;
  let c;
  while ((c = sc.exec(s)) !== null) { for (let i = c.index; i < c.index + c[0].length; i++) safe[i] = 0; }
  return safe;
}

function ocorrenciasSeguras(s, agulha) {
  const safe = mascaraSegura(s);
  const out = [];
  let i = s.indexOf(agulha);
  while (i !== -1) {
    let ok = true;
    for (let k = i; k < i + agulha.length; k++) { if (!safe[k]) { ok = false; break; } }
    if (ok) out.push(i);
    i = s.indexOf(agulha, i + 1);
  }
  return out;
}

function contexto(s, ini, fim) {
  return (s.slice(Math.max(0, ini - 130), ini) + ' >>>' + s.slice(ini, fim) + '<<< ' + s.slice(fim, fim + 130)).replace(/\s+/g, ' ');
}

if (op === 'substituir') {
  const find = req.find;
  const repl = req.repl;
  if (typeof find !== 'string' || !find.length) return falha('parametro find ausente ou vazio', base);
  if (typeof repl !== 'string') return falha('parametro repl ausente', base);
  const partes = html.split(find);
  const n = partes.length - 1;
  if (n === 0) return falha('a string procurada nao existe no post', Object.assign({ ocorrencias: 0 }, base));
  if (req.esperado !== undefined && req.esperado !== null && req.esperado !== '' && n !== Number(req.esperado)) {
    return falha('contagem divergente: esperava ' + req.esperado + ', achou ' + n + '. Nada foi alterado.', Object.assign({ ocorrencias: n }, base));
  }
  const novo = partes.join(repl);
  const i = html.indexOf(find);
  return [{ json: Object.assign({}, base, {
    ok: true, aplicar: req.apply === true, operacao: op, ocorrencias: n,
    contexto: contexto(html, i, i + find.length), tamanhoDepois: novo.length,
    urlSalvar: API + '/' + post.id, corpoSalvar: JSON.stringify({ content: novo })
  }) }];
}

if (op === 'link') {
  const frase = req.frase;
  const destino = String(req.destino || '').replace(/^\/+|\/+$/g, '');
  if (typeof frase !== 'string' || !frase.length) return falha('parametro frase ausente ou vazio', base);
  if (!destino.length) return falha('parametro destino ausente', base);
  const url = SITE + '/' + destino + '/';
  if (html.indexOf(destino) !== -1) {
    return falha('o post ja aponta para ' + destino + '. Regra da casa: um link por destino por pagina.', base);
  }
  const pos = ocorrenciasSeguras(html, frase);
  if (pos.length === 0) {
    return falha('a frase nao aparece em texto linkavel; pode estar so dentro de tag, heading, shortcode ou de outro link', Object.assign({ ocorrencias: 0 }, base));
  }
  if (pos.length > 1 && (req.ocorrencia === undefined || req.ocorrencia === null || req.ocorrencia === '')) {
    return falha(pos.length + ' ocorrencias em texto seguro. Escolha uma com o parametro ocorrencia (1 a ' + pos.length + ').', Object.assign({ ocorrencias: pos.length, contextos: pos.map(p => contexto(html, p, p + frase.length)) }, base));
  }
  const escolhida = (Number(req.ocorrencia) || 1) - 1;
  if (escolhida < 0 || escolhida >= pos.length) return falha('ocorrencia fora do intervalo: existem ' + pos.length, base);
  const alvo = pos[escolhida];
  const novo = html.slice(0, alvo) + '<a href="' + url + '">' + frase + '</a>' + html.slice(alvo + frase.length);
  return [{ json: Object.assign({}, base, {
    ok: true, aplicar: req.apply === true, operacao: op, ancora: frase, url: url,
    ocorrencias: pos.length, contexto: contexto(html, alvo, alvo + frase.length), tamanhoDepois: novo.length,
    urlSalvar: API + '/' + post.id, corpoSalvar: JSON.stringify({ content: novo })
  }) }];
}

return falha('operacao ' + op + ' sem tratamento', base);
