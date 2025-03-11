import math

def calculo(entrada):
    
    while True:
        numero = input(entrada)

        if numero == 'sair':
            print('Foi um prazer te ajudar! Volte sempre.')
            break

        try: 
            numero = int(numero)
            if numero < 0:
                print('Esse número é negativo, precisamos de um número positivo. Operação finalizada!')
            elif numero == 0:
                print('O fatorial de 0 é 1.')
            else:
                print(f'O fatorial de {numero} é {math.factorial(numero)}!')

        except ValueError:
            print('Número inserido incorretamente. Digite apenas números inteiros.')

calculo(entrada='Digite um número inteiro e positivo:')