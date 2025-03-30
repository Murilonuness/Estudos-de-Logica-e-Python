class Marca:
    def __init__(self, marca, produto):
        self.marca = marca
        self.produto = produto
        self.situacao_atual = True
        pass

    def exibir_info(self):
        if self.situacao_atual == True:
            print(self.marca, self.produto, 'Produto disponível.')
        else:
            print(self.marca, self.produto, 'Produto indisponível.')

    def alterar_sit(self):
        if self.situacao_atual == True:
            print(f'Compra realizada com êxito de {self.produto}.')
            self.situacao_atual = False
        else:
            print(f'O produto {self.produto} já foi comprado anteriormente.')

    def verificar_sit(self):
        if self.situacao_atual == True:
            print(f'{self.produto} está disponível no estoque.')
        else:
            print(f'{self.produto} não está disponível no estoque.')