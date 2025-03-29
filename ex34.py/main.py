from combustivel import CalculoCombustivel
from veiculo import Veiculo

try:
    distancia = float(input("Digite a distância em quilômetros a ser percorrida: "))
    consumo = float(input("Digite o consumo de combustível do seu veículo (km/l): "))

    meu_veiculo = Veiculo(consumo_km_l=consumo)

    calculo = CalculoCombustivel(veiculo=meu_veiculo, distancia=distancia)

    gastos = calculo.calcular_gasto()
    print("\nO valor total gasto será de:")
    for combustivel, valor in gastos.items():
        print(f"  {combustivel}: R$ {valor:.2f}")
except ValueError as e:
    print(f"Erro: {e}")