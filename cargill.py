import streamlit as st
import pandas as pd

# URL do Google Sheets exportado como CSV
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSq4bCC1d6FVPtjqpq-LQMLHxAhVEDCIxawGKoBMlKxxWuPMGKOBRmNYrMqcHFTFK-nFMO-FgMCe_ou/pub?output=csv"

# Lendo o CSV no DataFrame
df = pd.read_csv(url)

#Gerando um loap de atualização a cada minuto
if st.button("Atualizar Dados"):
    st.rerun()


# Verificando se a coluna 'DATA' existe e convertendo para formato datetime
if 'DATA' in df.columns:
    df['DATA'] = pd.to_datetime(df['DATA'], errors='coerce')

# Título e logomarca
st.image('logo.png', width=200)
st.title("PAINEL DE RECEBIMENTO DE VEÍCULOS - CARGILL")
st.markdown('''
            O intuito deste painel é disponibilizar em tempo real as informações de registro de veículos,
            e assim garantir a qualidade da informação para com nossos clientes.
''')

# Input de data para filtrar o DataFrame
data_selecionada = st.date_input("Selecione uma data", value=pd.Timestamp.now().date())

# Filtrando o DataFrame pela data selecionada
df_filtrado = df[df['DATA'].dt.date == data_selecionada]

# Exibindo o DataFrame filtrado
st.dataframe(df_filtrado)

# Exibindo o total de registros abaixo do DataFrame
num_registros = df_filtrado.shape[0]
st.write(f"**Total de Registros Filtrados:** {num_registros}")


# Menu lateral
st.markdown('''
Projeto desenvolvido por Williams Rodrigues  
Analista de Logística  

Solution Logística
''')

#Abrindo o link do Power Bi Cargil
pbix=st.link_button('Clique para Acessar ao Power BI','https://app.powerbi.com/view?r=eyJrIjoiYzE3ZmFlZmItMWYwZi00ODdjLTkyZGItNzdiODRiZTk3YThmIiwidCI6IjNiNTg1ODA2LWQzNTMtNDQxYy1iNGU2LTM3ZGE3YTM1NzMxNiJ9')
zap=st.link_button('Fale com o Desenvolvedor','https://api.whatsapp.com/send/?phone=5582988639394&text&type=phone_number&app_absent=0')
#Removendo a página de código lateral
st.set_page_config(page_title="Painel de Recebimento", layout="wide", initial_sidebar_state="collapsed")
