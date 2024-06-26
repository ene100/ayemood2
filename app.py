import streamlit as st

# Título de la aplicación
st.title("AYEMETER")

# Función para actualizar el estado del emoji
def actualizar_emoji():
    st.session_state['emoji'] = st.session_state['input_emoji']

# Campo de entrada para el emoji
if 'emoji' not in st.session_state:
    st.session_state['emoji'] = '😍'

emoji = st.text_input("Introduce un emoji:", value=st.session_state['emoji'], key='input_emoji')

# Botón para actualizar el emoji
if st.button('ACTUALIZAR'):
    actualizar_emoji()

# Mostrar el emoji en el centro
st.markdown(f"<div style='text-align: center; font-size: 100px;'>{st.session_state['emoji']}</div>", unsafe_allow_html=True)

# Ocultar la marca de agua y el menú de Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
