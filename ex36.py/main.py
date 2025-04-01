from estoque import Estoque

def menu():
    print("\n--- Menu de Opções ---")
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
    print("11. Sair")

def main():
    estoque = Estoque("estoque_db")

    while True:
        menu()
        escolha = input("Escolha uma opção (1-11): ")

        if escolha == '1':
            produto = input("Nome do Produto: ")
            preco = float(input("Preço do Produto: "))
            marca = input("Marca do Produto: ")
            peso = float(input("Peso do Produto (kg): "))
            quantidade = int(input("Quantidade do Produto: "))
            categoria = input("Categoria do Produto: ")
            estoque.adc_produto(produto, preco, marca, peso, quantidade, categoria)

        elif escolha == '2':
            produto_id = int(input("ID do Produto a ser removido: "))
            quantidade = int(input("Quantidade a ser removida: "))
            estoque.remove_produto(produto_id, quantidade)

        elif escolha == '3':
            produto_id = int(input("ID do Produto a ser atualizado: "))
            quantidade = int(input("Nova Quantidade: "))
            estoque.update_quantidade_por_id(produto_id, quantidade)

        elif escolha == '4':
            produto = input("Nome do Produto a ser atualizado: ")
            quantidade = int(input("Nova Quantidade: "))
            estoque.update_quantidade_por_nome(produto, quantidade)

        elif escolha == '5':
            produto_id = int(input("ID do Produto a ser atualizado: "))
            preco = float(input("Novo Preço: "))
            estoque.update_preco(produto_id, preco)

        elif escolha == '6':
            produto_id = int(input("ID do Produto a ser excluído: "))
            estoque.excluir_produto(produto_id)

        elif escolha == '7':
            estoque.listar_todos_produtos()

        elif escolha == '8':
            produto_id = int(input("ID do Produto: "))
            estoque.listar_produto_por_id(produto_id)

        elif escolha == '9':
            stats = estoque.estoqueStats()
            print(f"\nEstatísticas de Estoque:")
            print(f"Total de Produtos: {stats['total_produtos']}")
            print(f"Quantidade Total em Estoque: {stats['quantidade_total']}")

        elif escolha == '10':
            estoque.listar_historico()

        elif escolha == '11':
            estoque.fechar_conexao()
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()