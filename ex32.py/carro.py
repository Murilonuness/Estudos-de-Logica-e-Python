class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 20
        print(f'O {self.modelo} ({self.cor}) acelerou para {self.velocidade} km/h.')

    def frear(self):
        if self.velocidade > 0:
            self.velocidade = max(0, self.velocidade - 10)
            print(f'O {self.modelo} ({self.cor}) freiou para {self.velocidade} km/h.')
        else:
            print(f'O {self.modelo} ({self.cor}) já está parado.')

    def estado_atual(self):
        print(f'O {self.modelo} ({self.cor}) está a {self.velocidade} km/h.')