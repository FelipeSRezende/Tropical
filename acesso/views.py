from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView

from acesso.forms import EstabelecimentoAdminCreationForm
from acesso.models import Estabelecimento


class RegistroEstabelecimentoView(CreateView):

    model = Estabelecimento
    template_name = 'acesso/nova_conta.html'
    form_class = EstabelecimentoAdminCreationForm
    success_url = reverse_lazy('acesso:login')
    
    def form_valid(self, form):
        estabelecimento = form.save(commit=False);
        messages.success(self.request,'Você tem 15 dias de acesso gratis para testar o sistema. Aproveite!')
        if not estabelecimento.nome_estabelecimento:
            estabelecimento.nome_estabelecimento = estabelecimento.username
        return super(RegistroEstabelecimentoView, self).form_valid(form)

class MinhaContaAtualizarDadosView(LoginRequiredMixin,UpdateView):

    model = Estabelecimento
    template_name = 'acesso/atualizar_dados.html'
    fields = ['username','email','nome_estabelecimento','foto_perfil','cep','logradouro','complemento',
              'estado','municipio','bairro','telefone_principal']

    success_url = reverse_lazy('acesso:minha_conta')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(MinhaContaAtualizarDadosView, self).get_context_data(**kwargs)
        context['meus_dados'] = 'active'
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request,'Os dados foram atualizados.')
        return super(MinhaContaAtualizarDadosView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Não foi possivel atualizar os dados. Verifique os erros no formulario.')
        return super(MinhaContaAtualizarDadosView, self).form_invalid(form)

class MinhaContaAlterarSenhaView(LoginRequiredMixin,FormView):
    template_name = 'acesso/alterar_senha.html'
    success_url = reverse_lazy('produto:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(MinhaContaAlterarSenhaView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
        
    def get_context_data(self, **kwargs):
        context = super(MinhaContaAlterarSenhaView, self).get_context_data(**kwargs)
        context['alterar_senha'] = 'active'
        return context

    def form_valid(self, form):
        form.save()
        return super(MinhaContaAlterarSenhaView, self).form_valid(form)
