/**
 * Created by maique on 20/04/17.
 */

function NovoCatalogoVmodel(dados){
    var self = this;
    self.query = ko.observable();
    self.produtoSelecionado = ko.observable();
    self.categorias = ko.observableArray(dados.categorias);
    self.querysetProdutos = ko.observableArray();

    self.nomeCatalogo = ko.observable();
    self.linkImagem = ko.observable();
    self.dataInicio = ko.observable();
    self.dataFim = ko.observable();
    self.descricao = ko.observable();
    self.produtos = ko.observableArray();

    // normal functions
    self.selecionarProduto = function (prod) {
      self.produtoSelecionado(prod);
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

    self.addNovoProduto = function () {
      self.produtoSelecionado(new ProdutoVmodel());
    };

    self.salvarCatalogo = function(){
        alerta('Aguarde em breve será implementado isso...');
    };

    // computed functions
    self.temProduto = ko.computed(function () {
        return self.produtos().length > 0;
    });
    self.produtoFoiSelecionado = ko.computed(function () {
       return self.produtoSelecionado() ? true : false;
    });
    self.exibirFormPesquisa = ko.computed(function () {
       return self.produtoSelecionado()  ? false : true;
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
    self.id = ko.observable(produto ? produto.id : '0')
    self.nome = ko.observable(produto ? produto.nome : '');
    self.referencia = ko.observable(produto ? produto.referencia : '');
    self.preco_normal = ko.observable(produto ? produto.preco : '0.00');
    self.preco_promocional = ko.observable(produto ? produto.preco_promocional : '0.00');
    self.linkImg = ko.observable(produto ? produto.img : '');
    self.categoria = ko.observable(produto ? produto.categoria : {});

}

function toListaDeProdutos(queryset){
    lista = [];
    queryset.forEach(function (element) {
        lista.push(new ProdutoVmodel(element));
    },this);

    return lista;
}
