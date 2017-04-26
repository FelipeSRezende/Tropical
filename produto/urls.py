from django.conf.urls import url
from produto import views

app_name = 'produto'

urlpatterns = [
    url(r'^produtos/$',views.index,name='index'),
    url(r'^produtos/salvar_produto/$',views.salvar_produto,name='salvar_produto'),
    url(r'^produtos/editar_produto/$',views.editar_produto,name='editar_produto'),
    url(r'^produtos/trocar_status_produto/$',views.trocar_status_produto,name='desativar_produto'),
    url(r'^produtos/filtrar_produto_paginado/$',views.filtrar_por_nome_paginado,name='filtrar_produtos'),
]