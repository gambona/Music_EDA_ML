import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Popular music EDA",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="auto",
)
#------------------------------INTRODUCCIÓN------------------------------#
def mostrar_introduccion():
    st.header("Análisis 2024 hits musicales y predicción de su popularidad")
    st.write("Información:")
    
        
    with st.expander('Datos'):
        st.markdown("""
                    API de la aplicación de Spotify y otras plataformas, que proporciona información sobre las
                    """)
        st.markdown("4500 canciones más populares de 2024 en Spotify y su presencia en el resto de plataformas de música en streaming.")
        st.markdown("CSV obtenido de kaggle: [Visitar Kaggle](https://www.google.com)")
    
    with st.expander("Otros datos"):
        st.markdown("""Con 615 millones de usuarios, es la plataforma de audio más popular a nivel global, según muestran los datos de Stavia y la página oficial de Spotify  https://newsroom.spotify.com/company-info/ """)
        st.title("Número de suscriptores de servicios de música en streaming a nivel mundial durante el tercer trimestre de 2023, por plataforma")
        st.image("imagenes/Statista.jpg", use_column_width=True)

    st.image("imagenes/plataformas.png", use_column_width=True, width=50, caption="Desde Wikipedia")
        
#------------------------------EDA_2023------------------------------#

def mostrar_eda():

    st.header("Análisis Exploratorio de Datos (EDA)")
    st.write("Datos descriptivos sobre este dataset.")
    st.write("")
    st.header("Presencia de hits en las top plataformas de música en streaming")
    st.image('imagenes/1.png', use_column_width=True)
    st.write("")
    st.write("")
    st.header("Cómo de nuevas son las canciones más populares?")
    st.write("El 40.26% de las canciones más populares salieron en el último año.")
    st.image('imagenes/3.png', use_column_width=True)
    st.write("")
    st.header("Top 20 Artistas con más canciones en el top 2024")
    st.write("Taylor Swift, Drake y Bad Bunny se posicionan en el top, con más de 60 canciones populares, media mucho más alta qu la media de 28.5 del top 20")
    st.image('imagenes/2.png', use_column_width=True)
    st.write("")
    st.header("Canciones antiguas populares hoy")
    st.write("Encontramos 1 canción de los 80 como la má antigua popular hoy, 5 de los 90  y 4 de los 2000, con Eminem como top artisa con las 3 canciones más antiguas más populares a dia de hoy")
    st.image('imagenes/4.png', use_column_width=True)
    st.write("")
    st.header("Mapa de calor")
    st.header("Correlación entre las variables del dataframe")
    st.write("La correlación más significativa se encuentra entre el número total de reproduciones en Spotify y la cantidas de playlist en las que se encuentra la canción")
    st.image('imagenes/5.png', use_column_width=True)
    st.write("")
    st.write("")
    st.header("Diagrama de dispersión")
    st.write("Existe una relación postiva entre el número de reproducciones en Spotify y el número de playlist en las que se encuentra la canción")
    st.image('imagenes/6.png', use_column_width=True)
    st.write("Es por esto, que beneficia a los artistas que promocionar a los usuarios que guarden sus canciones en playlist, ya que de este modo se eleva la cantidad total de reproduciiones")
#------------------------------Power BI------------------------------#
def mostrar_powerbi():
    st.write("Power BI")  
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiNzRhZTMxZDMtMDlkNS00ZDQzLWEwOWYtNzRiM2NhYWI5NzE1IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
    st.markdown(f"""<iframe width="100%" height="600" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>""", unsafe_allow_html=True)
    st.write("En este panel interactivo podemos ver los artistas máss populares, la cantidad de playlist en las que se encuentran, y otras características de su música ")
#-----------------------------Modelo 1------------------------------#
def mostrar_ml():
    st.header("Características Youtube Views a través de modelo Random Forest")
    st.write("El objetivo de este modelo fue analizar las vistas de YouTube (YouTube Views) y que caracteriza a las canciones más populares en Youtube")
    st.write("Utilicé las variables numéricas de la data, y agrupé en 3 grupos o clusters para identificar patrones y reducir el número de observaciones únicas")
    tab1, tab2, tab3 = st.tabs(['Matriz de confusión','Distribución variables','Características'])
    with tab1:
        st.write("La curva ROC para cada clase muestra el rendimiento del modelo en términos de tasa de verdaderos positivos frente a tasa de falsos positivos")
        st.write("La curva ROC para cada clase muestra el rendimiento del modelo en términos de tasa de verdaderos positivos frente a tasa de falsos positivos")
        st.image('imagenes/7.png', use_column_width=True, width=100)
    with tab2:
        st.image('imagenes/9.png', use_column_width=True, width=100)
    with tab3:
        st.write("En el modelo de Random Forest, las importancias se normalizan para que sumen 1.")
        st.write("Los porcentajes de importancia nos dan una idea más clara del impacto relativo de cada característica en la predicción de las características de las canciones más populares en Youtube, con los datos dados.")
        col1, col2 = st.columns(2)
        with col1:
            st.image('imagenes/8.png', use_column_width=True, width=100)
        
#------------------------------Conclusión------------------------------#
def mostrar_conclusión():
    st.header("Recomendación a artistas:")
    st.image("imagenes/soundwave.png", use_column_width=True, width=100)
    st.write("Promocionar su música en Spotify, ya que es la plataforma con más usuarios y mayor presencia de hits")
    st.write("Alentar a usuarios a guardar sus canciones en Playllists")
    st.write("Asegurarse que su música se encuentra en Shazam")
#####################################################################

with st.sidebar:
    diapositiva = st.radio(
        "Índice",
        ("Introducción", "EDA", "Power BI", "Machine Learning", "Conclusión"))

funciones_diapositivas = {
    "Introducción": mostrar_introduccion,
    "EDA": mostrar_eda,
    "Power BI": mostrar_powerbi,
    "Machine Learning": mostrar_ml,
    "Conclusión": mostrar_conclusión

}
funciones_diapositivas[diapositiva]()