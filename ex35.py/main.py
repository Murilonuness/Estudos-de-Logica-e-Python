from loja import Marca

produto_1 = Marca('Brastemp', 'Geladeira')
produto_2 = Marca('Iphone', 'I Pad')
print('-'*20)
produto_1.exibir_info()

produto_1.verificar_sit()
produto_1.alterar_sit()
produto_1.verificar_sit()
print('-'*20)
produto_2.alterar_sit()
produto_2.verificar_sit()
produto_2.exibir_info()
print('-'*20)