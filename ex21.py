def cadastro(nomecall, emailcall, senhacall, telcall):
    try:
        usuarios = {}

        while True:
            print("\\\Bem vindo ao cadastro//\n(Digite 'sair' para sair)")

            nome = input(nomecall).strip()
            if nome.lower() == 'sair':
                break
            email = input(emailcall).strip()
            if email.lower() == 'sair':
                break
            tel = input(telcall)
            if nome.lower() == 'sair':
                break
            senha = input(senhacall).strip()
            if nome.lower() == 'sair':
                break

            if nome or email or senha or tel:
                print('sair')
            if not nome or not email or not senha or not tel:
                print("É obrigatório cadastrar todos os dados!")
                continue
            if '@' not in email:
                print("É necessário um e-mail que contenha '@'!")
                continue
            if not tel.isdigit():
                print("Digite somente números no campo de telefone!")
                continue

            dic = {
                "nome": nome,
                "tel": tel,
                "senha": senha
            }

            usuarios[email] = dic

            print("\nUsuário cadastrado com sucesso!")
            print(usuarios)

            continuar = input("Deseja cadastrar outro usuário: (s/n)").strip()
            if continuar != 's':
                break
    except FileNotFoundError:
        print("Arquivo não encontrado.")

cadastro(nomecall="Digite seu nome: ", emailcall="Digite seu email: ", telcall="Digite seu telefone: ", senhacall="Digite sua senha: ")