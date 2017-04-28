from django import forms
from django.utils.text import slugify

from utils.models import Categoria


class CategoriaModelForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nome']

    def save(self, commit=True):
        instance = super(CategoriaModelForm, self).save(commit=False)
        instance.slug = slugify(instance.nome)
        instance.save()
        return instance