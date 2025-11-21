import streamlit as st
import requests
import json
import numpy as np

st.title("API de Predicción del Modelo Iris")
st.write("Introduce las características para obtener la predicción:")

sepal_length = st.slider('Longitud del sépalo', 0.0, 10.0, 5.0)
sepal_width = st.slider('Anchura del sépalo', 0.0, 10.0, 3.0)
petal_length = st.slider('Longitud del pétalo', 0.0, 10.0, 4.0)
petal_width = st.slider('Anchura del pétalo', 0.0, 10.0, 1.0)

if st.button("Obtener Predicción"):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    data = {"features": features}

    # Leer API_URL desde variable de entorno
    import os
    api_url = os.environ.get("API_URL", "http://localhost:5000/predict")

    try:
        response = requests.post(api_url,
                                 data=json.dumps(data),
                                 headers={"Content-Type": "application/json"})

        if response.status_code == 200:
            pred = response.json()['prediction']
            species = {0:"Setosa",1:"Versicolor",2:"Virginica"}[pred]
            st.success(f"Predicción: {species}")
        else:
            st.error(response.text)

    except Exception as e:
        st.error(str(e))
