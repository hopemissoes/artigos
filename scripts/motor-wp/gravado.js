const salvo = $input.first().json || {};
const c = $('Conferir e Montar').first().json || {};
const b = salvo.body || {};
const gravou = salvo.statusCode === 200 || salvo.statusCode === 201;
const ou = (v, alt) => (v === undefined || v === null) ? alt : v;
return [{ json: {
  gravado: gravou,
  statusCode: salvo.statusCode,
  erro: gravou ? null : ('HTTP ' + salvo.statusCode + ' ao salvar: ' + JSON.stringify(b).slice(0, 400)),
  postId: ou(c.postId, ou(b.id, null)),
  slug: ou(c.slug, ou(b.slug, null)),
  operacao: ou(c.operacao, null),
  ocorrencias: ou(c.ocorrencias, null),
  contexto: ou(c.contexto, null),
  ancora: ou(c.ancora, null),
  url: ou(c.url, ou(b.link, null)),
  campo: ou(c.campo, null),
  valorAtual: ou(c.valorAtual, null),
  valorNovo: ou(c.valorNovo, null),
  titulo: ou(c.titulo, null),
  status: ou(b.status, ou(c.status, null)),
  resumoAcao: ou(c.resumoAcao, null),
  tamanhoAntes: ou(c.tamanhoAntes, null),
  tamanhoDepois: ou(c.tamanhoDepois, null),
  modified: ou(b.modified, null),
  aviso: 'O WordPress guardou revisao automatica; da para reverter pelo editor.'
} }];
