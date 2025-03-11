def exibirUsuarios():
    try:
        with open('arquivo_ex15.txt', 'r', encoding='UTF8') as arquivo:
            dados = arquivo.read()

        if dados.strip():
            print(f'Dados cadastrados:\n{dados}')
        else:
            print('Dados não encontrados.')
    except FileNotFoundError:
        print('Erro: O arquivo não foi encontrado. Certifique-se de que o cadastro foi feito primeiro.')

exibirUsuarios()