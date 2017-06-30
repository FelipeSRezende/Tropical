from django import forms
from django.contrib.auth.forms import UserCreationForm

from acesso.models import Estabelecimento


class EstabelecimentoAdminCreationForm(UserCreationForm):

    class Meta:
        model = Estabelecimento
        fields = ['nome_estabelecimento','username', 'email',]


class EstabelecimentoAdminForm(forms.ModelForm):

    class Meta:
        model = Estabelecimento
        fields = [
            'username','email','nome_estabelecimento','is_active','is_staff',
            'cep','logradouro','estado','municipio','bairro','complemento','telefone_principal',
            'foto_perfil'
        ]