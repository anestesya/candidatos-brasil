$(document).on("pageinit", "#index", function(event) {

  var render = [];

  for (e in Estados) {
    var estado = Estados[e];
    render.push(
      "<li>",
      "<a href='#'>",
      "<img src='/static/img/bandeiras_estados/", estado["sigla"],".png'>",
      "<h2>", estado["nome"], "</h2>",
      "</a>",
      "</li>"
    );
  }

  var listview = $(this).find('ul[data-role=listview]');
  listview.html(render.join(''));
  listview.listview('refresh');

  // verifica no webstorage se tiver estado salvo vai para tela de cargos
  if (!store.enabled) {
    alert('Local storage is not supported by your browser. Please disable "Private Mode", or upgrade to a modern browser.')
    return;
  }
  var user = store.get('user');

});


$(document).on("pageinit", "#cargos", function(event) {

});