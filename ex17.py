def attUsuarios(nomeCall, emailCall, telefoneCall):
    try:
        nome = input(nomeCall).strip()
        email = input(emailCall).strip()
        telefone = input(telefoneCall).strip()

        if not nome:
            print('Erro: O nome não pode estar vazio!')
            return
        
        if email and '@' not in email:
            print('Erro: O e-mail deve conter "@"!')
            return
        
        if telefone and not telefone.isdigit():
            print('Erro: O telefone deve conter apenas números!')
            return

        atualizado = False
        nome_encontrado = False

        with open('arquivo_ex15.txt', 'r', encoding='UTF8') as arquivo:
            dados = arquivo.readlines()

        for linhaAtual in range(len(dados)):
            if dados[linhaAtual].strip() == f"Nome: {nome}":
                nome_encontrado = True
                if email:  
                    dados[linhaAtual + 1] = f"Email: {email}\n"
                    atualizado = True 
                if telefone:  
                    dados[linhaAtual + 2] = f"Telefone: {telefone}\n"
                    atualizado = True
        
        if nome_encontrado:
            if atualizado:
                with open('arquivo_ex15.txt', 'w', encoding='UTF8') as arquivo:
                    arquivo.writelines(dados)
                print(f'Sucesso: os dados de {nome} foram atualizados!')
            else:
                print('Nenhuma modificação foi realizada nos dados.')
        else:
            print('Erro: Nome não encontrado no banco de dados.')   
        
    except FileNotFoundError:
        print('Erro: O arquivo não foi encontrado. Certifique-se de que o cadastro foi feito primeiro.')

attUsuarios(
    nomeCall="Digite o nome que quer atualizar: ", 
    emailCall="Digite o novo e-mail (ou deixe em branco para não alterar): ", 
    telefoneCall="Digite o novo telefone (ou deixe em branco para não alterar): ")