from django.conf.urls import url

from utils import views

app_name = 'utils'

urlpatterns = [
    url(r'^utils/obter_categorias/$',views.obter_categorias,name='obter_categorias'),
]