def cadastro_produtos(nomeArg, precoArg, quantidadeArg):
    try:
        nome = input(nomeArg)
        preco = input(precoArg)
        quantidade = input(quantidadeArg)

        if not nome or not preco or not quantidade:
            print('Dados cadastrados incorretamente!')
            return
        if not preco.replace('.', '', 1).isdigit():
            print('Digite um preço válido (apenas números e ponto para centavos).')
            return
        if not quantidade.isdigit():
            print('Digite somente números para descrever a quantidade de produtos.')
            return
        
        with open('arquivo_ex18.txt', 'a', encoding='UTF8') as arquivo:
            arquivo.write(f'Produto: {nome}\nPreço:  {preco}\nQuantidade: {quantidade}\n\n')
            print('Dados cadastrados com sucesso!')
    except ValueError:
        print('Erro ao tentar converter dados. Verifique os valores informados.')


def exibir_unico_produto(procura_produto):
    try:
        listar_produto = input(procura_produto).strip()
        
        if not listar_produto:
            print('É obrigatório inserir um produto para buscarmos no banco de dados.')
            return

        with open('arquivo_ex18.txt', 'r', encoding='UTF8') as arquivo:
            dados = arquivo.readlines()
        
        for linhaAtual in range(len(dados)):
            if dados[linhaAtual].strip() == f'Produto: {listar_produto}':
                print(dados[linhaAtual])
                print(dados[linhaAtual + 1])
                print(dados[linhaAtual + 2])
                break
        else:
            print('Produto não encontrado.')
            
    except FileNotFoundError:
        print('Arquivo não encontrado no banco de dados.')
    

def exibir_todos_produtos():
    try:
        with open('arquivo_ex18.txt', 'r', encoding='UTF8') as arquivo:
            dados = arquivo.read()
            print(f'Aqui está todos os produtos cadastrados: \n{dados}')
    except FileNotFoundError:
        print('Arquivo de banco de dados não encontrado!')

def menu():
    while True:
        print('Escolha uma opção:\n'
        '1. Cadastrar Produto\n'
        '2. Consultar Produto\n'
        '3.Exibir Todos os produtos\n'
        '4. Sair')

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            cadastro_produtos(
            nomeArg='Digite o nome do produto:',
            precoArg='Digite o valor do produto: R$',
            quantidadeArg='Digite a quantidade dos produtos:')
        elif opcao == "2":
            exibir_unico_produto(procura_produto='Digite o nome do produto que quer procurar: ')
        elif opcao == "3":
            exibir_todos_produtos()
        elif opcao == "4":
            print('Saindo..')
            break
        else:
            print('Opção inválida. Tente novamente.')

menu()