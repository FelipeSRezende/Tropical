from django.db import models

# Create global methods here.
def lista_json(queryset):
    itens = []
    for row in queryset:
        itens.append(row.to_json())

    return itens

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def to_json(self):
        categoria = {
            'id' : self.id,
            'nome' : self.nome
        }

        return categoria

