import streamlit as st
import os

st.title("Familias Olfativas")

st.markdown("---")

st.header("Descubre tu familia olfativa")

# Carga y muestra de un video
st.write("La clasificación de perfumes se basa en las notas que los componen. Elegir una fragancia de tu familia olfativa favorita te asegura una conexión más profunda con el aroma.")

# Ejemplo de un widget de selección (select box)
familia = st.selectbox(
    'Selecciona una familia olfativa',
    ('Floral', 'Oriental', 'Cítrica', 'Chipre')
)

st.write(f'Seleccionaste la familia olfativa: **{familia}**.')
# Condicional para explicar la familia olfativa seleccionada
if familia == 'Floral':
    st.info("La familia floral es la más popular. Sus fragancias se componen de notas de flores como rosas, jazmines y lirios.")
if familia == 'Cítrica':
    st.info("La familia cítrica es fresca y energizante, perfecta para climas cálidos. Sus fragancias se componen de notas brillantes y jugosas como limón, bergamota y mandarina.")
if familia == 'Oriental':
    st.info("La familia Oriental es conocida por sus aromas cálidos y exóticos. Sus fragancias se componen de notas ricas como vainilla, especias y resinas.")
if familia == 'Chipre':
    st.info("La familia chipre es clásica y sofisticada. Sus fragancias se componen de notas de contraste entre la frescura cítrica de la salida y una base amaderada y musgosa.")
# Más contenido multimedia y widgets
st.header("Componentes de una fragancia")
st.write("Los perfumes se construyen en una pirámide olfativa con notas de salida, corazón y fondo. Las primeras son las que hueles al aplicar, las del corazón se revelan después, y las de fondo son las que perduran.")
import streamlit as st
import os

# Si la imagen es local

# Si la imagen es desde una URL
url_de_la_imagen = "https://github.com/nicolasalejandro1910-droid/trabajo-1/blob/main/mi_sitio_streamlit/assets/foto1.jpg?raw=true"
st.image(url_de_la_imagen, width=600, caption="Imagen de referencia")

















