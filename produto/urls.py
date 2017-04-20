from django.conf.urls import url
from produto import views

app_name = 'produto'

urlpatterns = [
    url(r'^produtos/$',views.index,name='index'),
]