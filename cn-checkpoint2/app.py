#!pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from pycaret.classification import *

st.set_page_config(page_title = 'Simulador - Case Ifood',
                   layout = 'wide',
                   initial_sidebar_state = 'expanded')

st.title('Simulador - Conversão de Vendas')
with st.expander('Descrição do App', expanded = False):
    st.markdown('O objetivo principal deste app .....')
file = ''
with st.sidebar:
    st.subheader('Auto ML - Fiap [v1]')

    database = st.radio('Fonte dos dados de entrada (X):', ('CSV',))

    if database == 'CSV':
        st.info('Upload do CSV')
        file = st.file_uploader('Selecione o arquivo CSV', type='csv')
        if file:
            X_test = pd.read_csv(file)

show_df = st.checkbox('Visualizar o CSV carregado')
if file and show_df:
    st.dataframe(X_test.head())