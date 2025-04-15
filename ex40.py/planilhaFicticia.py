import random
from datetime import datetime, timedelta

class PlanilhaFicticia:
    def __init__(self, planilha):
        self.sheet = planilha.sheet

    def gerar_dado_ficticio(self):
        hoje = datetime.now()
        data = (hoje - timedelta(days=random.randint(0, 90))).strftime("%d/%m/%Y")

        tipo = random.choice(["Receita", "Despesa"])

        if tipo == "Receita":
            categoria = random.choice(["Salário", "Venda", "Educação", "Investimentos"])
        else:
            categoria = random.choice(["Alimentação", "Transporte", "Lazer", "Educação", "Contas", "Saúde"])

        descricao = random.choice(["Compra", "Pagamento", "Pix", "Boleto", "Venda"])
        valor = round(random.uniform(20.0, 1500.0), 2)
        forma_pagamento = random.choice(["Crédito", "Débito", "Dinheiro", "PIX", "Boleto"])
        parcelado = random.choice(["Sim", "Não"])

        if parcelado == "Sim":
            total_parcelas = random.randint(2, 12)
            numero_parcela = random.randint(1, total_parcelas)
        else:
            total_parcelas = ""
            numero_parcela = ""

        competencia = hoje.strftime("%m/%Y")
        observacoes = random.choice(["", "Pago em dia", "Atrasado", "Desconto aplicado"])

        return [data, tipo, categoria, descricao, valor, forma_pagamento, parcelado, numero_parcela, total_parcelas, competencia, observacoes]

    def inserir_dados_ficticios(self, quantidade):
        for _ in range(quantidade):
            dado = self.gerar_dado_ficticio()
            self.sheet.append_row(dado)
