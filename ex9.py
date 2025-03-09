def media():
    lista = []
    limite = 5
    contagem = 0

    while contagem < limite:
        contagem += 1
        numero = int(input('Digite um número: '))
        lista.append (numero)
    
    soma = sum(lista)
    quantidade = len(lista)
    resultado = soma / quantidade
    print(f"A média dos números é: {resultado}")
media()