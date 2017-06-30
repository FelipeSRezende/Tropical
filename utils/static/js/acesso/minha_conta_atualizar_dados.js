/**
 * Created by maique on 01/05/17.
 */
$(document).ready(function () {
    var cepField =  $('#id_cep');

    cepField.blur(function () {
        if(cepField.val().length > 0){
         encontrarCEP(cepField.val(),function (dados) {
             $('#id_logradouro').val(dados.logradouro);
             $('#id_bairro').val(dados.bairro);
             $('#id_municipio').val(dados.localidade);
             $('#id_estado').val(dados.uf);
         });
        }
    });
});

