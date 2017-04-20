"""
tropical URL Configuration

"""

from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('acesso.urls')),
    url(r'^',include('home.urls')),
    url(r'^',include('catalogo.urls')),
    url(r'^',include('produto.urls')),
    url(r'^',include('utils.urls')),
]
