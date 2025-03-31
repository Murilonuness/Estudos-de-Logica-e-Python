import mysql.connector

class Historico:
    def __init__(self, banco):
        self.conn = self.conectar_banco(banco)
        self.criar_tabela_estoque()

    def conectar_banco(self, banco):
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database=banco
            )
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            return None


    def criar_tabela_estoque(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS estoque (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                produto VARCHAR(255),
                preco FLOAT,
                marca VARCHAR(255),
                peso FLOAT,
                quantidade INTEGER,
                categoria VARCHAR(255)
            )
        """)
        self.conn.commit()
        cursor.close()

    def adc_produto(self, produto, preco, marca, peso, quantidade, categoria):
        if not self.conn:
            print("Erro: Sem conexão com o banco de dados.")
            return
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO estoque (produto, preco, marca, peso, quantidade, categoria) VALUES (%s, %s, %s, %s, %s, %s)", 
            (produto, preco, marca, peso, quantidade, categoria)
        )
        self.conn.commit()
        cursor.close()
        print(f"Produto '{produto}' adicionado com sucesso!")


    def remove_produto(self, produto_id, quantidade):
        cursor = self.conn.cursor()
        cursor.execute("SELECT quantidade FROM estoque WHERE id = %s", (produto_id,))
        resultado = cursor.fetchone()

        if resultado:
            estoque_atual = resultado[0]
            if estoque_atual >= quantidade:
                cursor.execute("UPDATE estoque SET quantidade = %s WHERE id = %s", 
                               (estoque_atual - quantidade, produto_id))
                self.conn.commit()
                print(f"Produto {produto_id} atualizado. Nova quantidade: {estoque_atual - quantidade}")
            else:
                print(f"Quantidade insuficiente do produto {produto_id} em estoque.")
        else:
            print(f"Produto {produto_id} não encontrado em estoque.")

        cursor.close()

    def update_preco(self, produto_id, preco):
        cursor = self.conn.cursor()
        cursor.execute("SELECT preco FROM estoque WHERE id = %s", (produto_id,))
        resultado = cursor.fetchone()

        if resultado:
            cursor.execute("UPDATE estoque SET preco = %s WHERE id = %s", (preco, produto_id))
            self.conn.commit()
            print(f"Preço do produto {produto_id} atualizado para R$ {preco:.2f}")
        else:
            print(f"Produto {produto_id} não encontrado.")

        cursor.close()

    def update_peso(self, produto_id, peso):
        cursor = self.conn.cursor()
        cursor.execute("SELECT peso FROM estoque WHERE id = %s", (produto_id,))
        resultado = cursor.fetchone()

        if resultado:
            cursor.execute("UPDATE estoque SET peso = %s WHERE id = %s", (peso, produto_id))
            self.conn.commit()
            print(f"Peso do produto {produto_id} atualizado para: {peso}")
        else:
            print(f"Produto {produto_id} não encontrado.")

        cursor.close()

    def update_quantidade(self, produto_id, quantidade):
        cursor = self.conn.cursor()
        cursor.execute("SELECT quantidade FROM estoque WHERE id = %s", (produto_id,))
        resultado = cursor.fetchone()

        if resultado:
            cursor.execute("UPDATE estoque SET quantidade = %s WHERE id = %s", (quantidade, produto_id))
            self.conn.commit()
            print(f"Quantidade do produto {produto_id} atualizada para: {quantidade}")
        else:
            print(f"Produto {produto_id} não encontrado.")

        cursor.close()

    def listar_produto_por_id(self, produto_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM estoque WHERE id = %s", (produto_id,))
        resultado = cursor.fetchone()

        if resultado:
            print(f"ID: {resultado[0]}")
            print(f"Produto: {resultado[1]}")
            print(f"Preço: R$ {resultado[2]:.2f}")
            print(f"Marca: {resultado[3]}")
            print(f"Peso: {resultado[4]:.2f} kg")
            print(f"Quantidade: {resultado[5]}")
            print(f"Categoria: {resultado[6]}")
        else:
            print(f"Produto com ID {produto_id} não encontrado.")

        cursor.close()

    def listar_todos_produtos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM estoque")
        resultados = cursor.fetchall()

        if resultados:
            for produto in resultados:
                print(f"ID: {produto[0]}, Produto: {produto[1]}, Preço: R$ {produto[2]:.2f}, "
                      f"Marca: {produto[3]}, Peso: {produto[4]}kg, Quantidade: {produto[5]}, Categoria: {produto[6]}")
        else:
            print("Nenhum produto encontrado no estoque.")

        cursor.close()

    def excluir_produto(self, produto_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM estoque WHERE id = %s", (produto_id,))
        self.conn.commit()
        print(f"Produto com ID {produto_id} foi removido do estoque.")
        cursor.close()