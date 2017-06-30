from django.conf.urls import url
from home import views
from home.views import HomeMeusProdutosView

app_name = 'home'

urlpatterns = [
    url(r'^$',views.index,name='home'),
    url(r'^inicio/meus_produtos/$',HomeMeusProdutosView.as_view(),name='inicio')
]