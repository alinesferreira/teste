import streamlit as st

#Questao 2
st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# Questao 3
# Utilizando select_slider para obter o grau de satisfação do cliente (0 a 100)
satisfacao = st.select_slider(
    'Qual é o seu nível de satisfação?',
    options=range(0, 101),
    value=50  # Valor padrão
)

# Exibindo o resultado selecionado
st.write(f"Sua avaliação de satisfação é: {satisfacao}/100")
