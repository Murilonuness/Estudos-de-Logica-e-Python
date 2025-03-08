senhaORG = "000"
loginORG = "adm"
limiteTentativas = 3
tentativas = 0

while tentativas < limiteTentativas:
    tentativas += 1
    loginTeste = input("Digite seu login de acesso: ")
    senhaTeste = input("Digite sua senha de acesso: ")

    if loginTeste == loginORG and senhaTeste == senhaORG:
        print("Acesso liberado!")
        break
    elif tentativas >= limiteTentativas:
        print("Você está bloqueado!")
    else:
        print("Dados inseridos incorretos! Tente novamente.")
