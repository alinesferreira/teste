import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'nomeServidor': ['selecione', 'Adriana', 'Monica', 'Samara'],
    'salario': [0,1200,300,5000]
})

st.write("Criando uma tabela!")
st.write(df)
opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
     df['nomeServidor'])

st.write('Você selecionou: ', opcao)

dadosFiltrados = df[df['nomeServidor'] == opcao]
dadosFiltrados
