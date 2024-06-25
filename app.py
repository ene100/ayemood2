import streamlit as st

# Configura la página
st.set_page_config(
    page_title="Ayemood",  # Cambia esto al título que desees
    page_icon=":heart_eyes:",  # Puedes cambiar esto a la URL de tu favicon si tienes uno específico
    layout="centered"
)

# Título de la aplicación
st.title("AYEMOOD")

# Input para el emoji
emoji = st.text_input("Introduce un emoji:", value="😍")

# Mostrar el emoji en el centro cuando se presiona el botón
if st.button('ACTUALIZAR'):
    st.markdown(f"<div style='text-align: center; font-size: 100px;'>{emoji}</div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div style='text-align: center; font-size: 100px;'>{emoji}</div>", unsafe_allow_html=True)

# Quitar la marca de agua y el menú de Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
