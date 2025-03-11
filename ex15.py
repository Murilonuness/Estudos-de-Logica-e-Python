def cadastroContatos(nomeCall, emailCall, telefoneCall):
    nome = input(nomeCall)
    email = input(emailCall)
    telefone = input(telefoneCall)
    
    if not nome.strip() or not email.strip() or not telefone:
        print("Erros: Todos os dados são obrigatórios!")
    elif '@' not in email:
        print("Erro: É obrigatório o uso de '@' no cadastro e e-mail!")
    elif not telefone.isdigit():
        print("Erro: O telefone deve conter apenas números!")
    else:
        with open('arquivo_ex15.txt', 'a', encoding='UTF8') as arquivo:
            arquivo.write(f"-----------------\nDados do cliente.\n-----------------\nNome: {nome}\nEmail: {email}\nTelefone: {telefone}\n-----------------\n\n")
        print(f"Sucesso: Cadastro realizado com êxito!\nDados do cliente {nome} foram salvos no arquivo.\n")

cadastroContatos(nomeCall="Digite seu nome: ", emailCall="Digite seu e-mail:", telefoneCall="Digite seu telefone:")
