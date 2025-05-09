from django.db import models
import random

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
        """Aumenta a experiência e sobe o nível do personagem, se necessário."""
        self.experiencia += quantidade
        while self.experiencia >= 100:
            self.experiencia -= 100
            self.nivel += 1
        self.save()

    def __str__(self):
        return f"{self.nome} ({self.classe})"

class DesafioCenario(models.Model):
    descricao = models.TextField()
    acao = models.CharField(max_length=50)
    dificuldade = models.IntegerField()
    resolvido = models.BooleanField(default=False)
    personagem_resolveu = models.ForeignKey('Personagem', null=True, blank=True, on_delete=models.SET_NULL)
    sucesso = models.BooleanField(null=True, blank=True)
    dado = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)

    def rolar_dado(self, personagem):
        """Rola um dado (d20) e calcula se o personagem venceu o desafio."""
        rolagem = random.randint(1, 20)
        total = rolagem + personagem.destreza
        self.dado = rolagem
        self.total = total
        if total >= self.dificuldade:
            self.sucesso = True
        else:
            self.sucesso = False

       
        self.resolvido = True
        self.personagem_resolveu = personagem

        self.save()

    def __str__(self):
        return f"{self.descricao[:40]}... (dif: {self.dificuldade})"
    