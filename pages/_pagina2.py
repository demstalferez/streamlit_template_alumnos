#--------------------LIBRERÍAS----------------------------#
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go


#--------------------CONFIGURACIÓN DE LA PÁGINA----------------------------#
#layout="centered" or "wide"
st.set_page_config(page_title="Mi primera APP", layout="wide", page_icon="👋")
st.set_option('deprecation.showPyplotGlobalUse', False)

#--------------------LOGO+CREACIÓN DE COLUMNA----------------------------#
col1,col2,col3 = st.columns(3)
with col1:
    st.title("")
with col2:
    st.image("img/logo.png", width=300)
with col3:
    st.title("")
