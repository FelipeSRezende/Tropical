from datetime import datetime
import pytz
from django import forms
from produto.models import EstabelecimentoProduto


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = EstabelecimentoProduto
        fields = ['nome_produto', 'ref', 'preco_normal', 'imagem', 'is_active', 'secao']
        widgets = {
            'preco_normal' : forms.TextInput(),
        }

class PromocaoRelampagoForm(forms.ModelForm):
    class Meta:
        model = EstabelecimentoProduto
        fields = ['preco_promocional','promocao_relampago','em_promocao']
        widgets = {
            'preco_promocional': forms.TextInput(),

        }