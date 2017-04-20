from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from utils.models import Produto


@login_required
def index(request):
    contexto = {'catalogos':'active'}
    return render(request,'catalogo/catalogos.html',contexto)

@login_required
def visualizar(request,id_catalogo):
    #obter o catalogo aqui e envia-lo via paramentro para o html
    nome_catalogo = 'Ano Novo Tropical'

    if int(id_catalogo) == 1:
        nome_catalogo = 'Promoção de Natal'

    contexto = {'catalogo': '','nome_catalogo':nome_catalogo}
    return render(request,'catalogo/visualizar.html',contexto)

@login_required
def novo_catalogo(request):
    return render(request,'catalogo/novo_catalogo.html',{})

@login_required
def obter_produtos(request):
    query = request.GET.get('query')
    produtos = Produto.objects.filter(nome__icontains=query).order_by('nome')
    contexto = {'produtos': Produto.lista_json(produtos)}
    return JsonResponse(contexto)