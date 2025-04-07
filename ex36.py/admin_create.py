import jwt
import mysql.connector
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta

SECRET_KEY = "sua_chave_super_secreta"

class AdminManager:
    def __init__(self, nome_banco):
        self.conn = self.conectar_banco(nome_banco)
        self.cursor = self.conn.cursor(dictionary=True)
        self.criar_tabela_admins()

    def conectar_banco(self, nome_banco):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=nome_banco
        )

    def criar_tabela_admins(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS admins (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(100) UNIQUE NOT NULL,
                senha VARCHAR(255) NOT NULL
            )
        """)
        self.conn.commit()

    def verificar_admin(self, email, senha):
        self.cursor.execute("SELECT * FROM admins WHERE email = %s", (email,))
        admin = self.cursor.fetchone()
        if admin and check_password_hash(admin["senha"], senha):
            return self.gerar_token(admin["email"])
        return None

    def gerar_token(self, email):
        payload = {
            "email": email,
            "tipo": "admin",
            "exp": datetime.utcnow() + timedelta(hours=2)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
