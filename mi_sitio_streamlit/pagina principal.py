#Librería de Streamlit
import streamlit as st
import os

#Titulo e icono
st.set_page_config(
    page_title="El Universo de los Perfumes",
    page_icon="🌸",
    layout="wide"
)
# Título de la página principal
st.title("🌸 El Universo de los Perfumes Femeninos 🌸")

#Presentación
st.write("¡Bienvenida a un viaje sensorial por el fascinante mundo de las fragancias! Aquí descubrirás las historias, familias olfativas y secretos detrás de los perfumes más icónicos.")

st.markdown("---") # Separador
import streamlit as st
import os

# Si la imagen es local

# Si la imagen es desde una URL
url_de_la_imagen = "https://github.com/nicolasalejandro1910-droid/trabajo-1/blob/main/mi_sitio_streamlit/assets/foto1.jpg?raw=true"
st.image(url_de_la_imagen, width=600, caption="Imagen de referencia")

# Imagenes de la carpeta 'assets'
st.header("¿Por qué elegir un perfume?")

# Textos
st.write("Un perfume es mucho más que un aroma; es una declaración de estilo, un recuerdo y una extensión de tu personalidad. Cada fragancia cuenta una historia diferente en la piel de quien la lleva.")

# Interacción con el usuario
if st.button("¡Haz clic para una curiosidad sobre perfumes!"):
    st.info("¿Sabías que la palabra 'perfume' proviene del latín 'per fumum', que significa 'a través del humo'?")





