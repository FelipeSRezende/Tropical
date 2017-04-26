/**
 * Created by maique on 21/04/17.
 */
$(document).ready(function () {

    var vmodel = new ProdutoVmodel();
    ko.applyBindings(vmodel);
    aplicandoInputMask();


    var query = $('#nome_produto');
    query.blur(function () {
       if(query.val().length != 0){
          verificarSeJaExisteProduto(query.val());
       }
    });
});


function verificarSeJaExisteProduto(query) {
   var msgError = $('#msgError');
   var btSalvar = $('#btnSalvar');

    get('/utils/ja_existe_produto_cadastrado/',{'query':query},function (dados) {
         if(dados.existe){
            msgError.removeClass('hidden');
            btSalvar.attr('disabled','disable');
         }else{
            msgError.addClass('hidden');
            btSalvar.removeAttr('disable');
         }
    });
}

function aplicandoInputMask() {
  $('#preco_original_produto').maskMoney();
  $('#preco_promocional').maskMoney();
}