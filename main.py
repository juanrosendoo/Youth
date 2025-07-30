import pandas as pd
import streamlit as st

st.title("Meu título")
st.write("Tabela:")

csv = pd.read_csv("Funcionarios.csv")

st.dataframe(csv)