import json
import os

ARQUIVO_JSON = "ex23.json"

def carregar_usuarios():
    if os.path.exists(ARQUIVO_JSON):
        try:
            with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read().strip()
                return json.loads(conteudo) if conteudo else {}
        except json.JSONDecodeError:
            print("Erro: Arquivo JSON corrompido. Criando um novo.")
            return {}
    return {}  
    
def salvar_usuarios(usuarios):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)
    
def cadastrar_usuarios():
    usuarios = carregar_usuarios()

    try:
        while True:
            print("\nBem-vindo ao cadastro! Digite 'sair' para voltar ao menu.\n")
            nome = input("Digite seu nome: ").strip()
            if nome.lower() == 'sair':
                print("Cadastro cancelado. Redirecionando para o menu...")
                break

            idade = input("Digite sua idade: ").strip()
            if idade.lower() == 'sair':
                print("Cadastro cancelado. Redirecionando para o menu...")
                break

            email = input("Digite seu email: ").strip()
            if email.lower() == 'sair':
                print("Cadastro cancelado. Redirecionando para o menu...")
                break

            senha = input("Digite sua senha: ").strip()
            if senha.lower() == 'sair':
                print("Cadastro cancelado. Redirecionando para o menu...")
                break

            telefone = input("Digite seu telefone (somente números): ").strip()
            if telefone.lower() == 'sair':
                print("Cadastro cancelado. Redirecionando para o menu...")
                break

            cidade = input("Digite sua cidade (somente letras): ").strip()
            if cidade.lower() == 'sair':
                print("Cadastro cancelado. Redirecionando para o menu...")
                break

            if not nome or not idade or not email or not telefone or not cidade or not senha:
                print("Erro: É necessário preencher todos os campos.")
                continue
            if "@" not in email:
                print("Erro: É necessário conter '@' no email.")
                continue
            if not telefone.isdigit():
                print("Erro: É necessário conter apenas números no campo de telefone.")
                continue
            if not all(c.isalpha() or c.isspace() for c in cidade):
                print("Erro: A cidade deve conter apenas letras e espaços.")
                continue
            if email in usuarios:
                print("Erro: Este e-mail já está cadastrado.")
                continue

            usuarios[email] =  {
                "Nome": nome,
                "Idade": idade,
                "Email": email,
                "Senha": senha,
                "Telefone": telefone,
                "Cidade": cidade
            }

            salvar_usuarios(usuarios)
            print(f"Usuário {nome} cadastrado com sucesso!")

    except KeyboardInterrupt:
        print("\nCadastro interrompido pelo usuário.")

def listar_usuarios():
    usuarios = carregar_usuarios()
    
    if not usuarios:
        print("Nenhum usuário cadastrado ainda.")
    else:
        print("\nLista de Usuários Cadastrados:")
        for email, dados in usuarios.items():
            print(f"\nNome: {dados['Nome']}")
            print(f"Idade: {dados['Idade']}")
            print(f"E-mail: {dados['Email']}")
            print(f"Telefone: {dados['Telefone']}")
            print(f"Cidade: {dados['Cidade']}")
            print("-" * 30)        

def usuario_unico():
    usuarios = carregar_usuarios()

    if not usuarios:
        print("Nenhum usuário cadastrado ainda.")
    else:
        email_busca = input("Digite o email do usuário que deseja buscar os dados: ")

        if email_busca in usuarios:
            dados = usuarios[email_busca]
            print("\nDados do usuário:")
            print(f"Nome: {dados['Nome']}")
            print(f"Idade: {dados['Idade']}")
            print(f"E-mail: {dados['Email']}")
            print(f"Telefone: {dados['Telefone']}")
            print(f"Cidade: {dados['Cidade']}")
            print("-" * 30)
        else:
            print("E-mail não encontrado.")

def excluir_usuário():
    usuarios = carregar_usuarios()
    
    if not usuarios:
        print("Nenhum usuário cadastrado ainda.")
    else:
        email_busca = input("Digite o email do usuário que deseja excluir: ")

        if email_busca in usuarios:
            senha = input("Digite a sua senha para confirmar a exclusão: ").strip()

            if senha == usuarios[email_busca]["Senha"]:
                del usuarios[email_busca]
                salvar_usuarios(usuarios)
                print(f"Usuário com o e-mail {email_busca} foi excluído com sucesso!")
            else:
                print("Senha incorreta. A exclusão foi cancelada.")
        else:
            print("E-mail não encontrado.")

def atualizar_usuario():
    usuarios = carregar_usuarios()
    
    if not usuarios:
        print("Nenhum usuário cadastrado ainda.")
    else:
        email_busca = input("Digite o e-mail do usuário que deseja atualizar: ").strip()

        if email_busca in usuarios:
            senha = input("Digite a sua senha para confirmar a atualização: ").strip()

            if senha == usuarios[email_busca]["Senha"]:
                print("Autenticação bem-sucedida! O que você deseja atualizar?")
                
                print(f"Dados atuais de {usuarios[email_busca]['Nome']}:")
                for chave, valor in usuarios[email_busca].items():
                    print(f"{chave}: {valor}")
            
                nome = input("Novo nome (deixe em branco para manter o atual): ").strip()
                idade = input("Nova idade (deixe em branco para manter a atual): ").strip()
                telefone = input("Novo telefone (deixe em branco para manter o atual): ").strip()
                cidade = input("Nova cidade (deixe em branco para manter a atual): ").strip()
                
                if nome:
                    usuarios[email_busca]["Nome"] = nome
                if idade:
                    usuarios[email_busca]["Idade"] = idade
                if telefone:
                    usuarios[email_busca]["Telefone"] = telefone
                if cidade:
                    usuarios[email_busca]["Cidade"] = cidade

                salvar_usuarios(usuarios)
                print(f"Dados de {usuarios[email_busca]['Nome']} atualizados com sucesso!")
            else:
                print("Senha incorreta. A atualização foi cancelada.")
        else:
            print("E-mail não encontrado.")

def menu():
    try:
        while True:
            print("\nMenu de Cadastro:")
            print("1. Cadastrar usuário")
            print("2. Listar usuários")
            print("3. Listar usuário único")
            print("4. Excluir usuário")
            print("5. Atualizar usuário")
            print("0. Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                cadastrar_usuarios()
            elif opcao == "2":
                listar_usuarios()
            elif opcao == '3':
                usuario_unico()
            elif opcao == '4':
                excluir_usuário()
            elif opcao == '5':
                atualizar_usuario()
            elif opcao == "0":
                print("Foi um prazer enorme te ajudar, volte sempre!")
                break
            else:
                print("Opção inválida, tente novamente.")
    except ValueError:
        print('Erro: Problema no menu interativo. Contate o suporte de TI.\n')

if __name__ == "__main__":
    menu()
