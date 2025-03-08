idade = int(input("Fale um número:"))
if idade > 0:
    print('Esse número é positivo!')
elif idade == 0:
    print('Esse número é zero!')
else:
    print('Esse número é negativo!')

print('Tarefa condicional número um concluída!')

idadeEx2 = int(input('Classificação de idade aqui!\nDiga sua idade:'))
if idadeEx2 <= 12 and idadeEx2 > 0:
    print('Você é uma criança.')
elif idadeEx2 > 12 and idadeEx2 <= 17:
    print('Você é um adolescente.')
elif idadeEx2 <= 0:
    print('Você não existe.')
else:
    print('Você já é adulto.')

print('Tarefa condicional número dois concluída!')