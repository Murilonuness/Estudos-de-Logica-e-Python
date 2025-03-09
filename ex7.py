tuplaUm = ('carrinho', 'boneca', 'iô iô')
print('Aqui você lê todos os itens da tupla:')
print (tuplaUm)

tuplaUm = ('carrinho', 'boneca', 'iô iô')
print('Aqui você conta o número total de itens que tem na tupla:')
print (len(tuplaUm))

tuplaUm = ('carrinho', 'boneca', 'iô iô')
print('Aqui estamos pegando o primeiro e último item da lista:')
print(tuplaUm[0] + ', ' + tuplaUm[-1])

dic = {"nome": "Lucas", 
       "idade": 30, 
       "cidade": "São Paulo",
       "escola": "Angular"}
print('Aqui estamos pegando o primeiro e único nome do dicionário:', dic["nome"])

dic2 = {"nome": ["Lucas", 'Mateus', 'João', 'José'],
       "idade": 30, 
       "cidade": "São Paulo",
       "escola": "Angular"}
print('Aqui estamos pegando o terceiro nome de uma lista de nomes dentro de um dicionário:', dic2["nome"][3])