import streamlit as st
from PIL import Image
from ultralytics import YOLO
import numpy as np

# Загрузка модели
@st.cache_resource
def load_model():
    return YOLO('kvasir+polypDB.pt')

model = load_model()

# --- ТВОЙ CSS ДИЗАЙН ---
st.markdown("""<style>...</style>""", unsafe_allow_html=True) # Оставь свой CSS здесь

# --- ДИАГНОСТИКА ---
# (В блоке анализа замени старую логику на эту)
if uploaded_file:
    img = Image.open(uploaded_file)
    results = model.predict(img, conf=0.3) # ИИ анализирует фото
    
    res_plotted = results[0].plot() # Рисуем рамки/маски
    st.image(res_plotted, channels="BGR", use_container_width=True)
    
    if len(results[0].boxes) > 0:
        st.error("Полип обнаружен")
    else:
        st.success("Патологий не найдено")
