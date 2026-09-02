const c = $input.first().json || {};
const ou = (v, alt) => (v === undefined || v === null) ? alt : v;
const LEITURA = ['buscar', 'listar', 'auditar_links'];
const leitura = LEITURA.indexOf(c.operacao) !== -1;
return [{ json: {
  gravado: false,
  ok: c.ok === true,
  erro: ou(c.erro, null),
  detalhe: ou(c.detalhe, null),
  postId: ou(c.postId, null),
  slug: ou(c.slug, null),
  operacao: ou(c.operacao, null),
  dados: ou(c.dados, null),
  total: ou(c.total, null),
  ocorrencias: ou(c.ocorrencias, null),
  contexto: ou(c.contexto, null),
  contextos: ou(c.contextos, null),
  ancora: ou(c.ancora, null),
  url: ou(c.url, null),
  campo: ou(c.campo, null),
  valorAtual: ou(c.valorAtual, null),
  valorNovo: ou(c.valorNovo, null),
  titulo: ou(c.titulo, null),
  status: ou(c.status, null),
  resumoAcao: ou(c.resumoAcao, null),
  tamanhoAntes: ou(c.tamanhoAntes, null),
  tamanhoDepois: ou(c.tamanhoDepois, null),
  aviso: c.ok !== true
    ? 'Nada foi alterado.'
    : (leitura
       ? 'Leitura: nada foi alterado no site.'
       : 'SIMULACAO: nada foi gravado. Reenvie com apply true para valer.')
} }];
