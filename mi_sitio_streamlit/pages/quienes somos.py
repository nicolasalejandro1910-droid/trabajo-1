import streamlit as st

# Información ficticia para la página de "Quiénes somos"
st.title("Sobre Nosotras")

st.markdown("---")

st.header("Nuestra pasión por los aromas")

st.write("""
**Fragrances IeJ S.A.** Es una empresa ficticia dedicada a la divulgación de la cultura del perfume. Fundada en 2025 por una perfumistas y amantes de las fragancias con el único propósito de compartir conocimientos y secretos sobre este arte.

Nuestro equipo está compuesto por:
* **Javiera:** Perfumista experta.
* **Maria** Social Management.
* **Patricia** Creadora de contenido digital.

""")
st.warning("Toda la información y los perfumes son exclusivos de la dueña.")
import streamlit as st

# Reemplaza la URL de ejemplo con el enlace de tu imagen
url_de_la_imagen = "https://github.com/nicolasalejandro1910-droid/trabajo-1/blob/main/mi_sitio_streamlit/assets/foto1.jpg?raw=true"

# Muestra la imagen directamente desde la URL
st.image(url_de_la_imagen, caption="Una imagen desde un enlace")






