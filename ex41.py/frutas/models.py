from django.db import models

class Fruta(models.Model):
    nome = models.CharField(max_length=100)
    qtd = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.nome} ({self.qtd})'
    