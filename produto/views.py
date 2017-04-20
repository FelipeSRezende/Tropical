from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from utils.models import Produto


@login_required
def index(request):
    query = request.GET.get('query',None)

    if query:
        produtos = Produto.objects.filter(nome__icontains=query).order_by('nome')
    else:
        produtos = Produto.objects.all().order_by('nome')

    contexto = {'produtos':produtos,'prod':'active','query':query}
    return render(request,'produto/index.html',contexto)