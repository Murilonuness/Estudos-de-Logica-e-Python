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
    print("11. Limpar Histórico de Edições")
    print("12. Voltar ao Menu Principal")

def menu_compras():
    print("\n--- Menu de Compras ---")
    print("1. Registrar Compra")
    print("2. Consultar Todas as Compras")
    print("3. Consultar Compras por Usuário")
    print("4. Top 5 Produtos Mais Vendidos")
    print("5. Top 5 Usuários que Mais Gastaram")
    print("6. Estatísticas de Compras")
    print("7. Voltar ao Menu Principal")

def menu_usuarios():
    print("\n--- Menu de Usuários ---")
    print("1. Cadastrar Usuário")
    print("2. Listar Usuários")
    print("3. Atualizar Usuário")
    print("4. Deletar Usuário")
    print("5. Buscar Usuário por Nome")
    print("6. Alterar Senha")
    print("7. Resetar Senha")
    print("8. Voltar ao Menu Principal")

def menu_login():
    print("\n--- Menu de Login ---")
    print("1. Fazer Login")
    print("2. Voltar ao Menu Principal")

def menu_usuario_logado():
    print("\n--- Menu de Usuário Logado ---")
    print("1. Adicionar item ao carrinho")
    print("2. Ver carrinho")
    print("3. Remover item do carrinho")
    print("4. Finalizar compra")
    print("5. Consultar compras")
    print("6. Alterar dados")
    print("7. Resetar senha")
    print("8. Logout")

def main():
    estoque = Estoque("estoque_db")
    compras = Compras("estoque_db", estoque)
    user_manager = User("estoque_db")
    usuario_logado = None
    carrinhos = {}

    while True:
        print("\n--- Menu Principal ---")
        print("1. Acessar Menu de Usuários")
        print("2. Acessar Menu de Estoque")
        print("3. Acessar Menu de Compras")
        print("4. Acesso de Usuário")
        print("5. Sair")

        escolha_principal = input("Escolha uma opção (1-4): ")

        if escolha_principal == '1':
            while True:
                menu_usuarios()
                escolha_usuario = input("Escolha uma opção (1-6): ")
                
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
                    email = input("Digite o email do usuário: ")
                    nova_senha = input("Digite a nova senha: ")
                    user_manager.alterar_senha(email, nova_senha)

                elif escolha_usuario == '7':
                    email = input("Digite o email do usuário para resetar a senha: ")
                    user_manager.resetar_senha(email)

                elif escolha_usuario == '8':
                    break
        elif escolha_principal == '2':
            while True:
                menu_estoque()
                escolha_estoque = input("Escolha uma opção (1-12): ")
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
                    estoque.limpar_historico()
                elif escolha_estoque == '12':
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif escolha_principal == '3':
            while True:
                menu_compras()
                escolha_compras = input("Escolha uma opção (1-7): ")

                if escolha_compras == '1':
                    usuario_id = int(input("ID do Usuário que está comprando: "))
                    produto_id = int(input("ID do Produto a ser comprado: "))
                    quantidade = int(input("Quantidade de produto: "))
                    preco_unitario = float(input("Preço Unitário do Produto: "))

                    if estoque.verificar_estoque(produto_id, quantidade):
                        compras.registrar_compra(usuario_id, produto_id, quantidade, preco_unitario)
                        print("Compra registrada com sucesso!")
                    else:
                        print("Estoque insuficiente para a quantidade solicitada. Tente uma quantidade menor.")

                elif escolha_compras == '2':
                    try:
                        produto_id = int(input("ID do Produto (ou 0 para todas as compras): "))
                        data_inicio = input("Data de Início (YYYY-MM-DD): ")
                        data_fim = input("Data de Fim (YYYY-MM-DD): ")
                        compras_realizadas = compras.consultar_compras(
                            produto_id if produto_id != 0 else None,
                            data_inicio,
                            data_fim
                        )

                        print("\nCompras Realizadas no Período:")

                        if not compras_realizadas:
                            print("Nenhuma compra encontrada no período informado.")
                        else:
                            for compra in compras_realizadas:
                                print(f"  - Produto ID: {compra['produto_id']}")
                                print(f"    Quantidade: {compra['quantidade']}")
                                print(f"    Preço Total: R${float(compra['preco_total']):.2f}".replace(".", ","))
                                print(f"    Data: {compra['data_compra']}")
                                print("-" * 40)
                    except Exception as e:
                        print(f"Erro ao consultar compras: {e}")

                elif escolha_compras == '3':
                    usuario_id = int(input("ID do Usuário: "))
                    compras_usuario = compras.consultar_compras_por_usuario(usuario_id)
    
                    for compra in compras_usuario:
                        print(f"Produto: {compra['nome_produto']} | Quantidade: {compra['quantidade']} | "
                              f"Total: R${compra['preco_total']:.2f} | Data: {compra['data_compra']}")

                elif escolha_compras == '4':
                    top_produtos = compras.produtos_mais_vendidos()
                    print("\nTop 5 Produtos Mais Vendidos:")
                    for produto in top_produtos:
                        print(f"Produto: {produto['nome']} | Quantidade Vendida: {produto['quantidade_total']}")

                elif escolha_compras == '5':
                    top_usuarios = compras.usuarios_que_mais_compraram()
                    print("\nTop 5 Usuários que Mais Gastaram:")
                    for usuario in top_usuarios:
                        print(f"Usuário: {usuario['nome']} | Total Gasto: R${usuario['total_gasto']:.2f}")

                elif escolha_compras == '6':
                    estatisticas = compras.estatisticas_compras()
                    print("\nEstatísticas de Compras:")

                    print("\nLucro total da loja por mês:")
                    for item in estatisticas['total_lucro_por_mes']:
                        mes = item['mes']
                        total = float(item['total_gasto'])
                        print(f"  - {mes}: R${total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

                    print("\nProduto mais comprado:")
                    produto = estatisticas['produto_mais_comprado']
                    print(f"  - ID do Produto: {produto['produto_id']}")
                    print(f"  - Total Comprado: {int(produto['total_comprado'])}")

                elif escolha_compras == '7':
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif escolha_principal == '4':
            while True:
                menu_login()
                escolha_login = input("Escolha uma opção (1-2): ")
                if escolha_login == '1':
                    email = input("Email: ")
                    senha = input("Senha: ")
                    usuario_logado = user_manager.login(email, senha)
                    if usuario_logado:
                        while True:
                            menu_usuario_logado()
                            escolha_logado = input("Escolha uma opção (1-8): ")

                            if escolha_logado == '1':
                                usuario_id = usuario_logado[0]
                                produto_id = int(input("ID do Produto a ser adicionado ao carrinho: "))
                                quantidade = int(input("Quantidade: "))
                                compras.adicionar_ao_carrinho(usuario_id, produto_id, quantidade)

                            elif escolha_logado == '2':
                                usuario_id = usuario_logado[0]
                                itens = compras.ver_carrinho(usuario_id)
                                if not itens:
                                    print("Carrinho vazio.")
                                else:
                                    print("\n--- Itens no Carrinho ---")
                                    for item in itens:
                                        print(f"Produto: {item['produto']} | ID: {item['produto_id']} | Quantidade: {item['quantidade']} | Preço Unitário: R${item['preco']:.2f}")

                            elif escolha_logado == '3':
                                usuario_id = usuario_logado[0]
                                produto_id = int(input("ID do Produto que deseja remover do carrinho: "))
                                compras.remover_do_carrinho(usuario_id, produto_id)

                            elif escolha_logado == '4':
                                usuario_id = usuario_logado[0]
                                compras.finalizar_compra(usuario_id)

                            elif escolha_logado == '5':
                                usuario_id = usuario_logado[0]
                                compras_usuario = user_manager.consultar_compras_do_usuario(usuario_id)
                                if compras_usuario:
                                    print("\n--- Compras Realizadas ---")
                                    for compra in compras_usuario:
                                        print(f"ID Compra: {compra['id_compra']} | Produto: {compra['nome_produto']} | "
                                              f"Qtd: {compra['quantidade']} | Total: R${compra['preco_total']:.2f} | "
                                              f"Data: {compra['data_compra'].strftime('%d/%m/%Y %H:%M')}")
                                else:
                                    print("Nenhuma compra encontrada.")

                            elif escolha_logado == '6':
                                usuario_id = usuario_logado[0]
                                nome = input("Novo nome (ou deixe em branco): ")
                                telefone = input("Novo telefone (ou deixe em branco): ")
                                cidade = input("Nova cidade (ou deixe em branco): ")
                                sexo = input("Novo sexo (ou deixe em branco): ")
                                segundo_nome = input("Novo segundo nome (ou deixe em branco): ")
                                email_novo = input("Novo email (ou deixe em branco): ")
                                senha_nova = input("Nova senha (ou deixe em branco): ")
                                user_manager.update_user(
                                    usuario_id,
                                    nome or None,
                                    telefone or None,
                                    cidade or None,
                                    sexo or None,
                                    segundo_nome or None,
                                    email_novo or None,
                                    senha_nova or None
                                )

                            elif escolha_logado == '7':
                                email = input("Confirme seu email para resetar a senha: ")
                                user_manager.resetar_senha(email)

                            elif escolha_logado == '8':
                                usuario_logado = None
                                break
                            
                            else:
                                print("Opção inválida. Tente novamente.")
                elif escolha_login == '2':
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif escolha_principal == '5':
            print("Saindo...")
            estoque.fechar_conexao()
            compras.fechar_conexao()
            user_manager.close_connection()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
