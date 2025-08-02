import pandas as pd
import streamlit as st

st.title("Página com Três Colunas")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Vídeo")
    st.video("https://www.youtube.com/watch?v=h4VJGNNSQnw") 

with col2:
    st.header("Imagem")
    st.image("https://preview.redd.it/no-more-implants-v0-zy01jij42gsd1.jpeg?width=1284&format=pjpg&auto=webp&s=f679a0bba504e95e8f0016ffb0e72ebaf1ef05e9", caption="Imagem Exemplo")

with col3:
    st.header("Texto")
    st.write("Este anime é bom viu!")