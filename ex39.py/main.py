from random import randint, choices

class CofreDragao:
    def __init__(self, nome, range, limite):
        self.limite = limite
        self.nome = nome
        self.range = range
        self.segredo = randint(self.range[0], self.range[1])

    def sortear_premio(self):
        lista = ['Bota Furada', 'Cento e Cinquenta Dráquios', '10 Diamantes', 'Filhote de Dragão']
        pesos = [0.4, 0.3, 0.2, 0.1]

        sorteio = choices(lista, weights=pesos, k=1)[0]
        print(f'Seu prêmio encontrado dentro do cofre é {sorteio}')

    def resultado(self):
            tentativas = 0
            while tentativas < self.limite:
                tentativas += 1
                try:
                    chute = int(input(f'Tentativa {tentativas}/{self.limite} - Digite um número para tentar adivinhar qual é o número que abre o cofre do {self.nome}: '))
                except ValueError:
                    print("Isso não é um número! Tente novamente.")
                    tentativas -= 1
                    continue
                if chute == self.segredo:
                    print('Acertou, humano miserável!')
                    self.sortear_premio()
                    return
                elif chute < self.segredo:
                    print('Muito baixo!')
                else:
                    print('Muito alto!')
            
            print('O número de tentativas concedidas chegou ao limite. Nunca saberá o que tem no cofre, adeus.')
    
    @staticmethod
    def game():
        while True:
            print("\nBem-vindo ao Cofre do Dragão Kairos!")
            print("Escolha o modo de jogo:")
            print("1 - Modo Normal (5 tentativas)")
            print("2 - Modo Expert (3 tentativas)")

            modo = input("Digite 1 ou 2: ")
            if modo == "1":
                tentativas = 5
            elif modo == "2":
                tentativas = 3
            else:
                print("Opção inválida. Tente novamente.")
                continue
            
            cofre = CofreDragao("Dragão Kairos", (1, 10), tentativas)
            cofre.resultado()

            jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
            if jogar_novamente != "s":
                print("\nObrigado por jogar! Até a próxima aventura!")
                break

CofreDragao.game()
