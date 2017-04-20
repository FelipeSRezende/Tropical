from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from utils.models import Categoria,lista_json


@login_required
def obter_categorias(request):
    contexto = {'categorias': lista_json(Categoria.objects.all().order_by('nome'))}
    return JsonResponse(contexto)
