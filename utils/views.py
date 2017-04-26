from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from utils.models import Categoria, lista_json, Produto


@login_required
def obter_categorias(request):
    contexto = {'categorias': lista_json(Categoria.objects.all().order_by('nome'))}
    return JsonResponse(contexto)

@login_required
def verificar_se_existe_produto_ja_cadastrado(request):
    query = request.GET.get('query')
    produto = Produto.objects.filter(nome__iexact=query).first()

    if(produto):
        dados = {'existe': True}
    else:
        dados = {'existe': False}

    return JsonResponse(dados)

@login_required
def salvar_nova_categoria(request):

    if request.method == 'POST':
        categoria = Categoria()
        categoria.nome = request.POST.get('nome')
        categoria.save()
        return JsonResponse({'categoria': categoria.to_json()})

    return NotImplementedError