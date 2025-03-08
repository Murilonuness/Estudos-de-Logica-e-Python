senhaORG = "000"
loginORG = "adm"

loginTeste = input("Digite seu login de acesso: ")
senhaTeste = input("Digite sua senha de acesso: ")

if loginTeste == loginORG and senhaTeste == senhaORG:
    print("Acesso liberado!")
else:
    print("Acesso negado. Dados inseridos incorretos.")