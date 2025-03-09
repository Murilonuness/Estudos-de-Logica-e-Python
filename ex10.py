def calculos( a, b ):
    soma = a + b
    mult = a * b
    operacao = input("Digite 'soma' para saber a soma.\n"
                    "Digite 'mult' para saber a multiplicação.\n"
                    "Digite 'ambos' para saber ambos:").lower()
    
    if operacao != 'soma' and operacao != 'mult' and operacao != 'ambos':
        print("Digite apenas 'soma', 'mult' ou 'ambos'!")
    elif operacao == 'soma':
        print(f'A soma de {a} + {b} é {soma}')
    elif operacao == 'ambos':
        print(f'A multiplicação de {a} e {b} é {mult} e a soma de {a} + {b} é {soma}!')
    else:
        print(f'A multiplicação de {a} e {b} é {mult}')
try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    calculos(a, b)
    
except ValueError:
    print('Digite apenas números inteiros!')