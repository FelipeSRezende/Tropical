/**
 * Created by maique on 20/04/17.
 */
$(document).ready(function () {
    get('/utils/obter_categorias/',{},function (dados) {
       var model = new NovoCatalogoVmodel(dados);
       ko.applyBindings(model);
    });
});