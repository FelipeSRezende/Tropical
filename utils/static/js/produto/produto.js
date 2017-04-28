/**
 * Created by maique on 21/04/17.
 */
$(document).ready(function () {

    //var vmodel = new ProdutoVmodel();
    //ko.applyBindings(vmodel);
    aplicandoInputMask();


    var nomeProduto = $('#id_nome');
    nomeProduto.blur(function () {
        if (nomeProduto.val().length != 0) {
            verificarSeJaExisteProduto(nomeProduto.val());
        }
    });

    var imgProduto = $('#id_img');
    imgProduto.blur(function () {
        console.log('entrou');
        checkLinkImgOnline(
            imgProduto.val(),
            function () {
                console.log('caiu no erro');
                $('#fotoProduto').attr('src', '');
                $('#fotoProduto').attr('alt', 'O link informado é Invalido. Por Favor tente outro.')
            },
            function () {
                console.log('caiu no sucesso');
                $('#fotoProduto').attr('src', imgProduto.val())
            }
        )
    });

});

function checkLinkImgOnline(link, callbackError, calbackOk) {
    var img = new Image();
    img.src = link;
    img.onload = calbackOk;
    img.onerror = callbackError;
}


function verificarSeJaExisteProduto(query) {
    var msgError = $('#msgError');
    var btSalvar = $('#btnSalvar');

    get('/utils/ja_existe_produto_cadastrado/', {'query': query}, function (dados) {
        if (dados.existe) {
            msgError.removeClass('hidden');
            btSalvar.attr('disabled', 'disabled');
        } else {
            msgError.addClass('hidden');
            btSalvar.removeAttr('disabled');
        }
    });
}

function aplicandoInputMask() {debugger;
    $('#id_preco').maskMoney();
    $('#id_preco_promocional').maskMoney();
}