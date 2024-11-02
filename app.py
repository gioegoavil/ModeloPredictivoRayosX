# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZTkcKZWkKlsGPmP6JRRnN_2yuiEZYAnL
"""

with open("app.py", "w") as f:
    f.write('''
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Título y descripción de la aplicación
st.title("Clasificación de Neumonía en Rayos X Pediátricos")
st.write("Esta aplicación utiliza un modelo de deep learning para predecir si una imagen de rayos X muestra signos de neumonía.")

# Cargar el modelo preentrenado
@st.cache_resource  # Usa caché para cargar el modelo solo una vez
def load_model():
    model = tf.keras.models.load_model("modelo_neumonia.h5")
    return model

# Mostrar mensaje de carga del modelo
st.text("TensorFlow version: " + tf.__version__)
st.success("Modelo cargado correctamente.")

model = load_model()

# Función para procesar la imagen y realizar la predicción
def predict(image_data, model):
    # Convertir la imagen a RGB si no está en ese formato
    if image_data.mode != "RGB":
        image_data = image_data.convert("RGB")

    # Redimensionar la imagen a 224x224 píxeles y normalizarla
    img = image_data.resize((224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Expande a 4 dimensiones para el modelo

    # Realizar la predicción
    prediction = model.predict(img_array)[0][0]

    # Interpreta la predicción
    if prediction > 0.5:
        return "Neumonía", prediction
    else:
        return "Normal", prediction

# Cargar la imagen del usuario
uploaded_file = st.file_uploader("Sube una imagen de rayos X en formato JPG o PNG", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Mostrar la imagen cargada
    image_data = Image.open(uploaded_file)
    st.image(image_data, caption="Imagen cargada", use_column_width=True)

    # Realizar la predicción
    label, confidence = predict(image_data, model)

    # Mostrar el resultado de la predicción con estilo
    if label == "Neumonía":
        st.error(f"El modelo predice que la imagen es de un caso de **{label}**.")
    else:
        st.success(f"El modelo predice que la imagen es de un caso **{label}**.")

    st.write(f"Confianza de la predicción: **{confidence:.2f}**")
    ''')