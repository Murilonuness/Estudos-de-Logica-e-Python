def media(entrada):
    lista = []

    while True:
        numero = input(entrada)

        if numero == 'sair':
            break

        try:
            
            if '.' in numero:
                numero = float(numero)
            else:
                numero = int(numero)
            
            lista.append(numero)
        except ValueError:
            print('Digite apenas números (inteiros ou flutuantes)!')


    soma = sum(lista)
    quantidade = len(lista)

    if soma == 0 and quantidade == 0:
        print('Nenhum número foi adicionado. Espero que possa voltar outrora!')
    else:
        mediafinal = soma / quantidade
        print(f'A média final dos {quantidade} números citados é: {mediafinal:.2f}')
    

media(entrada="Digite um número inteiro ou flutuante (digite 'sair' para encerrar a sessão): ")