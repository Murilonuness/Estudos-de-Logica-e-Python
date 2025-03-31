from classes import Historico

def main():
    estoque = Historico("estoque_db")
    estoque.adc_produto("Arroz", 25.99, "Tio João", 5.0, 50, "Alimentos")
    estoque.adc_produto("Detergente", 2.99, "Ypê", 0.5, 100, "Limpeza")
    estoque.adc_produto("Coca-Cola", 8.49, "Coca-Cola", 2.0, 30, "Bebidas")
    print("\nLista de Produtos no Estoque:")
    estoque.listar_todos_produtos()
    estoque.update_preco(1, 27.50)
    estoque.remove_produto(2, 10)
    print("\nDetalhes do Produto ID 3:")
    estoque.listar_produto_por_id(3)
    estoque.excluir_produto(3)
    print("\nEstoque atualizado:")
    estoque.listar_todos_produtos()

if __name__ == "__main__":
    main()