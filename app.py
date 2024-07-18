import streamlit as st
import pandas as pd 
import json as js
import matplotlib.pyplot as plt
from plotly.offline import iplot
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Popular music EDA",
    page_icon="🎧",
    layout="wide")

st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #191414;
    }
    .css-1d391kg {
        color: #FFFFFF;
    }
    .css-1v3fvcr {
        color: #FFFFFF;
    }
    .css-h5rgaw {
        background-color: #1DB954;
    }
    </style>
    """,
    unsafe_allow_html=True)


#------------------------------INTRODUCCIÓN------------------------------#
def mostrar_introduccion():
    st.header("Análisis 2024 hits musicales y predicción de su popularidad")
    st.write("Información:")

    with st.expander('Datos'):
        st.markdown("""
                    La colección de información proviene de Kaggle, las 4500 canciones más populares de 2024 en Spotify y su presencia en el resto de plataformas de música en streaming.
                    """)
        st.markdown("[Visitar Kaggle](https://www.google.com)")
    
    with st.expander("Significanza"):
        st.markdown("""Con 615 millones de usuarios, es la plataforma de audio más popular a nivel global, según muestran los datos de Stavia y la página oficial de Spotify  https://newsroom.spotify.com/company-info/ anuncian que son """)
        st.markdown("""Número de suscriptores de servicios de música en streaming a nivel mundial durante el tercer trimestre de 2023, por plataforma""")
        st.image("/Users/aguedagambon/Bootcamp/Github/Spotify_analisis/imagenes/Statista.jpg", use_column_width=True)
    st.image("/Users/aguedagambon/Bootcamp/Github/Spotify_analisis/imagenes/reproductor.png", use_column_width=True, width=50, caption="Desde Vecteezy.com")
        
#------------------------------EDA_2023------------------------------#

def mostrar_eda():

    st.header("Análisis Exploratorio de Datos (EDA)")
    st.write("Datos descriptivos sobre este dataset.")
    st.write("")
    st.write("")
    st.image('imagenes/1.png', use_column_width=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.image('imagenes/3.png', use_column_width=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.image('imagenes/2.png', use_column_width=True)
    st.write("")
    st.write("")
    st.image('imagenes/4.png', use_column_width=True)
    st.write("")
    st.write("")
    st.image('imagenes/5.png', use_column_width=True)
    st.write("")
    st.write("")
    st.image('imagenes/6.png', use_column_width=True)
#------------------------------Power BI------------------------------#
def mostrar_powerbi():
    st.write("Power BI")  
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiNzRhZTMxZDMtMDlkNS00ZDQzLWEwOWYtNzRiM2NhYWI5NzE1IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
    st.markdown(f"""<iframe width="100%" height="600" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>""", unsafe_allow_html=True)
    st.write("En este panel interactivo podemos ver los artistas máss populares, la cantidad de playlist en las que se encuentran, y otras características de su música ")
#-----------------------------Modelo 1------------------------------#
def mostrar_comparacion():
    st.header("Modelo 1")
    st.write("Comparación de los datos de Airbnb en Amsterdam en 2016 y 2023")
    col1, col2 = st.columns(2)

    with col1:
        st.image('imagenes/7barrios+airbnbt.png', use_column_width=True)
        st.image('imagenes/output2.png', use_column_width=True)
        
    with col2:
        st.image('imagenes/output_copy_2.png', use_column_width=True)
#------------------------------MAPA------------------------------#

#####################################################################
with st.sidebar:
    st.image("/Users/aguedagambon/Bootcamp/Github/Spotify_analisis/imagenes/spotifylogo.png", use_column_width=True, width=100)
    st.write("## Navegación")
    diapositiva = st.radio(
        "Selecciona una Diapositiva",
        ("Introducción", "EDA", "Power BI", "Modelo de predicción"))

funciones_diapositivas = {
    "Introducción": mostrar_introduccion,
    "EDA": mostrar_eda,
    "Power BI": mostrar_powerbi,
    "Modelo de predicción": mostrar_comparacion,

}
funciones_diapositivas[diapositiva]()