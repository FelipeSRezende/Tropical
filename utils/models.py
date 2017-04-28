from django.db import models
from django.urls.base import reverse
from django.utils.formats import  localize
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger



# Create your custom manager here.
class ProdutoManager(models.Manager):

    def filtrar_por_nome_paginado_json(self,query,pagina=1):

        if(query):
            produtos = self.get_queryset().filter(nome__icontains=query).order_by('nome')
        else:
            produtos = self.get_queryset().all().order_by('nome')

        paginador = Paginator(lista_json(produtos),10)

        try:
            produtos_filtrado = paginador.page(pagina)
        except PageNotAnInteger:
            produtos_filtrado = paginador.page(1)
        except EmptyPage:
            produtos_filtrado = paginador.page(paginador.num_pages)

        dados = {'produtos_filtrado':produtos_filtrado,'total_de_pagina':paginador.num_pages}
        return dados

# Create global methods here.
def lista_json(queryset):
    itens = []
    for row in queryset:
        itens.append(row.to_json())

    return itens


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def to_json(self):
        categoria = {
            'id' : self.id,
            'nome' : self.nome
        }

        return categoria

class Produto(models.Model):

    objects = ProdutoManager()
    nome = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(unique=True)
    referencia = models.CharField(max_length=100,blank=True)
    preco = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    preco_promocional = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    img = models.CharField(max_length=5000,blank=True)
    ativo = models.BooleanField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name='produtos')

    def get_absolute_url(self):
        return reverse('produto:visualizar_produto',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['nome']

    def to_json(self):
        produto = {
            'id' : self.id,
            'nome' : self.nome,
            'referencia':self.referencia,
            'preco': localize(self.preco),
            'preco_promocional': localize(self.preco_promocional),
            'img':self.img,
            'ativo':self.ativo,
            'categoria': {'id':self.categoria.id,'nome':self.categoria.nome}
        }
        return produto

# TODO trocar está classe de lugar : colocar no app de catalogo
class Catalogo(models.Model):
    nome = models.CharField(max_length=200)
    texto_slogan = models.TextField(max_length=1000)
    img = models.CharField(max_length=5000)
    validade_inicio = models.DateTimeField()
    validade_fim = models.DateTimeField()
    produtos = models.ManyToManyField(Produto)

    def to_json(self):
        catalogo = {
            'id' : self.id,
            'nome' : self.nome,
            'texto_slogan' : self.texto_slogan,
            'img' : self.img,
            'validade_inicio' : self.validade_inicio,
            'validade_fim' : self.validade_fim,
            'produtos' : lista_json(self.produtos)
        }

        return catalogo

