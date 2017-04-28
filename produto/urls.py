from django.conf.urls import url
from produto.views import IndexView, CadastroProdutoView,AtualizarProdutoView,TrocaStatusProdutoView

app_name = 'produto'

urlpatterns = [
    url(r'^produtos/$',IndexView.as_view(template_name = 'produto/indexCCBV.html'),name='index'),
    url(r'^produtos/cadastrar_produto/$',CadastroProdutoView.as_view(),name='cadastrar_produto'),
    url(r'^produtos/(?P<slug>[\w_-]+)/edit$',AtualizarProdutoView.as_view(),name='atualizar_produto'),
    url(r'^produtos/(?P<slug>[\w_-]+)/troca$',TrocaStatusProdutoView.as_view(),name='troca_status_produto'),

    #TODO Urls das Functions Based View com JsonResponse : Verificar se vai ser utilizada e deletar se possivel
    # url(r'^produtos/salvar_produto/$',views.salvar_produto,name='salvar_produto'),
    # url(r'^produtos/editar_produto/$',views.editar_produto,name='editar_produto'),
    # url(r'^produtos/trocar_status_produto/$',views.trocar_status_produto,name='desativar_produto'),
    # url(r'^produtos/filtrar_produto_paginado/$',views.filtrar_por_nome_paginado,name='filtrar_produtos'),
]