/**
 * Created by maique on 20/04/17.
 */

function NovoCatalogoVmodel(){
    var self = this;
    self.query = ko.observable();
    self.querysetProdutos = ko.observableArray();
    self.produtoSelecionado = ko.observable();


    self.nomeCatalogo = ko.observable();
    self.linkImagem = ko.observable();
    self.dataInicio = ko.observable();
    self.dataFim = ko.observable();
    self.descricao = ko.observable();
    self.produtos = ko.observableArray();

    // normal functions
    self.selecionarProduto = function (prod) {
      self.produtoSelecionado(prod);debugger;
    };

    self.adicionarAoCatalogo = function () {
      self.produtos.push(self.produtoSelecionado());
      self.limparItemSelecionado();
    };

    self.limparItemSelecionado = function(){
        self.query(null);
        self.produtoSelecionado(null);
        self.querysetProdutos.removeAll();
    };

    // computed functions
    self.temProduto = ko.computed(function () {
        return self.produtos().length > 0;
    });
    self.produtoFoiSelecionado = ko.computed(function () {
       return self.produtoSelecionado() ? true : false;
    });
    self.exibirFormPesquisa = ko.computed(function () {
       return self.produtoSelecionado() ? false : true;
    });

    // subscribe functions
    self.query.subscribe(function(value){
        if(self.query() && self.query().length >= 3){
            var contexto = {'query':self.query()};
            
            get('/catalogos/obter_produtos/',contexto,function (dados) {
               self.querysetProdutos(toListaDeProdutos(dados.produtos));
            });
        }
        else if(self.query() && self.query().length < 3){
            self.querysetProdutos.removeAll();
        }
    })
}

function ProdutoVmodel(produto) {
    var self = this;

    self.nome = ko.observable(produto.nome);
    self.referencia = ko.observable(produto.referencia);
    self.preco_normal = ko.observable(produto.preco);
    self.preco_promocional = ko.observable(produto.preco_promocional);
    self.linkImg = ko.observable(produto.img);
    self.categoria = ko.observable(produto.categoria);

}

function toListaDeProdutos(queryset){
    lista = [];
    queryset.forEach(function (element) {
        lista.push(new ProdutoVmodel(element));
    },this);

    return lista;
}
