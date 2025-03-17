import json

# Nome do arquivo JSON onde os usuários serão armazenados
ARQUIVO_JSON = "usuarios.json"

# Função para carregar os usuários do arquivo JSON
def carregar_usuarios():
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Função para salvar os usuários no arquivo JSON
def salvar_usuarios(usuarios):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

# Função para cadastrar um novo usuário
def cadastrar_usuario(email, nome):
    usuarios = carregar_usuarios()
    if email in usuarios:
        print("Erro: Usuário já cadastrado.")
        return
    usuarios[email] = {"nome": nome}
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")

# Função para listar usuários cadastrados
def listar_usuarios():
    usuarios = carregar_usuarios()
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for email, dados in usuarios.items():
            print(f"Email: {email} - Nome: {dados['nome']}")

# Teste básico das funções
if __name__ == "__main__":
    while True:
        print("\n1. Cadastrar usuário\n2. Listar usuários\n3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            email = input("Digite o email: ")
            nome = input("Digite o nome: ")
            cadastrar_usuario(email, nome)
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")
