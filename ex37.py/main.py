class Monstro:
    def __init__(self, nome, vida, vivo):
        self.nome = nome
        self.vida = vida
        self.vivo = vivo
    
    def receber_dano(self, valor):
        self.vida -= valor
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False
            print(f'O dano reduziu em {valor} de HP no último ataque.\nO monstro {self.nome} está morto!')
        else:
            print(f'O dano reduziu em {valor} de HP no último ataque.\nA vida atual do {self.nome} é {self.vida}!')
    
    def mostrar_status(self):
        status = "Vivo" if self.vivo else "Morto"
        print(f'O status atual do monstro "{self.nome}" é:\nHP: {self.vida}\nStatus: {status}')

    def atacar(self, outro_monstro, dano):
        if not self.vivo:
            print(f'{self.nome} está morto e não pode atacar.')
            return
    
        if not outro_monstro.vivo:
            print(f'{outro_monstro.nome} já está morto e não pode ser atacado.')
            return
        
        print(f'{self.nome} ataca {outro_monstro.nome} causando {dano} de dano!')
        outro_monstro.receber_dano(dano)

m1 = Monstro("Dragão das Sombras", 50, True)
m2 = Monstro("Dragão Reluzente", 70, True)

print("-" * 60)
m1.mostrar_status()
print("-" * 60)
m2.mostrar_status()

print("-" * 60)
m2.atacar(m1, 20)
m1.mostrar_status()

print("-" * 60)
m1.atacar(m2, 40)
m2.mostrar_status()

print("-" * 60)
m1.mostrar_status()
print("-" * 60)
m2.mostrar_status()
print("-" * 60)

m2.atacar(m1, 30)
m1.mostrar_status()
print("-" * 60)

m1.atacar(m2, 30)
m2.mostrar_status()

print("-" * 60)
m1.mostrar_status()
print("-" * 60)
m2.mostrar_status()
print("-" * 60)

m2.atacar(m1, 30)
m1.mostrar_status()