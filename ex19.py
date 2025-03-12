def cadastrar_usuario(cadastro_nome, cadastro_email, cadastro_tel):
    try:
        while True:
            print('\nInsira os dados de cadastro!\n'
            'Se desejar cancelar o cadastro e voltar ao menu digite "sair"!\n')

            nome = input(cadastro_nome)
            email = input(cadastro_email)
            tel = input (cadastro_tel)

            if 'sair' == nome or 'sair' == email or 'sair' == tel:
                print('Voltando ao menu inicial.')
                break
            if not nome:
                print('\nÉ obrigatório inserir um nome. Tente novamente!')
                continue
            if not '@' in email or not email:
                print('\nÉ obrigatório um email ser cadastrado e conter "@". Tente novamente!')
                continue
            if not tel.isdigit() or not tel:
                print('\nÉ obrgatório um telefone ser cadastrado e conter apenas números. Tente novamente!')
                continue
            
            with open('arquivo_ex19.txt', 'a', encoding='UTF8') as arquivo:
                arquivo.write(f'Nome: {nome}\nE-mail: {email}\nTelefone: {tel}\n\n')
                print('Dados cadastrados com sucesso!')

            while True:    
                resposta = input('Digite "1" para voltar ao menu ou "2" para cadastrar outro usuário:\n' )
                
                if resposta == '1':
                    print('Voltando para o menu..\n')
                    break
                elif resposta == '2':
                    print('Ok, iremos cadastrar outro usuário.\n')
                    break
                else:
                    print('Resposta inválida, responda somente com "1" ou "2".\n')
            if resposta == '1':
                break
    except ValueError:
        print('Erro ao criar arquivo, verifique os dados cadastrados.\n')            

def exibir_todos_usuarios():
    with open('arquivo_ex19.txt', 'r', encoding='UTF8') as arquivo:
        dados = arquivo.read()
        print(f"\nAqui está todos os dados cadastrados: \n{dados}\n\n")
        print('Segue acima o arquivo completo dos usuários.\n')
    
    while True:    
        resposta = input('Digite "menu" para voltar ao menu ou "sair" para encerrar a sessão:\n' )   
        if resposta == 'menu':
            print('Voltando para o menu..\n')
            return
        elif resposta == 'sair':
            print('Encerrando sessão..\n')
            break
        else:
            print('Resposta inválida, responda somente com "1" ou "2".\n')

def exibir_usuario_unico(busca_email):
    try:
        while True:
            print('\nDigite "sair" se quiser voltar ao menu inicial!\n')
            email = input(busca_email).strip()

            if 'sair' == email:
                print('Voltando ao menu inicial.')
                break
            if not '@' in email or not email:
                print('\nÉ obrigatório um email ser cadastrado e conter "@". Tente novamente!')
                continue
            
            
            with open('arquivo_ex19.txt', 'r', encoding='UTF8') as arquivo:
                dados = arquivo.readlines()
                encontrado = False
                
                for linhaAtual in range(len(dados)):
                    if dados[linhaAtual].strip() == f'E-mail: {email}':
                        print(dados[linhaAtual - 1].strip())
                        print(dados[linhaAtual].strip())
                        print(dados[linhaAtual + 1].strip())
                        print('Acima está os dados do e-mail solicitado.')
                        encontrado = True
                        break
            if not encontrado:
                print('Usuário não encontrado.')
    except FileNotFoundError:
        print('Erro ao ler o arquivo.')

def menu():
    try:
        while True:
            opcao = input('\nEscolha a opção do menu de cadastro:'
            '\nOpção 1. Cadastrar usuário\n'
            'Opção 2. Ver todos os cadastros\n'
            'Opção 3. Buscar informações de usuário pelo e-mail\n'
            'Opção 4. Sair do menu\n')

            if opcao == '1':
                cadastrar_usuario(cadastro_nome='Digite o nome do usuario: ',
                                cadastro_email='Digite o e-mail do usuario: ',
                                cadastro_tel='Digite o telefone do usuario: ')
            elif opcao == '2':
                exibir_todos_usuarios()
            elif opcao == '3':
                exibir_usuario_unico(busca_email='Digite o e-mail do usuário que quer buscar as informações:\n')
            elif opcao == '4':
                print('\nSaindo..\n')
                break
            else:
                print('\nOpção inválida. Vamos tentar novamente.\n')
    except ValueError:
        print('Instabilidade com menu interativo. Contate o suporte.\n')
menu()