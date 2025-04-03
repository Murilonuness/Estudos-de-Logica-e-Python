from estoque import Estoque
from compras import Compras
from users import User

def menu_estoque():
    print("\n--- Menu de Estoque ---")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Atualizar Quantidade por ID")
    print("4. Atualizar Quantidade por Nome")
    print("5. Atualizar Preço")
    print("6. Excluir Produto")
    print("7. Listar Todos os Produtos")
    print("8. Listar Produto por ID")
    print("9. Estatísticas de Estoque")
    print("10. Listar Histórico de Edições")
    print("11. Voltar ao Menu Principal")

def menu_compras():
    print("\n--- Menu de Compras ---")
    print("1. Registrar Compra")
    print("2. Consultar Compras")
    print("3. Estatísticas de Compras")
    print("4. Voltar ao Menu Principal")

def menu_usuarios():
    print("\n--- Menu de Usuários ---")
    print("1. Cadastrar Usuário")
    print("2. Listar Usuários")
    print("3. Atualizar Usuário")
    print("4. Deletar Usuário")
    print("5. Buscar Usuário por Nome")
    print("6. Login")
    print("7. Voltar ao Menu Principal")

def main():
    estoque = Estoque("estoque_db")
    compras = Compras("estoque_db", estoque)
    user_manager = User("estoque_db")

    while True:
        print("\n--- Menu Principal ---")
        print("1. Gerenciar Usuários")
        print("2. Acessar Menu de Estoque")
        print("3. Acessar Menu de Compras")
        print("4. Sair")

        escolha_principal = input("Escolha uma opção (1-4): ")

        if escolha_principal == '1':
            while True:
                menu_usuarios()
                escolha_usuario = input("Escolha uma opção (1-7): ")
                
                if escolha_usuario == '1':
                    nome = input("Nome: ")
                    telefone = input("Telefone: ")
                    cidade = input("Cidade: ")
                    sexo = input("Sexo (M/F/Outro): ")
                    segundo_nome = input("Segundo Nome: ")
                    email = input("Email: ")
                    senha = input("Senha: ")
                    user_manager.create_user(nome, telefone, cidade, sexo, segundo_nome, email, senha)

                elif escolha_usuario == '2':
                    usuarios = user_manager.read_users()
                    if usuarios:
                        for usuario in usuarios:
                            print(usuario)
                    else:
                        print("Nenhum usuário encontrado.")

                elif escolha_usuario == '3':
                    user_id = input("Digite o ID do usuário a ser atualizado: ")
                    nome = input("Novo nome (ou deixe em branco): ")
                    telefone = input("Novo telefone (ou deixe em branco): ")
                    cidade = input("Nova cidade (ou deixe em branco): ")
                    sexo = input("Novo sexo (ou deixe em branco): ")
                    segundo_nome = input("Novo segundo nome (ou deixe em branco): ")
                    email = input("Novo email (ou deixe em branco): ")
                    senha = input("Nova senha (ou deixe em branco): ")
                    user_manager.update_user(user_id, nome or None, telefone or None, cidade or None, sexo or None, segundo_nome or None, email or None, senha or None)

                elif escolha_usuario == '4':
                    user_id = input("Digite o ID do usuário a ser deletado: ")
                    user_manager.delete_user(user_id)

                elif escolha_usuario == '5':
                    nome = input("Digite o nome para buscar: ")
                    usuarios = user_manager.search_by_name(nome)
                    if usuarios:
                        for usuario in usuarios:
                            print(usuario)
                    else:
                        print("Nenhum usuário encontrado com esse nome.")

                elif escolha_usuario == '6':
                    email = input("Email: ")
                    senha = input("Senha: ")
                    user_manager.login(email, senha)

                elif escolha_usuario == '7':
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif escolha_principal == '2':
            while True:
                menu_estoque()
                escolha_estoque = input("Escolha uma opção (1-11): ")
                if escolha_estoque == '1':
                    produto = input("Nome do Produto: ")
                    preco = float(input("Preço do Produto: "))
                    marca = input("Marca do Produto: ")
                    peso = float(input("Peso do Produto (kg): "))
                    quantidade = int(input("Quantidade do Produto: "))
                    categoria = input("Categoria do Produto: ")
                    estoque.adc_produto(produto, preco, marca, peso, quantidade, categoria)
                elif escolha_estoque == '2':
                    produto_id = int(input("ID do Produto a ser removido: "))
                    quantidade = int(input("Quantidade a ser removida: "))
                    estoque.remove_produto(produto_id, quantidade)
                elif escolha_estoque == '3':
                    produto_id = int(input("ID do Produto a ser atualizado: "))
                    quantidade = int(input("Nova Quantidade: "))
                    estoque.update_quantidade_por_id(produto_id, quantidade)
                elif escolha_estoque == '4':
                    produto = input("Nome do Produto a ser atualizado: ")
                    quantidade = int(input("Nova Quantidade: "))
                    estoque.update_quantidade_por_nome(produto, quantidade)
                elif escolha_estoque == '5':
                    produto_id = int(input("ID do Produto a ser atualizado: "))
                    preco = float(input("Novo Preço: "))
                    estoque.update_preco(produto_id, preco)
                elif escolha_estoque == '6':
                    produto_id = int(input("ID do Produto a ser excluído: "))
                    estoque.excluir_produto(produto_id)
                elif escolha_estoque == '7':
                    estoque.listar_todos_produtos()
                elif escolha_estoque == '8':
                    produto_id = int(input("ID do Produto: "))
                    estoque.listar_produto_por_id(produto_id)
                elif escolha_estoque == '9':
                    stats = estoque.estoqueStats()
                    print(f"\nEstatísticas de Estoque:")
                    print(f"Total de Produtos: {stats['total_produtos']}")
                    print(f"Quantidade Total em Estoque: {stats['quantidade_total']}")
                elif escolha_estoque == '10':
                    estoque.listar_historico()
                elif escolha_estoque == '11':
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif escolha_principal == '3':
            while True:
                menu_compras()
                escolha_compras = input("Escolha uma opção (1-4): ")
                if escolha_compras == '1':
                    usuario_id = int(input("ID do Usuário que está comprando: "))
                    produto_id = int(input("ID do Produto a ser comprado: "))
                    quantidade = int(input("Quantidade de produto: "))
                    preco_unitario = float(input("Preço Unitário do Produto: "))

                    if compras.verificar_estoque(produto_id, quantidade):
                        compras.registrar_compra(usuario_id, produto_id, quantidade, preco_unitario)
                        print("Compra registrada com sucesso!")
                    else:
                        print("Estoque insuficiente para a quantidade solicitada. Tente uma quantidade menor.")
                elif escolha_compras == '2':
                    produto_id = int(input("ID do Produto (ou 0 para todas as compras): "))
                    data_inicio = input("Data de Início (YYYY-MM-DD): ")
                    data_fim = input("Data de Fim (YYYY-MM-DD): ")
                    compras_realizadas = compras.consultar_compras(produto_id, data_inicio, data_fim)
                    print(f"\nCompras realizadas: {compras_realizadas}")
                elif escolha_compras == '3':
                    estatisticas = compras.estatisticas_compras()
                    print(f"\nEstatísticas de Compras:")
                    print(f"Total gasto por mês: {estatisticas['total_gasto_por_mes']}")
                    print(f"Produto mais comprado: {estatisticas['produto_mais_comprado']}")
                elif escolha_compras == '4':
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif escolha_principal == '4':
            print("Saindo...")
            estoque.fechar_conexao()
            compras.fechar_conexao()
            user_manager.close_connection()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()