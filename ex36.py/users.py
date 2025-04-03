import mysql.connector

class User:
    def __init__(self, db_name):
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': db_name
        }
        self.conn = mysql.connector.connect(**self.db_config)
        self.cursor = self.conn.cursor()

    def create_user(self, nome, telefone, cidade, sexo, segundo_nome, email, senha):
        sql = """
        INSERT INTO users (nome, telefone, cidade, sexo, segundoNome, email, senha)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(sql, (nome, telefone, cidade, sexo, segundo_nome, email, senha))
            self.conn.commit()
            print("Usuário cadastrado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao cadastrar usuário: {err}")

    def read_users(self):
        self.cursor.execute("SELECT id, nome, telefone, cidade, sexo, segundoNome, email FROM users")
        for user in self.cursor.fetchall():
            print(user)

    def update_user(self, user_id, nome=None, telefone=None, cidade=None):
        sql = "UPDATE users SET "
        values = []
        
        if nome:
            sql += "nome = %s, "
            values.append(nome)
        if telefone:
            sql += "telefone = %s, "
            values.append(telefone)
        if cidade:
            sql += "cidade = %s, "
            values.append(cidade)
        
        sql = sql.rstrip(", ")
        sql += " WHERE id = %s"
        values.append(user_id)
        
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Usuário atualizado!")
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar usuário: {err}")

    def delete_user(self, user_id):
        try:
            self.cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            self.conn.commit()
            print("Usuário deletado!")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar usuário: {err}")

    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return self.cursor.fetchone()
    
    def close_connection(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    user_manager = User("estoque_db")
    user_manager.create_user("João", "11999999999", "São Paulo", "M", "Silva", "joao@email.com", "senha123")
    user_manager.read_users()
    user_manager.close_connection()