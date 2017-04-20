from django.db import models
from django.utils.formats import  localize
# Create your models here.


def lista_json(queryset):
    itens = []
    for row in queryset:
        itens.append(row.to_json())

    return itens

class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def to_json(self):
        categoria = {
            'id' : self.id,
            'nome' : self.nome
        }

        return categoria

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    referencia = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    preco_promocional = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    img = models.CharField(max_length=5000)
    ativo = models.BooleanField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name='produtos')

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
