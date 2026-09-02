const r = $input.first().json || {};
const SITE = 'https://tabelaplanos.com.br';
const API = SITE + '/wp-json/wp/v2';
const op = String(r.operacao || '').trim();
const enc = encodeURIComponent;
const num = (v, d) => (v === undefined || v === null || v === '' || isNaN(Number(v))) ? d : Number(v);
const txt = (v, d) => (v === undefined || v === null || String(v).trim() === '') ? d : String(v).trim();
const faixa = (v, min, max) => Math.min(max, Math.max(min, v));

let url;
if (op === 'listar') {
  const q = ['per_page=' + faixa(num(r.per_page, 10), 1, 100),
             'orderby=' + enc(txt(r.orderby, 'date')),
             'order=' + enc(txt(r.order, 'desc')),
             'context=edit'];
  const s = txt(r.busca, '');
  if (s) q.push('search=' + enc(s));
  url = API + '/posts?' + q.join('&');
} else if (op === 'auditar_links') {
  const q = ['orderby=' + enc(txt(r.orderby, 'internal_in')),
             'order=' + enc(txt(r.order, 'asc')),
             'per_page=' + faixa(num(r.per_page, 20), 1, 100)];
  url = SITE + '/wp-json/drv/v1/audit-links?' + q.join('&');
} else if (op === 'criar') {
  const slug = txt(r.slug, '');
  const chave = slug ? ('slug=' + enc(slug)) : ('search=' + enc(txt(r.titulo, 'zzz-sem-titulo')));
  url = API + '/posts?' + chave + '&status=any&per_page=5&context=edit';
} else {
  url = API + '/posts/' + num(r.id, 0) + '?context=edit';
}
return [{ json: Object.assign({}, r, { urlBusca: url }) }];
