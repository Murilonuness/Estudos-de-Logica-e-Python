import os
import json
import tempfile
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import pandas as pd

class GerenciarPlanilha:
    def __init__(self):
        escopo = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        credenciais_info = json.loads(os.getenv("GOOGLE_CREDS_JSON")) # aqui fica os dados do json pego do Google Cloud, na maioria das vezes configurado na hora do Deploy para não ser exposto.
        credenciais = ServiceAccountCredentials.from_json_keyfile_dict(credenciais_info, escopo)
        self.cliente = gspread.authorize(credenciais)
        self.planilha = None

    def criar_planilha(self, nome):
        try:
            self.planilha = self.cliente.open(nome)
            print(f"A planilha '{nome}' já existe. Abrindo planilha existente...")
        except gspread.SpreadsheetNotFound:
            self.planilha = self.cliente.create(nome)
            sheet = self.planilha.sheet1
            sheet.update_title("Dados")
            cabecalho = ["Data", "Tipo", "Categoria", "Descrição", "Valor", "Forma de Pagamento", "Parcelado", "Nº Parcela", "Total Parcelas", "Competência (Mês/Ano)", "Observações"]
            sheet.insert_row(cabecalho, index=1)

        self.sheet = self.planilha.worksheet("Dados")

    def compartilhar_planilha(self, email_usuario):
        if self.planilha:
            self.planilha.share(email_usuario, perm_type="user", role="writer")
            print(f"Planilha compartilhada com {email_usuario}")
        else:
            print("Você precisa criar a planilha antes de compartilhar.")

    def limpar_dados(self, quantidade_linhas=None):
        if self.planilha:
            sheet = self.planilha.worksheet("Dados")
            total_linhas = len(sheet.get_all_values())
            
            if quantidade_linhas is None:
                if total_linhas > 1:
                    sheet.delete_rows(2, total_linhas)
                    print("Todos os dados foram excluídos, exceto o cabeçalho.")
                else:
                    print("A planilha já está limpa.")
            else:
                fim = min(1 + quantidade_linhas, total_linhas)
                if fim > 1:
                    sheet.delete_rows(2, fim)
                    print(f"{fim - 1} linha(s) foram excluídas.")
                else:
                    print("Não há linhas suficientes para excluir.")
        else:
            print("Você precisa criar ou abrir a planilha antes.")

    def excluir_planilha(self):
        if self.planilha:
            drive_id = self.planilha.id
    
            creds = self.cliente.auth.credentials
            service = build("drive", "v3", credentials=creds)
    
            service.files().delete(fileId=drive_id).execute()
            print("Planilha excluída com sucesso.")
        else:
            print("Você precisa abrir uma planilha antes de excluir.")

    def ler_dados(self, mostrar_resumo=True):
        if not self.planilha:
            print("Você precisa abrir ou criar uma planilha antes.")
            return

        try:
            sheet = self.planilha.worksheet("Dados")
            dados = sheet.get_all_values()
            if len(dados) <= 1:
                print("A planilha não contém dados além do cabeçalho.")
                return

            df = pd.DataFrame(dados[1:], columns=dados[0])
            df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0)

            df["Tipo"] = df["Tipo"].str.strip().str.title()

            lucro_total = df[df["Tipo"] == "Receita"]["Valor"].sum()
            perda_total = df[df["Tipo"] == "Despesa"]["Valor"].sum()
            saldo_final = lucro_total - perda_total

            if mostrar_resumo:
                print("Resumo financeiro da planilha:")
                print(f"Lucros totais: R$ {lucro_total:.2f}")
                print(f"Perdas totais: R$ {perda_total:.2f}")
                print(f"Saldo final: R$ {saldo_final:.2f}")

            return df

        except Exception as e:
            print(f"Erro ao ler dados da planilha: {e}")

    def filtrar_por_categoria(self, categoria):
        df = self.ler_dados(mostrar_resumo=False)
        if df is not None:
            df["Categoria"] = df["Categoria"].str.strip().str.lower()
            categoria = categoria.strip().lower()

            filtrado = df[df["Categoria"] == categoria]

            if not filtrado.empty:
                total = filtrado["Valor"].sum()
                return filtrado, total
            else:
                return None, 0

    def filtrar_por_tipo(self, tipo):
        df = self.ler_dados(mostrar_resumo=False)
        if df is not None:
            filtrado = df[df["Tipo"].str.lower() == tipo.lower()]
            return filtrado

    def filtrar_por_competencia(self, mes, ano):
        df = self.ler_dados(mostrar_resumo=False)
        if df is not None:
            df["Competência (Mês/Ano)"] = df["Competência (Mês/Ano)"].astype(str).str.strip()

            competencia = f"{mes.zfill(2)}/{ano}"
            filtrado = df[df["Competência (Mês/Ano)"] == competencia]

            saldo = filtrado.apply(
                lambda row: row["Valor"] if row["Tipo"] == "Receita" else -row["Valor"],
                axis=1
            ).sum()
            return filtrado, saldo

    def resumo_por_categoria(self):
        df = self.ler_dados(mostrar_resumo=False)
        if df is not None:
            resumo = df.groupby("Categoria")["Valor"].sum().reset_index()
            resumo = resumo.rename(columns={"Valor": "Total"})
            return resumo
        else:
            return pd.DataFrame()

    def resumo_mensal(self):
        df = self.ler_dados(mostrar_resumo=False)
        if df is not None:
            df["Valor Ajustado"] = df.apply(lambda row: row["Valor"] if row["Tipo"] == "Receita" else -row["Valor"], axis=1)
            resumo = df.groupby("Competência (Mês/Ano)")["Valor Ajustado"].sum().reset_index()
            resumo = resumo.rename(columns={"Valor Ajustado": "Saldo"})
            return resumo
        
    def importar_csv(self, caminho_csv=None, df_csv=None):
        if not self.planilha:
            print("Você precisa criar ou abrir uma planilha antes.")
            return

        try:
            if df_csv is None and caminho_csv is not None:
                df = pd.read_csv(caminho_csv)
            elif df_csv is not None:
                df = df_csv.copy()
            else:
                print("Você precisa fornecer um caminho ou um DataFrame.")
                return

            colunas_esperadas = ["Data", "Tipo", "Categoria", "Descrição", "Valor", "Forma de Pagamento", "Parcelado", "Nº Parcela", "Total Parcelas", "Competência (Mês/Ano)", "Observações"]

            if list(df.columns) != colunas_esperadas:
                print("As colunas do CSV não estão no formato esperado.")
                return

            df = df.fillna("")

            valores = df.astype(str).values.tolist()

            sheet = self.planilha.worksheet("Dados")
            sheet.append_rows(valores)
            print(f"{len(valores)} linha(s) importadas com sucesso do CSV.")

        except Exception as e:
            print(f"Erro ao importar CSV: {e}")

    def exportar_para_csv(self):
        df = self.ler_dados(mostrar_resumo=False)
        if df is not None and not df.empty:
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
            df.to_csv(temp_file.name, index=False)
            return temp_file.name
        else:
            return None
