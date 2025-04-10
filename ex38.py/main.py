class FortalezaMagica:
    def __init__(self, nome, escudo, resistencia, ativa):
        self.nome = nome
        self.escudo = escudo
        self.resistencia = resistencia
        self.ativa = ativa

    def status(self):
        status = "Escudo ativo." if self.ativa else "Escudo destruído."
        print(f'O status atual do escudo "{self.nome}" é:\nShield: {self.escudo}\nStatus: {status}')

    def sofrer_ataque(self, dano):
        self.escudo -= dano
        if self.escudo <= 0:
            self.escudo = 0
            self.ativa = False
            print(f'O dano recebido em {self.nome} foi de {dano}.\nPor conta desse ataque o escudo caiu!')
        else:
            print(f'O dano recebido em {self.nome} foi de {dano} e agora está com {self.escudo} de vida útil.')

    def reforcar_escudo(self, valor):
        self.escudo += valor
        if not self.ativa and self.escudo > 0:
            self.ativa = True
            print(f'O escudo foi reativado. Recebeu a restauração de {valor}.')
        else:
            print(f'O escudo recebeu uma restauração e agora contém {self.escudo} de vida útil.')

f1 = FortalezaMagica("Muralha de Etherion", escudo=100, resistencia=20, ativa=True)

print("-" * 80)
f1.status()
print("-" * 80)
f1.sofrer_ataque(40)
print("-" * 80)
f1.status()
print("-" * 80)
f1.reforcar_escudo(30)
print("-" * 80)
f1.status()
print("-" * 80)
f1.sofrer_ataque(91)
print("-" * 80)
f1.status()
print("-" * 80)
f1.reforcar_escudo(30)
print("-" * 80)
f1.status()
print("-" * 80)