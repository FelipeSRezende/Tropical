from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,UserManager
import re

# Create your models here.
class Estabelecimento(AbstractBaseUser,PermissionsMixin):

    username = models.CharField('Login',
        max_length= 30,unique=True,validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+_-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, numeros'
                'e os caracteres: @/./+/-/_. ',
                'Inválido'
            )
        ],help_text="Um nome curto que será usado para acessar a plataforma."
    )
    nome_estabelecimento = models.CharField('Nome do Estabelecimento',max_length=100, unique=True)
    email = models.EmailField(unique=True)
    cep = models.CharField('CEP',blank=True,max_length=20)
    logradouro = models.CharField('Logradouro',max_length=150)
    complemento = models.CharField('Complemento',max_length=100)
    municipio = models.CharField('Municipio',max_length=100)
    bairro = models.CharField('Bairro',max_length=100,blank=True)
    estado = models.CharField('UF',max_length=100)
    telefone_principal = models.CharField('Telefone Principal',max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField('Cadastrado em ',auto_now_add=True)
    foto_perfil = models.ImageField('Perfil',upload_to='estabelecimentos',null=True,blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Estabelecimento'
        verbose_name_plural = 'Estabelecimentos'


    def __str__(self):
        return self.nome_estabelecimento or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return (self)

