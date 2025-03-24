def parOuImpar():
    while True:
        try:
            num = int(input("Digite um número de 1 a 10: "))
            if 1 <= num <= 10:
                if num % 2 == 0:
                    print("Número digitado é par")
                else:
                    print("Número digitado é ímpar")
                break
            else:
                print("Número fora da solicitação. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
parOuImpar()
