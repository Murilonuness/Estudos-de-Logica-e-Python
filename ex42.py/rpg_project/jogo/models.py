from django.db import models

class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    forca = models.IntegerField()
    inteligencia = models.IntegerField()
    carisma = models.IntegerField()
    destreza = models.IntegerField()
    
    nivel = models.IntegerField(default=1)
    experiencia = models.IntegerField(default=0)

    def ganhar_xp(self, quantidade):
        self.experiencia += quantidade
        while self.experiencia >= 100:
            self.experiencia -= 100
            self.nivel += 1
        self.save()

    def __str__(self):
        return f"{self.nome} ({self.classe})"
