from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from produto.models import EstabelecimentoProduto


def index(request):
    return render(request,'home/home.html')

class HomeMeusProdutosView(LoginRequiredMixin,ListView):

    model = EstabelecimentoProduto
    template_name = 'home/home_autenticado.html'
    context_object_name = 'produtos'
    paginate_by = 5
    template_name = 'home/produto/meus_produtos.html'

    def get_context_data(self, **kwargs):
        contexto = super(HomeMeusProdutosView, self).get_context_data(**kwargs)
        contexto['inicio'] = 'active'
        contexto['meus_produtos'] = 'active'
        return contexto

    def get_queryset(self):
        qs = super(HomeMeusProdutosView, self).get_queryset()
        return qs.filter(nome_produto__icontains=self.request.GET.get('query', ''))