from django import forms
from django.utils.text import slugify

from utils.models import Produto


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'referencia', 'preco', 'img', 'ativo', 'categoria']
        widgets = {
            'preco' : forms.TextInput(),
            'preco_promocional' : forms.TextInput()
        }

    def save(self, commit=True):

        instance = super(ProdutoModelForm,self).save(commit=False)
        instance.slug = slugify(instance.nome)
        instance.save()

        return instance