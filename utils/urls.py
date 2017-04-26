from django.conf.urls import url

from utils import views

app_name = 'utils'

urlpatterns = [
    url(r'^utils/obter_categorias/$',views.obter_categorias,name='obter_categorias'),
    url(r'^utils/ja_existe_produto_cadastrado/$',views.verificar_se_existe_produto_ja_cadastrado,name='ja_existe_produto'),
    url(r'^utils/nova_categoria/$',views.salvar_nova_categoria,name='nova_categoria'),
]