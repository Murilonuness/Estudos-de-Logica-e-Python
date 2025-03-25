import time

def saidaAPP():
    while True:
        newTry = input("Deseja descobrir outro número? [s/n]\n").lower()

        if newTry == 's':
            parOuImpar()
            break
        elif newTry == 'n':
            print('Processo sendo cancelado. Volte sempre!')
            time.sleep(2)
            break
        else:
            print('Informação inserida fora da solicitação. Tente novamente!')

def parOuImpar():
    while True:
        try:
            num = input("Digite um número de 1 a 10 ou digite 'sair' para cancelar o processo: ").lower()

            if num == 'sair':
                print('Processo sendo cancelado.. Volte sempre!')
                time.sleep(2)
                break
            
            num = int(num)
            if 1 <= num <= 10:
                if num % 2 == 0:
                    print("Número digitado é par")
                else:
                    print("Número digitado é ímpar")
            else:
                print("Número fora da solicitação. Tente novamente.")
            saidaAPP()
            break
        except ValueError:
            print("Certifique-se de digitar um número entre 1 e 10 ou 'sair'.")
parOuImpar()