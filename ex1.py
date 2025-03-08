print('Olá, aqui iremos estudar!')

x = int(input('Digite um número inteiro:'))
print(f'Você digitou o número: {x}')
y = float(input('Digite um número com vírgula:'))
print(f'Você digitou o número:{y:.2f}')

soma = x + y

print(f'Os números digitados foram {x} e {y:.2f} e a soma entre os dois é: {soma:.2f}!')

fraseUm = ('Foi um prazer te ajudar nos seus estudos!\n')
fraseDois = ('Espero que volte sempre aqui s2.')

print(f'{fraseUm + fraseDois}')