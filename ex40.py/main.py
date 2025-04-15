import streamlit as st
import pandas as pd
from crudPlanilha import GerenciarPlanilha
from planilhaFicticia import PlanilhaFicticia
import plotly.express as px

st.set_page_config(page_title="Resumo Financeiro", layout="wide")
st.title("Controle Financeiro com Google Sheets")

criar = GerenciarPlanilha()
criar.criar_planilha("Automacao Lucros e Perdas")
ficticio = PlanilhaFicticia(criar)
df = criar.ler_dados(mostrar_resumo=False)

if df is not None:
    with st.expander("Visualizar todos os dados"):
        st.dataframe(df)

        receitas = df[df["Tipo"] == "Receita"]["Valor"].sum()
        despesas = df[df["Tipo"] == "Despesa"]["Valor"].sum()
        saldo = receitas - despesas

        cor_total = "green" if saldo >= 0 else "red"
        st.markdown(
            f"<span style='color:{cor_total}; font-weight:bold'>Saldo total: R$ {saldo:.2f}</span>",
            unsafe_allow_html=True
        )


    st.markdown("---")

    st.subheader("Filtrar dados")

    tipo = st.selectbox("Filtrar por tipo", ["Todos", "Receita", "Despesa"])
    if tipo != "Todos":
        df_filtrado = criar.filtrar_por_tipo(tipo)
        st.dataframe(df_filtrado)
        st.markdown(f"**Total de {tipo.lower()}s: R$ {df_filtrado['Valor'].sum():.2f}**")

    st.subheader("Resumo por categoria")
    resumo_categoria = criar.resumo_por_categoria()
    st.dataframe(resumo_categoria)
    fig_categoria = px.pie(resumo_categoria, names="Categoria", values="Total", title="Distribuição por Categoria")
    st.plotly_chart(fig_categoria, use_container_width=True)

    categoria = st.text_input("Filtrar por categoria exata (ex: Transporte, Lazer)")
    if categoria:
        df_categoria, total_categoria = criar.filtrar_por_categoria(categoria)
        st.dataframe(df_categoria)
        st.markdown(f"**Total da categoria '{categoria}': R$ {total_categoria:.2f}**")

    st.markdown("---")

    st.subheader("Filtro por competência")
    col1, col2 = st.columns(2)
    with col1:
        mes = st.text_input("Mês (ex: 04)").strip()
    with col2:
        ano = st.text_input("Ano (ex: 2025)").strip()

    if mes and ano and mes.isdigit() and ano.isdigit() and 1 <= int(mes) <= 12:
        df_competencia, saldo = criar.filtrar_por_competencia(mes, ano)
        st.dataframe(df_competencia)
        competencia_formatada = f"{mes.zfill(2)}/{ano}"
        cor = "green" if saldo >= 0 else "red"
        st.markdown(
            f"<span style='color:{cor}; font-weight:bold'>Saldo da competência {competencia_formatada}: R$ {saldo:.2f}</span>",
            unsafe_allow_html=True
        )
    elif mes or ano:
        st.warning("Insira um mês e ano válidos (ex: 04 e 2025).")

    st.markdown("---")

    st.subheader("Resumo por competência")
    resumo_mensal = criar.resumo_mensal()
    st.dataframe(resumo_mensal)
    fig_mensal = px.line(resumo_mensal, x="Competência (Mês/Ano)", y="Saldo", title="Evolução do Saldo por Competência")
    st.plotly_chart(fig_mensal, use_container_width=True)

else:
    st.warning("Nenhum dado encontrado. Verifique se a planilha está conectada.")

with st.sidebar:
    st.markdown(" **Gerar dados fictícios**")
    with st.form("form_dados_ficticios_sidebar"):
        qtd = st.number_input("Quantidade de registros", min_value=1, max_value=100, step=1)
        submitted = st.form_submit_button("Inserir dados")

        if submitted:
            ficticio.inserir_dados_ficticios(qtd)
            st.success(f"{qtd} dado(s) aleatório(s) inserido(s) com sucesso!")
            df = criar.ler_dados(mostrar_resumo=False)

    st.markdown("---")

    st.markdown(" **Limpar dados da planilha**")
    with st.form("form_limpar_dados_sidebar"):
        qtd_linhas = st.number_input("Quantidade de linhas para limpar", min_value=1, max_value=100, step=1, value=1)
        limpar_submitted = st.form_submit_button("Limpar dados")

        if limpar_submitted:
            criar.limpar_dados(qtd_linhas)
            st.success(f"{qtd_linhas} linha(s) excluída(s) com sucesso!")

    st.markdown("---")

    st.markdown(" **Excluir planilha**")
    excluir_submitted = st.button("Excluir planilha")
    if excluir_submitted:
        criar.excluir_planilha()
        st.success("Planilha excluída com sucesso!")

    st.markdown("---")

    st.markdown("**Importar dados de um arquivo CSV**")

    with st.form("form_importar_csv_sidebar"):
        arquivo_csv = st.file_uploader("Selecione o arquivo CSV", type=["csv"], key="upload_csv_sidebar")
        importar_submitted = st.form_submit_button("Importar CSV")

        if importar_submitted:
            if arquivo_csv is not None:
                df_csv = pd.read_csv(arquivo_csv)
                criar.importar_csv(df_csv=df_csv)
                st.success("CSV importado com sucesso!")
            else:
                st.warning("Por favor, selecione um arquivo CSV válido.")

    st.markdown("---")
    
    st.markdown("**Exportar planilha para CSV**")
    exportar_btn = st.button("Exportar dados")

    if exportar_btn:
        caminho_csv = criar.exportar_para_csv()
        if caminho_csv:
            with open(caminho_csv, "rb") as file:
                st.download_button(
                    label="Clique aqui para baixar o CSV",
                    data=file,
                    file_name="dados_financeiros_exportados.csv",
                    mime="text/csv"
                )
        else:
            st.warning("Não há dados na planilha para exportar.")
