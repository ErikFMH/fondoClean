import streamlit as st
from PIL import Image
from rembg import remove
import io
import os

def prcs_ima(imagenSub):
    image = Image.open(imagenSub)
    prcs_ima = rem_bckgr(image)
    return prcs_ima

def rem_bckgr(image):
    image_byte = io.BytesIO()
    image.save(image_byte, format = "PNG")
    image_byte.seek(0)
    prcs_ima_bytes = remove(image_byte.read())
    return Image.open(io.BytesIO(prcs_ima_bytes))

st.header("Removedor de fondos.jpg")
st.subheader("Sube la imagen")
imagenSub = st.file_uploader("Elige una imagen:", type = ["jpg", "jpeg", "png"])

if imagenSub is not None:
    st.image(imagenSub, caption = "Imagen Subida", use_column_width = True)
    remover = st.button(label = "Quitar Fondo")

    if remover:
        prcsd_ima = prcs_ima(imagenSub)
        st.image(prcsd_ima, caption = "Fondo Eliminado", use_column_width = True)
        prcsd_ima.save("prcsd_ima.png")
        with open("prcsd_ima.png", "rb") as f:
            image_data = f.read()
        st.download_button("Descargar Imagen Procesada", data = image_data, file_name = "prcsd_ima.png")
        os.remove("prcsd_ima.png")