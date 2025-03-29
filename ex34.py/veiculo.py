class Veiculo:
    def __init__(self, consumo_km_l):
        self.consumo_km_l = consumo_km_l

    @property
    def consumo_km_l(self):
        return self._consumo_km_l

    @consumo_km_l.setter
    def consumo_km_l(self, novo_consumo):
        if novo_consumo > 0:
            self._consumo_km_l = novo_consumo
        else:
            raise ValueError("O consumo deve ser maior que zero!")