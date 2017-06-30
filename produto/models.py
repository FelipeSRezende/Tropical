from django.db import models


from acesso.models import Estabelecimento
from utils.models import Categoria
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger


# Create your custom manager here.
class ProdutoManager(models.Manager):

    def filtrar_por_nome_paginado_json(self,query,pagina=1):

        if(query):
            produtos = self.get_queryset().filter(nome__icontains=query).order_by('nome')
        else:
            produtos = self.get_queryset().all().order_by('nome')

        paginador = Paginator(produtos,10)

        try:
            produtos_filtrado = paginador.page(pagina)
        except PageNotAnInteger:
            produtos_filtrado = paginador.page(1)
        except EmptyPage:
            produtos_filtrado = paginador.page(paginador.num_pages)

        dados = {'produtos_filtrado':produtos_filtrado,'total_de_pagina':paginador.num_pages}
        return dados

# Create your models here.
class ProdutoBase(models.Model):

    nome_produto = models.CharField('Nome do Produto',max_length=100,unique=True)
    codigo = models.IntegerField('Codigo de Barras',default=0)
    ref = models.CharField('Ref',max_length=100,blank=True)
    data_criacao = models.DateTimeField('Data de Criação',auto_now_add=True)

    objects = ProdutoManager()

    class Meta:
        verbose_name = 'Produto Base'
        verbose_name_plural = 'Produtos'

class EstabelecimentoProduto(ProdutoBase):
    slug = models.SlugField('Ident',unique=True)
    preco_normal = models.DecimalField('Preço Normal',max_digits=8,decimal_places=2)
    preco_promocional = models.DecimalField('Preço Promocional', max_digits=8, decimal_places=2)
    em_promocao = models.BooleanField('Desejo iniciar a promoção assim que salvar.',default=False)
    promocao_relampago = models.IntegerField('Expira em',null=True)
    fim_da_promocao = models.DateTimeField(null=True,blank=True)
    is_active = models.BooleanField('Esta Ativo',default=True)
    data_modificacao = models.DateTimeField('Data de Modificação', auto_now=True)
    imagem = models.ImageField('Imagem',upload_to='produtos',blank=True,null=True)
    estabelecimento = models.ForeignKey(Estabelecimento,on_delete=models.CASCADE)
    secao = models.ForeignKey(Categoria,on_delete=models.SET_NULL,null=True)

    def to_json(self):
        produto = {
            'slug' : self.slug,
            'nome_produto' : self.nome_produto,
            'codigo' : self.codigo,
            'ref' : self.ref,
            'data_criacao' : self.data_criacao,
            'preco_normal' : self.preco_normal,
            'preco_promocional' : self.preco_promocional,
            'em_promocao' : self.em_promocao,
            'is_active' : self.is_active,
            'promocao_relampago' : self.promocao_relampago,
            'data_modificacao' : self.data_modificacao,
            'estabelecimento' : self.estabelecimento,
            'secao' : self.secao
        }

        return produto

    class Meta:
        verbose_name = 'Estabelecimento Produto'
        verbose_name_plural = 'Produtos do Estabelecimento'
        ordering = ('nome_produto',)