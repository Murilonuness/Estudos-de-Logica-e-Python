def coleta_dados(chamadaNome, chamadaEmail, chamadaTel):
    nome = input(chamadaNome)
    email = input(chamadaEmail)
    telefone = input(chamadaTel)
    if not nome or not email  or not telefone:
        print('Erro: Dados não inseridos. Tente novamente mais tarde!')
    elif '@' not in email:
        print('Erro: É obrigatório incluir "@" em e-mail: ')
    else:
        print('Erro: Dados inseridos corretamente!\n')
        print(f'O nome do usuário é {nome}.\nO e-email do usuário é {email}.\nO telefone que consta no sistema é o {telefone}.')

coleta_dados(
    chamadaNome='Digite seu nome:', 
    chamadaEmail='Digite seu e-mail:', 
    chamadaTel='Digite seu telefone: '
    )