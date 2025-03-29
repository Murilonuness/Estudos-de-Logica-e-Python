class CalculoCombustivel:
    PRECO_COMBUSTIVEIS = {
        "Gasolina": 6.35,
        "Álcool": 4.13,
        "Diesel": 6.03
    }

    def __init__(self, veiculo, distancia):
        self.distancia = distancia
        self._veiculo = veiculo

    @property
    def distancia(self):
        return self._distancia

    @distancia.setter
    def distancia(self, nova_distancia):
        if nova_distancia > 0:
            self._distancia = nova_distancia
        else:
            raise ValueError("A distância deve ser maior que zero!")

    def calcular_gasto(self):
        litros_necessarios = self._distancia / self._veiculo.consumo_km_l
        gastos = {combustivel: litros_necessarios * preco for combustivel, preco in self.PRECO_COMBUSTIVEIS.items()}
        return gastos