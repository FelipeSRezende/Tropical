from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import  HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.utils.text import slugify
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from produto.forms import ProdutoModelForm, PromocaoRelampagoForm
from produto.models import EstabelecimentoProduto


# Create your views here.
class CadastroProdutoView(LoginRequiredMixin,CreateView):
    form_class = ProdutoModelForm
    template_name = 'produto/formulario_produtoCCBV.html'
    success_url = reverse_lazy('home:inicio')

    def get_initial(self):
        self.request.session['url_redirect'] = 'produto:cadastrar_produto'
        self.request.session['kwargs'] = None
        return super(CadastroProdutoView, self).get_initial()

    def get_context_data(self, **kwargs):
        contexto = super(CadastroProdutoView, self).get_context_data(**kwargs)
        contexto['inicio'] = 'active'
        contexto['cadastrar_produto'] = 'active'
        return contexto

    def form_valid(self, form):
        produto = form.save(commit=False)
        produto.ativo = True
        produto.estabelecimento = self.request.user
        produto.preco_promocional = 0.0
        produto.slug = slugify(produto.nome_produto)
        produto.is_active = True
        produto.save()
        form.save_m2m()
        messages.success(self.request,'Produto armazenado com sucesso!')
        return super(CadastroProdutoView,self).form_valid(form)

class AtualizarProdutoView(LoginRequiredMixin, UpdateView):
    model = EstabelecimentoProduto
    form_class = ProdutoModelForm
    template_name = 'produto/formulario_produtoCCBV.html'
    success_url = reverse_lazy('home:inicio')

    def get_initial(self):
        self.request.session['url_redirect'] = 'produto:atualizar_produto'
        self.request.session['kwargs'] = self.get_object().slug
        return super(AtualizarProdutoView, self).get_initial()

    def get_context_data(self, **kwargs):
        contexto = super(AtualizarProdutoView, self).get_context_data(**kwargs)
        contexto['produto'] = self.get_object()
        contexto['inicio'] = 'active'
        return contexto

    def form_valid(self, form):
        produtoNoBanco = self.get_object()

        produtoASalvar = form.save(commit=False)
        produtoASalvar.is_active = produtoNoBanco.is_active

        produtoASalvar.save()
        form.save_m2m()
        messages.success(self.request,'Produto atualizado com sucesso!')
        return super(AtualizarProdutoView,self).form_valid(form)

class TrocaStatusProdutoView(LoginRequiredMixin,DeleteView):
    model = EstabelecimentoProduto
    success_url = reverse_lazy('home:inicio')
    template_name = 'produto/confirmacao_produto.html'
    context_object_name = 'produto'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = not self.object.is_active
        self.object.save()
        return HttpResponseRedirect(success_url)

class PromocaoRelampagoView(LoginRequiredMixin,UpdateView):
    model = EstabelecimentoProduto
    form_class = PromocaoRelampagoForm
    template_name = 'produto/form_promocao_relampago.html'
    success_url = reverse_lazy('home:inicio')

    def get_context_data(self, **kwargs):
        contexto = super(PromocaoRelampagoView, self).get_context_data(**kwargs)
        contexto['produto'] = self.get_object()
        contexto['meus_produtos'] = 'active'
        return contexto

    def form_valid(self, form):
        produto_formulario = form.save(commit=False)

        return super(PromocaoRelampagoView, self).form_valid(form)