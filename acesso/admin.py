from django.contrib import admin

from acesso.forms import EstabelecimentoAdminCreationForm, EstabelecimentoAdminForm
from acesso.models import Estabelecimento
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class EstabelecimentoAdmin(BaseUserAdmin):

    add_form = EstabelecimentoAdminCreationForm

    form = EstabelecimentoAdminForm

    add_fieldsets = (
        (
            None, {
                'fields':('username','email','password1','password2')
                }
        ),
    )


    fieldsets = (
        (
            None,{
                'fields': (
                    'username','email'
                )
            }
        ),

        (
            'Informações Basicas',{
                'fields' : (
                    'foto_perfil','nome_estabelecimento','telefone_principal'
                )
            }
        ),

        (
            'Localização', {
                'fields' : (
                    'cep','logradouro','complemento','municipio',
                    'estado'
                )
            }
        ),

        (
            'Permições',{
                'fields': (
                    'is_active','is_staff','is_superuser','groups',
                    'user_permissions'
                )

            }

        ),
    )
    list_display = ['username','email','is_active','is_staff']


admin.site.register(Estabelecimento,EstabelecimentoAdmin)