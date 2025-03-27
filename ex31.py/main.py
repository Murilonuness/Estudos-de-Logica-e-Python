from comodo import Comodo
from calculadora import Calculadora

comodo = Comodo(
    input('Digite a largura do cômodo: '),
    input('Digite a profundidade do cômodo: ')
    )

calc = Calculadora()

print('A área das paredes é: ', 
      calc.calcular_area_paredes(comodo))
print('A área do teto é: ', 
      calc.calcular_area_teto(comodo))
print('A litragem da tinta necessária é: ', 
      calc.calcular_litragem_necessaria(comodo))