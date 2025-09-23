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

# Más contenido multimedia y widgets
st.header("Componentes de una fragancia")
st.write("Los perfumes se construyen en una pirámide olfativa con notas de salida, corazón y fondo. Las primeras son las que hueles al aplicar, las del corazón se revelan después, y las de fondo son las que perduran.")







