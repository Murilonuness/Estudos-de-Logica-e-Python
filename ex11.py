def obter_numero(mensagem):
    while True:
        try:
            numero = input(mensagem)
            if '.' in numero:
                return float(numero)
            else:
                return int(numero)
        except ValueError:
            print('Digite apenas números (inteiros ou flutuantes)!')

n1 = obter_numero('Digite o primeiro número: ')
n2 = obter_numero('Digite o segundo número: ')
n3 = obter_numero('Digite o terceiro número: ')
n4 = obter_numero('Digite o quarto número: ')
n5 = obter_numero('Digite o quinto número: ')

print(f'O tipo do primeiro número é {type(n1)} e o valor dele é {n1:.2f};')
print(f'O tipo do segundo número é {type(n2)} e o valor dele é {n2:.2f};')
print(f'O tipo do terceiro número é {type(n3)} e o valor dele é {n3:.2f};')
print(f'O tipo do quarto número é {type(n4)} e o valor dele é {n4:.2f};')
print(f'O tipo do quinto número é {type(n5)} e o valor dele é {n5:.2f}!')
