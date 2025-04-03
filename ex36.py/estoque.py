import mysql.connector

class Estoque:
    def __init__(self, banco):
        self.conn = self.conectar_banco(banco)
        self.criar_tabela_estoque()

    def conectar_banco(self, banco):
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database=banco,
                connection_timeout=60
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
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS historico_estoque (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                produto_id INTEGER,
                acao VARCHAR(50),
                quantidade_antiga INTEGER,
                quantidade_nova INTEGER,
                preco_antigo FLOAT,
                preco_novo FLOAT,
                peso_antigo FLOAT,
                peso_novo FLOAT,
                data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (produto_id) REFERENCES estoque(id)
            )
        """)
        self.conn.commit()
        cursor.close()
        print("Tabela historico_estoque recriada com sucesso!")

    def adc_produto(self, produto, preco, marca, peso, quantidade, categoria):
        if not self.conn:
            print("Erro: Sem conexão com o banco de dados.")
            return
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO estoque (produto, preco, marca, peso, quantidade, categoria) VALUES (%s, %s, %s, %s, %s, %s)", 
            (produto, preco, marca, peso, quantidade, categoria)
        )
        produto_id = cursor.lastrowid
        self.conn.commit()
        self.registrar_historico(produto_id, "Adicionado", quantidade_nova=quantidade, preco_novo=preco, peso_novo=peso)
        cursor.close()
        print(f"Produto '{produto}' adicionado com sucesso!")

    def remove_produto(self, produto_id, quantidade):
        cursor = self.conn.cursor()
        cursor.execute("SELECT quantidade FROM estoque WHERE id = %s", (produto_id,))
        resultado = cursor.fetchone()

        if resultado:
            estoque_atual = resultado[0]
            if estoque_atual >= quantidade:
                nova_quantidade = estoque_atual - quantidade
                cursor.execute("UPDATE estoque SET quantidade = %s WHERE id = %s", (nova_quantidade, produto_id))
                self.conn.commit()
                self.registrar_historico(produto_id, "Removido", estoque_atual, nova_quantidade)
                print(f"Produto {produto_id} atualizado. Nova quantidade: {nova_quantidade}")
            else:
                print(f"Quantidade insuficiente do produto {produto_id} em estoque.")
        else:
            print(f"Produto {produto_id} não encontrado em estoque.")

        cursor.close()

    def update_quantidade_por_id(self, produto_id, quantidade):
        cursor = self.conn.cursor()
        cursor.execute("SELECT quantidade FROM estoque WHERE id = %s", (produto_id,))
        resultado = cursor.fetchone()

        if resultado:
            quantidade_antiga = resultado[0]
            cursor.execute("UPDATE estoque SET quantidade = %s WHERE id = %s", (quantidade, produto_id))
            self.conn.commit()
            self.registrar_historico(produto_id, "Alteração de quantidade", quantidade_antiga, quantidade)
            print(f"Quantidade do produto {produto_id} atualizada para: {quantidade}")
        else:
            print(f"Produto {produto_id} não encontrado.")

        cursor.close()
    
    def update_quantidade_por_nome(self, produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, quantidade FROM estoque WHERE produto = %s", (produto,))
        resultado = cursor.fetchone()
        
        if resultado:
            produto_id, quantidade_antiga = resultado
            cursor.execute("UPDATE estoque SET quantidade = %s WHERE produto = %s", (quantidade, produto))
            self.conn.commit()
            self.registrar_historico(produto_id, "Alteração de quantidade", quantidade_antiga, quantidade)
            print(f"Quantidade do produto '{produto}' atualizada para: {quantidade}")
        else:
            print(f"Produto '{produto}' não encontrado.")
        
        cursor.close()

    def update_preco(self, produto_id, preco):
        cursor = self.conn.cursor()
        cursor.execute("SELECT preco FROM estoque WHERE id = %s", (produto_id,))
        resultado = cursor.fetchone()

        if resultado:
            preco_antigo = resultado[0]
            cursor.execute("UPDATE estoque SET preco = %s WHERE id = %s", (preco, produto_id))
            self.conn.commit()
            self.registrar_historico(produto_id, "Alteração de preço", preco_antigo=preco_antigo, preco_novo=preco)
            print(f"Preço do produto {produto_id} atualizado para R$ {preco:.2f}")
        else:
            print(f"Produto {produto_id} não encontrado.")

        cursor.close()

    def excluir_produto(self, produto_id):
        cursor = self.conn.cursor()

        cursor.execute("SET foreign_key_checks = 0;")

        cursor.execute("SELECT produto, preco, peso, quantidade, categoria FROM estoque WHERE id = %s", (produto_id,))
        produto_info = cursor.fetchone()

        if not produto_info:
            print(f"Produto ID {produto_id} não encontrado.")
            return

        produto, preco, peso, quantidade, categoria = produto_info

        print(f"Produto encontrado: {produto_info}")

        print(f"Registrando histórico da exclusão do produto ID {produto_id}...")  
        self.registrar_historico(
            produto_id, 
            "Produto Excluído", 
            quantidade_antiga=quantidade, 
            preco_antigo=preco, 
            peso_antigo=peso
        )
        print("Histórico registrado com sucesso!")

        try:
            cursor.execute("DELETE FROM estoque WHERE id = %s", (produto_id,))
            self.conn.commit()
            print(f"Produto '{produto}' (ID {produto_id}) foi excluído com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao excluir produto: {err}")

        cursor.execute("SET foreign_key_checks = 1;")
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

    def estoqueStats(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*), SUM(quantidade) FROM estoque")
        stats = cursor.fetchone()
        cursor.close()
        return {"total_produtos": stats[0], "quantidade_total": stats[1]}

    def registrar_historico(self, produto_id, acao, quantidade_antiga=None, quantidade_nova=None, 
                            preco_antigo=None, preco_novo=None, peso_antigo=None, peso_novo=None):
        cursor = self.conn.cursor()

        try:
            if quantidade_nova is None: quantidade_nova = quantidade_antiga
            if preco_novo is None: preco_novo = preco_antigo
            if peso_novo is None: peso_novo = peso_antigo

            cursor.execute("""
                INSERT INTO historico_estoque
                (produto_id, acao, quantidade_antiga, quantidade_nova, preco_antigo, preco_novo, peso_antigo, peso_novo) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (produto_id, acao, quantidade_antiga, quantidade_nova, preco_antigo, preco_novo, peso_antigo, peso_novo))

            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(f"Erro ao registrar histórico: {e}")
        finally:
            cursor.close()

    def listar_historico(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM historico_estoque")
        historico = cursor.fetchall()

        if not historico:
            print("\nNenhum histórico encontrado.")
            return

        print("\n--- Histórico de Edições ---")
        for registro in historico:
            produto_id = registro[1]
            acao = registro[2]
            qtd_antiga = registro[3] if registro[3] is not None else "-"
            qtd_nova = registro[4] if registro[4] is not None else "-"
            preco_antigo = f"R$ {registro[5]:.2f}" if registro[5] is not None else "-"
            preco_novo = f"R$ {registro[6]:.2f}" if registro[6] is not None else "-"
            peso_antigo = f"{registro[7]} kg" if registro[7] is not None else "-"
            peso_novo = f"{registro[8]} kg" if registro[8] is not None else "-"

            print(f"Produto ID: {produto_id} | Ação: {acao}")
            print(f"Quantidade: {qtd_antiga} → {qtd_nova}")
            print(f"Preço: {preco_antigo} → {preco_novo}")
            print(f"Peso: {peso_antigo} → {peso_novo}")
            print("-" * 30)

        cursor.close()

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            print("Conexão com o banco de dados encerrada.")