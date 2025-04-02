import mysql.connector
from datetime import datetime

class Compras:
    def __init__(self, banco, estoque):
        self.conn = self.conectar_banco(banco)
        self.criar_tabela_compras()
        self.estoque = estoque
    
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

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            print("Conexão com o banco de dados encerrada.")

    def criar_tabela_compras(self):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS compras (
                    id_compra INT AUTO_INCREMENT PRIMARY KEY,
                    produto_id INT,
                    quantidade INT,
                    preco_total DECIMAL(10,2),
                    data_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (produto_id) REFERENCES estoque(id)
                );
            """)
            self.conn.commit()
            cursor.close()

    def verificar_estoque(self, produto_id, quantidade_comprada):

        estoque_atual = self.consultar_quantidade(produto_id)
        if estoque_atual >= quantidade_comprada:
            return True
        else:
            return False

    def registrar_compra(self, produto_id, quantidade, preco_unitario):
        if self.verificar_estoque(produto_id, quantidade):

            preco_total = quantidade * preco_unitario

            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO compras (produto_id, quantidade, preco_total, data_compra)
                VALUES (%s, %s, %s, NOW())
            """, (produto_id, quantidade, preco_total))

            nova_quantidade = self.consultar_quantidade(produto_id) - quantidade
            cursor.execute("""
                UPDATE estoque
                SET quantidade = %s
                WHERE id = %s
            """, (nova_quantidade, produto_id))

            self.conn.commit()
            cursor.close()
            print("Compra registrada e estoque atualizado com sucesso!")
        else:
            print("Estoque insuficiente para a quantidade solicitada. Tente uma quantidade menor.")

    def consultar_quantidade(self, produto_id):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT quantidade FROM estoque WHERE id = %s", (produto_id,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado[0] if resultado else 0

    def consultar_preco(self, produto_id):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT preco FROM estoque WHERE id = %s", (produto_id,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado[0] if resultado else 0

    def consultar_compras(self, produto_id=None, data_inicio=None, data_fim=None):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = "SELECT * FROM compras WHERE 1=1"
            valores = []
            
            if produto_id:
                query += " AND produto_id = %s"
                valores.append(produto_id)
            if data_inicio and data_fim:
                query += " AND data_compra BETWEEN %s AND %s"
                valores.extend([data_inicio, data_fim])
            
            cursor.execute(query, valores)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados

    def estatisticas_compras(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            
            cursor.execute("""
                SELECT DATE_FORMAT(data_compra, '%Y-%m') AS mes, SUM(preco_total) AS total_gasto
                FROM compras
                GROUP BY mes
                ORDER BY mes DESC;
            """)
            total_gasto_por_mes = cursor.fetchall()
            
            cursor.execute("""
                SELECT produto_id, SUM(quantidade) AS total_comprado
                FROM compras
                GROUP BY produto_id
                ORDER BY total_comprado DESC
                LIMIT 1;
            """)
            produto_mais_comprado = cursor.fetchone()
            
            cursor.close()
            return {
                "total_gasto_por_mes": total_gasto_por_mes,
                "produto_mais_comprado": produto_mais_comprado
            }
