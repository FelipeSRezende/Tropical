from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse, HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.list import ListView

from produto.forms import ProdutoModelForm
from utils.models import Produto, Categoria


# Create your views here.
class IndexView(LoginRequiredMixin,ListView):
    model = Produto
    context_object_name = 'produtos'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['prod'] = 'active'
        return context

    def get_queryset(self):
        qs = super(IndexView,self).get_queryset()
        return qs.filter(nome__icontains=self.request.GET.get('query',''))

class CadastroProdutoView(LoginRequiredMixin,FormView):
    form_class = ProdutoModelForm
    template_name = 'produto/formulario_produtoCCBV.html'
    success_url = reverse_lazy('produto:index')

    def get_initial(self):
        self.request.session['url_redirect'] = 'produto:cadastrar_produto'
        self.request.session['kwargs'] = None
        return super(CadastroProdutoView, self).get_initial()

    def form_valid(self, form):
        produto = form.save(commit=False)
        produto.ativo = True
        produto.save()
        messages.success(self.request,'Produto armazenado com sucesso!')
        return super(CadastroProdutoView,self).form_valid(form)

class AtualizarProdutoView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoModelForm
    template_name = 'produto/formulario_produtoCCBV.html'
    success_url = reverse_lazy('produto:index')

    def get_initial(self):
        self.request.session['url_redirect'] = 'produto:atualizar_produto'
        self.request.session['kwargs'] = self.get_object().slug
        return super(AtualizarProdutoView, self).get_initial()

    def form_valid(self, form):
        produtoNoBanco = self.get_object()

        produtoASalvar = form.save(commit=False)
        produtoASalvar.ativo = produtoNoBanco.ativo
        produtoASalvar.save()
        messages.success(self.request,'Produto atualizado com sucesso!')
        return super(AtualizarProdutoView,self).form_valid(form)

class TrocaStatusProdutoView(LoginRequiredMixin,DeleteView):
    model = Produto
    success_url = reverse_lazy('produto:index')
    template_name = 'produto/confirmacao_produto.html'
    context_object_name = 'produto'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.ativo = not self.object.ativo
        self.object.save()
        return HttpResponseRedirect(success_url)





# TODO Function Based View usando JsonResponse : Não esta sendo utilizado, apaga-lo em breve
#
# @login_required
# def salvar_produto(request):
#     if request.method == 'POST':
#         id_categoria = request.POST.get('categoria')
#         produto = Produto()
#         produto.ativo = True
#         produto.nome = request.POST.get('nome')
#         produto.referencia = request.POST.get('referencia')
#         produto.categoria = Categoria.objects.get(pk=id_categoria)
#         produto.preco = request.POST.get('preco')
#         produto.preco_promocional = request.POST.get('preco_promocional')
#         produto.img = request.POST.get('img')
#         produto.save()
#         if produto.id > 0:
#             dados = {'success': True, 'message': 'Produto cadastrado com sucesso!'}
#             return JsonResponse(dados)
#         else:
#             dados = {'success': False,
#                      'message': 'Ouve um problema ao tentar salvar o produto, entre em contato com o TI'}
#             return JsonResponse(dados)
#
#     return InterruptedError
#
#
# @login_required
# def editar_produto(request):
#     if request.method == 'POST':
#         id_categoria = request.POST.get('categoria')
#         id_produto = request.POST.get('id')
#
#         produto = Produto.objects.get(pk=id_produto)
#         produto.ativo = True
#         produto.nome = request.POST.get('nome')
#         produto.referencia = request.POST.get('referencia')
#         produto.categoria = Categoria.objects.get(pk=id_categoria)
#         produto.preco = request.POST.get('preco')
#         produto.preco_promocional = request.POST.get('preco_promocional')
#         produto.img = request.POST.get('img')
#         produto.save()
#
#         dados = {'success': True, 'message': 'Produto atualizado com sucesso!'}
#         return JsonResponse(dados)
#
#
# def trocar_status_produto(request):
#     if (request.method == 'POST'):
#         id = request.POST.get('idProduto')
#         produto = Produto.objects.get(pk=id)
#         produto.ativo = not produto.ativo
#         produto.save()
#
#         return JsonResponse({})
#
#
# @login_required
# def filtrar_por_nome_paginado(request):
#     query = request.GET.get('query', None)
#     pagina = request.GET.get('pagina', 1)
#
#     dados = Produto.objects.filtrar_por_nome_paginado_json(query, pagina)
#     retorno = {'produtos': list(dados['produtos_filtrado']), 'total_de_paginas': dados['total_de_pagina']}
#     return JsonResponse(retorno)
