from django.conf.urls import url
from produto.views import CadastroProdutoView, AtualizarProdutoView, TrocaStatusProdutoView, PromocaoRelampagoView

app_name = 'produto'

urlpatterns = [
    url(r'^produtos/cadastrar_produto/$',CadastroProdutoView.as_view(),name='cadastrar_produto'),
    url(r'^produtos/(?P<slug>[\w_-]+)/edit$',AtualizarProdutoView.as_view(),name='atualizar_produto'),
    url(r'^produtos/(?P<slug>[\w_-]+)/troca$',TrocaStatusProdutoView.as_view(),name='troca_status_produto'),
    url(r'^produtos/(?P<slug>[\w_-]+)/promocao_relampago$',PromocaoRelampagoView.as_view(),name='promocao_relampago'),
]