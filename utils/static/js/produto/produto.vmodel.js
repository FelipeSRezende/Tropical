/**
 * Created by maique on 21/04/17.
 */
function ProdutoVmodel() {
    var self = this;

    self.id = ko.observable();
    self.nome = ko.observable();
    self.referencia = ko.observable();
    self.preco_normal = ko.observable();
    self.preco_promocional = ko.observable();
    self.linkImg = ko.observable();
    self.categoria = ko.observable({});
    self.categorias = ko.observableArray();

    //atributos auxiliares
    self.exibirFormCategoria = ko.observable(false);
    self.nomeNovaCategoria = ko.observable();
    self.nomeObrigatorio = ko.observable(false);
    self.referenciaObrigatorio = ko.observable(false);
    self.precoNormalObrigatorio = ko.observable(false);
    self.linkImgObrigatorio = ko.observable(false);
    self.categoriaObrigatorio = ko.observable(false);
    self.produtos = ko.observableArray();
    self.query = ko.observable();

    //atributos de paginação
    self.pagina_atual = ko.observable(1);
    self.total_de_paginas = ko.observable();
    self.paginas = ko.observableArray();


    // funções normal
    self.obterCategorias = function () {
        get('/utils/obter_categorias/', {}, function (dados) {
            self.categorias(dados.categorias);
        });
    };

    self.pesquisar = function () {
        self.pagina_atual(1);
        self.obterProdutos();
    };

    self.obterProdutos = function () {
        contexto = {'query':self.query(),'pagina':self.pagina_atual()};

        get('/produtos/filtrar_produto_paginado/',contexto,function (dados) {
           self.produtos(dados.produtos);
           self.total_de_paginas(dados.total_de_paginas);

           self.paginas.removeAll();
           for(var i = 1 ; i <= self.total_de_paginas() ; i++){
               self.paginas.push(i);
           }
        });
    };

    self.abrirFormCategoria = function () {
        self.exibirFormCategoria(true);
    };

    self.fecharFormCategoria = function () {
        self.nomeNovaCategoria('');
        self.exibirFormCategoria(false);
    };

    self.salvarNovaCategoria = function () {
        if(self.nomeNovaCategoria() && self.nomeNovaCategoria().length > 3){
            post('/utils/nova_categoria/',{'nome':self.nomeNovaCategoria()},function (dados) {
                self.categorias.push(dados.categoria);
                self.categoria(dados.categoria);
                self.exibirFormCategoria(false);
                alerta('Nova categoria foi adicionada.');
            });
        }else{
            alerta('Você precisa informar um nome para a seção.');
        }

    }

    self.salvarNovoProduto = function () {debugger;
      if(self.validarNovoProduto()){
        post('/produtos/salvar_produto/',toModelProduto(self),function (dados) {
                if(dados.success){
                    self.limparDados();
                    $('#novoProduto').modal('hide');
                    self.obterProdutos();
                }
                alerta(dados.message);
        });

      }

    };

    self.abrirEdicaoProduto = function(produto){
        self.id(produto.id);
        self.nome(produto.nome);
        self.referencia(produto.referencia);
        self.linkImg(produto.img);
        self.preco_normal(produto.preco);
        self.preco_promocional(produto.preco_promocional);
        self.categoria(produto.categoria.id);

        debugger;
        $("#novoProduto").modal('show');

    };

    self.editarProduto = function () {debugger;
      if(self.validarNovoProduto()){
        post('/produtos/editar_produto/',toModelProduto(self),function (dados) {
            self.limparDados();
            $('#novoProduto').modal('hide');
            self.obterProdutos();
            alerta(dados.message);
        });

      }

    };

    self.desativarProduto = function(produto){
        confirma('Desativar Produto','Deseja realmente desativar esse produto?',function(resposta){
           if(resposta){
               post('/produtos/trocar_status_produto/',{'idProduto':produto.id},function () {
                   self.obterProdutos();
                   alerta("O produto foi desativado e não será listado nos catalogos!");
               });
           }
        });
    };

    self.reativarProduto = function(produto){
        confirma('Reativar Produto','Este produto será reativado, deseja prosseguir?',function(resposta){
           if(resposta){
               post('/produtos/trocar_status_produto/',{'idProduto':produto.id},function () {
                   self.obterProdutos();
                   alerta("O produto foi reativado com sucesso");
               });
           }
        });
    };

    self.validarNovoProduto = function () {
        var valido = true;

        if(!self.nome()){
            valido = false;
            self.nomeObrigatorio(true);
        }else{
            self.nomeObrigatorio(false);
        }

        if(!self.referencia()){
            self.referenciaObrigatorio(true);
            valido = false;
        }else{
            self.referenciaObrigatorio(false);
        }

        if(!self.preco_normal()){
            self.precoNormalObrigatorio(true);
            valido = false;
        }else{
            self.precoNormalObrigatorio(false);
        }

        if(!self.linkImg()){
            self.linkImgObrigatorio(true);
            valido = false;
        }else{
            self.linkImgObrigatorio(false);
        }

        if(!self.categoria()){
            self.categoriaObrigatorio(true);
            valido = false;
        }else{
            self.categoriaObrigatorio(false);
        }

        return valido;
    };

    self.fecharModal = function () {
        self.limparDados();
        $("#novoProduto").modal('hide');
    };

    self.limparDados = function(){
        self.id(0);
        self.nome('');
        self.referencia('');
        self.categoria(null);
        self.linkImg('');
        self.preco_normal(0);
        self.preco_promocional(0);
    };


    //funções de paginação

    self.hasPrevious = ko.computed(function () {
       return self.pagina_atual() > 1;
    });

    self.hasNext = ko.computed(function () {
       return self.pagina_atual() < self.total_de_paginas();
    });

    self.goTo = function (pagina) {
        self.pagina_atual(pagina);
        self.obterProdutos();
    };

    self.next = function (pagina) {
        if(self.hasNext()){
            self.pagina_atual(self.pagina_atual()+1);
            self.obterProdutos();
        }
    };

    self.previous = function (pagina) {
        if(self.hasPrevious()){
            self.pagina_atual(self.pagina_atual()-1);
            self.obterProdutos();
        }
    };



    //chamada de funções iniciais
    self.obterProdutos();
    self.obterCategorias();
}

function toModelProduto(vmodel) {
    var produto = {
        id: vmodel.id(),
        nome: vmodel.nome(),
        referencia: vmodel.referencia(),
        preco: vmodel.preco_normal(),
        preco_promocional: vmodel.preco_promocional(),
        img: vmodel.linkImg(),
        categoria: vmodel.categoria()

    };

    return produto;
}


function toModelCategoria(vmodel) {
    var categoria = {
        nome: vmodel.nome
    };

    return categoria;
}

