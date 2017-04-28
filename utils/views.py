from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls.base import reverse_lazy
from django.views.generic.edit import FormView

from utils.forms import CategoriaModelForm
from utils.models import Categoria, lista_json, Produto


class CategoriaView(LoginRequiredMixin, FormView):
    form_class = CategoriaModelForm
    template_name = 'paginas/categoria.html'

    def get_success_url(self):
        if(self.request.session['kwargs']):
            kwargs = self.request.session['kwargs']
            self.request.session['kwargs']  = None
            return reverse_lazy(self.request.session['url_redirect'],kwargs={'slug':kwargs})
        else:
            return reverse_lazy(self.request.session['url_redirect'])

    def form_valid(self, form):
        form.save()
        return super(CategoriaView, self).form_valid(form)

@login_required
def obter_categorias(request):
    contexto = {'categorias': lista_json(Categoria.objects.all().order_by('nome'))}
    return JsonResponse(contexto)

@login_required
def verificar_se_existe_produto_ja_cadastrado(request):
    query = request.GET.get('query')
    produto = Produto.objects.filter(nome__iexact=query).first()

    if(produto):
        dados = {'existe': True}
    else:
        dados = {'existe': False}

    return JsonResponse(dados)

@login_required
def salvar_nova_categoria(request):

    if request.method == 'POST':
        categoria = Categoria()
        categoria.nome = request.POST.get('nome')
        categoria.save()
        return JsonResponse({'categoria': categoria.to_json()})

    return NotImplementedError