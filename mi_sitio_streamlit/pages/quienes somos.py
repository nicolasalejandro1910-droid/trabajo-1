import streamlit as st

# Información ficticia para la página de "Quiénes somos"
st.title("Sobre Nosotras")

st.markdown("---")

st.header("Nuestra pasión por los aromas")
st.image("https://images.unsplash.com/photo-1596707328224-d2e8b26e64c3", caption="Equipo de Ficticia Fragrances S.A.")

st.write("""
**Fragrances IeJ S.A.** Es una empresa ficticia dedicada a la divulgación de la cultura del perfume. Fundada en 2025 por una perfumistas y amantes de las fragancias con el único propósito de compartir conocimientos y secretos sobre este arte.

Nuestro equipo está compuesto por:
* **Javiera:** Perfumista experta.
* **Maria** Social Management.
* **Patricia** Creadora de contenido digital.

""")
st.warning("Toda la información y los perfumes son exclusivos de la dueña.")

