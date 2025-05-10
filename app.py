import streamlit as st
import sys
import os
import requests
import io
import pandas as pd

# Adicionando o diretório 'pages' ao caminho de busca de módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'pages'))

# Configuração da página
st.set_page_config(page_title="Página inicial", page_icon=":guardsman:", layout="wide")

# Título
st.title("🎯 Sistema de Recomendação de Candidatos")
st.markdown("Seja bem-vindo(a), selecione a opção desejada.")

# Função para carregar arquivos do Google Drive
def carregar_dados_drive(url):
    # Realizar o download do arquivo do Google Drive
    file_id = url.split('id=')[-1]
    download_url = f"https://drive.google.com/uc?id={file_id}&export=download"
    response = requests.get(download_url)

    # Verificar o status da resposta
    if response.status_code == 200:
        try:
            # Depuração: Exibir o conteúdo da resposta completo para verificar o que está sendo retornado
            st.write("Conteúdo do arquivo completo (primeiros 1000 caracteres):")
            st.write(response.text[:1000])  # Exibe até 1000 caracteres para depuração

            # Tenta carregar como JSON
            return pd.read_json(io.StringIO(response.text))
        except ValueError as e:
            st.error(f"Erro ao processar o arquivo JSON: {str(e)}")
            return None
    else:
        st.error(f"Erro ao carregar o arquivo. Status: {response.status_code}")
        return None

# URLs dos arquivos no Google Drive
url_vagas = "https://drive.google.com/uc?id=1U_H3lw1PUwitQxPhL_3HaOqll9KNabG9"
url_prospects = "https://drive.google.com/uc?id=1PV1VfdOUEUITazlZMfvZkvbzO6NS63xD"
url_applicants = "https://drive.google.com/uc?id=1CHv4tvbiLRUbqLZGGMAQdLhelUy-tQI3"

# Função para carregar as bases de dados com cache
@st.cache_data
def carregar_dados():
    applicants = carregar_dados_drive(url_applicants)
    vagas = carregar_dados_drive(url_vagas)
    prospects = carregar_dados_drive(url_prospects)
    
    # Verificação para garantir que as bases foram carregadas corretamente
    if applicants is None or vagas is None or prospects is None:
        st.error("Houve um erro ao carregar as bases de dados.")
    return prospects, vagas, applicants

# Carregar as bases de dados
prospects, vagas, applicants = carregar_dados()

# Verificação de carregamento
if applicants is not None and vagas is not None and prospects is not None:
    st.success("Bases de dados carregadas com sucesso!")
else:
    st.error("Houve um erro ao carregar as bases de dados.")
