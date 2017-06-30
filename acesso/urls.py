from django.conf.urls import url
from django.contrib.auth import views as auth_views
from acesso.views import RegistroEstabelecimentoView, MinhaContaAtualizarDadosView, \
    MinhaContaAlterarSenhaView

app_name = 'acesso'

urlpatterns = [
    url(r'^login/$',auth_views.login,{'template_name': 'acesso/login.html'},name='login'),
    url(r'^logout/$',auth_views.logout,{'next_page':'/'},name='logout'),
    url(r'^nova_conta/$',RegistroEstabelecimentoView.as_view(),name='nova_conta'),
    url(r'^minha_conta/$',MinhaContaAtualizarDadosView.as_view(),name='minha_conta'),
    url(r'^minha_conta/alterar_senha/$',MinhaContaAlterarSenhaView.as_view(),name='alterar_senha'),
]
