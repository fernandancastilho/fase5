import streamlit as st
import sys
import os

# Adicionando o diretório 'pages' ao caminho de busca de módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'pages'))

# Configuração da página
st.set_page_config(page_title="Página inicial", page_icon=":guardsman:", layout="wide")

# Título
st.title("🎯 Sistema de Recomendação de Candidatos")
st.markdown("Selecione uma aba no menu lateral para começar.")

# Adicionando as abas (usando selectbox ou radio)
aba = st.selectbox('Escolha o módulo:', ['Similaridade por cosseno', 'Similaridade por NPL'])

# Exibindo o conteúdo baseado na aba selecionada
if aba == 'Similaridade por cosseno':
    st.subheader('Módulo: Similaridade por Cosseno')
    st.write("Aqui vai o conteúdo do módulo de similaridade cosseno.")
    # Você pode importar e chamar funções ou rodar o script relacionado aqui.
    # Exemplo:
    import por_similaridade_cosseno
    por_similaridade_cosseno.run()
elif aba == 'Similaridade por NPL':
    st.subheader('Módulo: Similaridade por NPL')
    st.write("Aqui vai o conteúdo do aplicativo Streamlit.")
    # Importando o módulo 'streamlit_app' da pasta 'pages'
    import streamlit_app
    streamlit_app.run()  # Supondo que a função 'run()' exista no script
