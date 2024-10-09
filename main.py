# import esses pacotes streamlit pandas sklearn matplotlib

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("Previsão Inicial dos custos de uma franquia")

dados = pd.read_csv('slr12.csv',sep=';')

X = dados[['FrqAnual']]
y = dados['CusInic']

modelo = LinearRegression().fit(X,y)


col1,col2 = st.columns(2)
with col1:
    st.header("Dados da Franquia")
    st.table(dados.head(10))
    
with col2:
    st.header("Gráfico")
    fig, ax = plt.subplots()
    ax.scatter(X,y,color='blue')
    ax.plot(X,modelo.predict(X),color='red')
    ax.set_xlabel('Frequência Anual')
    ax.set_ylabel('Custo Inicial')
    st.pyplot(fig)
    
    

  



