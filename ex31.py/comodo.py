class Comodo:
    __largura: float
    __profundidade: float
    __alt: float
    __rendimento_tinta: int

    def __init__(self, largura, profundidade):
        self.largura = largura
        self.profundidade = profundidade
        self.__alt = 2.9
        self.rendimento_tinta = 10

    @property
    def largura(self):
        return self.__largura
    
    @property
    def profundidade(self):
        return self.__profundidade

    @property
    def alt(self):
        return self.__alt
    
    @largura.setter
    def largura(self, largura):
        try:
            self.__largura = float(largura)
        except ValueError:
            print('O valor informado da largura é inválido.')
            exit()
    
    @profundidade.setter
    def profundidade(self, profundidade):
        try:
            self.__profundidade = float(profundidade)
        except ValueError:
            print('O valor informado da profundidade é inválido.')
            exit()
