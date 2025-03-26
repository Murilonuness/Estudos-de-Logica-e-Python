import math
import time

def factorial():
    try:
        while True:
            print("-"*40)
            print('Bem-vindo ao cálculo de Fatorial!')
            print("-"*40)
            numSolicitado = input('Digite o número que quer saber o cálculo fatorial: ')
            numSolicitado = int(numSolicitado)
            resultado = math.factorial(numSolicitado)
            print(f'O cálculo fatorial do número mencionado é {resultado}')
            saída = input('Deseja calcular outro número? [s/n]\nComando: ').lower()

            if saída == 's':
                continue
            elif saída == 'n':
                print('Foi um prazer ajudar você. Irei te redirecionar para o menu inicial.')
                menu()
                time.sleep(2)
                break
    except ValueError:
        print('Erro: Por favor, digite um número válido!')
        
def fibonacci():
    try:
        while True:
            print("-"*40)
            print('Bem-vindo ao cálculo de Fibonacci!')
            print("-"*40)
            numSolicitado = input('Digite o número de termos de sequência da Fibonacci que deseja calcular: ')
            numSolicitado = int(numSolicitado)

            fib_sequence = [0, 1]
            
            for i in range(2, numSolicitado):
                next_fib = fib_sequence[-1] + fib_sequence[-2]
                fib_sequence.append(next_fib)
            
            print(f'A sequência de Fibonacci até {numSolicitado} termos é: {fib_sequence}')

            saída = input('Deseja calcular outro número? [s/n]\nComando: ').lower()

            if saída == 's':
                continue
            elif saída == 'n':
                print('Foi um prazer ajudar você. Irei te redirecionar para o menu inicial.')
                menu()
                time.sleep(2)
                break
    except ValueError:
        print('Erro: Por favor, digite um número válido!')

def menu():
    try:
        while True:
            print("-"*20)
            print('Bem vindo ao menu!')
            print("-"*20)

            opcao = input('O que você deseja?\n'
                          '1. Opção - Fatorial\n'
                          '2. Opção - Fibonacci\n'
                          '0. Opção - Sair do menu\n'
                          'Comando: ')

            if opcao == '1':
                factorial()
                break
            elif opcao == '2':
                fibonacci()
                break
            elif opcao == '0':
                print('Foi um prazer te ajudar. Volte sempre!')
                time.sleep(2)
                break
            else:
                print('Digite apenas números que estão dentre as opções. Tente novamente!')
    except ConnectionError:
        print('Erro: Menu com problemas, por favor tente novamente.')
menu()
