class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Foi acrescentado o valor de: {valor}R$')
        else:
            print('Depósito inválido.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Foi retirado o valor de: {valor}R$')
        else:
            print('Saldo insuficiente ou valor inválido.')

    def mostrar_saldo(self):
        print(f'O saldo atual é: {self.saldo}R$')