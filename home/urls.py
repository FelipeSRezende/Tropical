from django.conf.urls import url
from home import views

app_name = 'home'

urlpatterns = [
    url(r'^home/$',views.index,name='home'),
]