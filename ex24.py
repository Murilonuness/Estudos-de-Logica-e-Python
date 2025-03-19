import random

opcoes = []

def roleta():
    try:
        while True:
            print('-' * 50)
            print('BEM-VINDO À ROLETA DE COMIDAS '.center(50))
            print('-' * 50)
            print('Aqui você digitará opções de comidas e a roleta escolherá uma para você comer.')
            print('(Digite "sair" a qualquer momento para cancelar o processo.)')
            print('-' * 50)

            comidaUm = input('Digite a primeira opção de comida: ').strip()
            comidaDois = input('Digite a segunda opção de comida: ').strip()
            comidaTres = input('Digite a terceira opção de comida: ').strip()
            comidaQuatro = input('Digite a quarta opção de comida: ').strip()
            comidaCinco = input('Digite a quinta opção de comida: ').strip()

            if comidaUm == 'sair' or comidaDois == 'sair' or comidaTres == 'sair' or comidaQuatro == 'sair' or comidaCinco == 'sair':
                print('Cancelando processo de sorteio. Até a próxima!')
                break

            if not comidaUm and not comidaDois and not comidaTres and not comidaQuatro and not comidaCinco:
                print('Nenhuma comida foi cadastrada no sorteio.')
                break

            opcoes.extend([comidaUm, comidaDois, comidaTres, comidaQuatro, comidaCinco])
            print('\nOpções cadastradas com sucesso!')
            print('Agora digite "sortear" para girar a roleta!')

            sorteio = input('\nComando: ').lower().strip()

            if sorteio == 'sortear':
                escolhido = random.choice(opcoes)
                print('\nA ROLETA ESCOLHEU!')
                print(f'Opção sorteada: {escolhido}!')
                print('Espero que tenha uma ótima refeição!')

                encerramento = input('\nDeseja encerrar a sessão? [s/n] ').lower().strip()
                if encerramento == 's':
                    print('\nFoi um prazer te ajudar! Até mais!')
                    break
                else:
                    print('\nRetornando ao menu inicial...')
                    print('-' * 50)
                    continue
            else:
                print('\nComando inválido! Retornando ao menu inicial...')
    except ConnectionAbortedError:
        print('\nErro no sistema.')
roleta()
