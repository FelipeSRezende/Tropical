from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def index(request):
    user = request.user
    dados = {'user':user,'home':'active'}
    return render(request,'home/home.html',dados)