from django.conf.urls import url

from utils import views
from utils.views import CategoriaView

app_name = 'utils'

urlpatterns = [
    url(r'^utils/categoria/$',CategoriaView.as_view(),name='categoria'),
    url(r'^utils/ja_existe_produto_cadastrado/$',views.verificar_se_existe_produto_ja_cadastrado,name='ja_existe_produto'),
]