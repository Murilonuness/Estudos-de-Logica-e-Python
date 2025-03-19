import random
import datetime

def salvamento(historico):
    try:
        with open('arquivo_ex25.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(historico + '\n')
            print(historico)
    except FileNotFoundError:
        print('Erro no arquivo.')

def roleta():
    print('\nBem-vindo à roleta!')
    print('Digite "sair" para cancelar o processo.\n')

    opcoes = []

    try:
        while len(opcoes) < 8:
            comida = input('Digite uma opção a fazer: ').strip()

            if comida.lower() == 'sair':
                print('\nProcesso de sorteio cancelado.')
                return

            if comida:
                opcoes.append(comida)
                print('Opção cadastrada com sucesso!\n')
            else:
                print('Nenhum afazer foi cadastrado no sorteio.\n')

        print(f'Opções cadastradas: {", ".join(opcoes)}\n')

        while True:
            sorteio = input('Agora digite "sortear" para girar a roleta: ').lower().strip()

            if sorteio == 'sortear':
                escolhido = random.choice(opcoes)
                print(f'\nA escolha da roleta foi: {escolhido}!\n')

                historico = f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {escolhido}'
                salvamento(historico)
                break
            else:
                print('Digite somente "sortear".\n')

        while True:
            encerramento = input('Deseja encerrar a sessão? [s/n]: ').lower().strip()

            if encerramento == 's':
                print('\nFoi um prazer te ajudar, até mais!\n')
                return
            elif encerramento == 'n':
                print('\nReiniciando a roleta...\n')
                roleta()
                return
            else:
                print('Digite apenas "s" ou "n".\n')

    except ConnectionAbortedError:
        print("Erro no servidor.")

roleta()