from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from utils.models import Produto, Categoria


@login_required
def index(request):
    query = request.GET.get('query',None)
    contexto = {'produtos':Produto.objects.filtrar_por_nome_paginado_json(query),'prod':'active','query':query}
    return render(request,'produto/index.html',contexto)

@login_required
def salvar_produto(request):

    if request.method == 'POST':
        id_categoria = request.POST.get('categoria')
        produto = Produto()
        produto.ativo = True
        produto.nome = request.POST.get('nome')
        produto.referencia = request.POST.get('referencia')
        produto.categoria = Categoria.objects.get(pk = id_categoria)
        produto.preco = request.POST.get('preco')
        produto.preco_promocional = request.POST.get('preco_promocional')
        produto.img = request.POST.get('img')
        produto.save()
        if produto.id > 0:
            dados = {'success':True,'message':'Produto cadastrado com sucesso!'}
            return JsonResponse(dados)
        else:
            dados = {'success': False, 'message': 'Ouve um problema ao tentar salvar o produto, entre em contato com o TI'}
            return JsonResponse(dados)

    return InterruptedError

@login_required
def editar_produto(request):

    if request.method == 'POST':
        id_categoria = request.POST.get('categoria')
        id_produto = request.POST.get('id')

        produto = Produto.objects.get(pk=id_produto)
        produto.ativo = True
        produto.nome = request.POST.get('nome')
        produto.referencia = request.POST.get('referencia')
        produto.categoria = Categoria.objects.get(pk = id_categoria)
        produto.preco = request.POST.get('preco')
        produto.preco_promocional = request.POST.get('preco_promocional')
        produto.img = request.POST.get('img')
        produto.save()

        dados = {'success':True,'message':'Produto atualizado com sucesso!'}
        return JsonResponse(dados)

def trocar_status_produto(request):
    if(request.method == 'POST'):
        id = request.POST.get('idProduto')
        produto = Produto.objects.get(pk=id)
        produto.ativo = not produto.ativo
        produto.save()

        return JsonResponse({})

@login_required
def filtrar_por_nome_paginado(request):
    query = request.GET.get('query', None)
    pagina = request.GET.get('pagina', 1)

    dados = Produto.objects.filtrar_por_nome_paginado_json(query,pagina)
    retorno = {'produtos':list(dados['produtos_filtrado']),'total_de_paginas':dados['total_de_pagina']}
    return JsonResponse(retorno)