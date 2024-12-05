# Clasificación de Neumonía en Rayos X Pediátricos usando Transfer Learning o Modelos Personalizados

## Descripción

Este proyecto tiene como objetivo clasificar imágenes de rayos X pediátricos para determinar si un niño tiene neumonía o no. Se utiliza el **Pediatric Pneumonia Chest X-ray Dataset**, que contiene 5,856 imágenes etiquetadas como "pneumonia" o "normal". Los estudiantes pueden elegir entre aplicar **Transfer Learning** utilizando modelos preentrenados o entrenar sus propias redes neuronales convolucionales (CNN) personalizadas.

## Dataset

El dataset utilizado en este proyecto es el [Pediatric Pneumonia Chest X-ray Dataset](https://www.kaggle.com/competitions/sci-pediatric-chest-x-ray-pneumonia-classification/overview), el cual contiene radiografías de tórax pediátricas etiquetadas en dos categorías:
- **Pneumonia**
- **Normal**

Este dataset presenta desafíos adicionales debido a las diferencias fisiológicas en los niños y la dificultad de obtener imágenes de rayos X pediátricos de manera estándar, lo que lo convierte en un recurso valioso para desarrollar modelos de clasificación especializados.

## Tecnologías Utilizadas

- **Python**
- **TensorFlow / Keras**
- **OpenCV**
- **Streamlit** (para la interfaz web)
- **Transfer Learning** (ResNet, VGG, Inception, entre otros)

## Instalación

Para instalar las dependencias necesarias, utiliza el siguiente comando:

```bash
pip install -r requirements.txt
