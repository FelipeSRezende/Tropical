from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend as BaseModelBackend

class ModelBackend(BaseModelBackend):

    def authenticate(self,username=None, password=None):
        if not username is None:
            Estabelecimento = get_user_model()

            try:
                estabelecimento = Estabelecimento.objects.get(email=username)
                if(estabelecimento.check_password(password)):
                    return estabelecimento

            except Estabelecimento.DoesNotExist:
                pass