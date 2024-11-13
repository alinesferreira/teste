# Questao 3
# Utilizando select_slider para obter o grau de satisfação do cliente (0 a 100)
import streamlit as st
satisfacao = st.select_slider(
    'Qual é o seu nível de satisfação?',
    options=range(0, 101),
    value=50  # Valor padrão
)

# Exibindo o resultado selecionado
st.write(f"Sua avaliação de satisfação é: {satisfacao}/100")
