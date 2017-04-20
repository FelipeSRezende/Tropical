from django.conf.urls import url
from catalogo import views

app_name = 'catalogo'

urlpatterns = [
    url(r'^catalogos/$',views.index,name='catalogos'),
    url(r'^catalogos/novo_catalogo$',views.novo_catalogo,name='novo_catalogo'),
    url(r'^catalogos/visualizar/(?P<id_catalogo>\d+)/$',views.visualizar,name='visualizar'),
    url(r'^catalogos/obter_produtos/$',views.obter_produtos,name='obter_produtos'),
]