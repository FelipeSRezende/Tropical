"""
tropical URL Configuration

"""
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from tropical import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('acesso.urls')),
    url(r'^',include('home.urls')),
    url(r'^',include('produto.urls')),
    url(r'^',include('utils.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)