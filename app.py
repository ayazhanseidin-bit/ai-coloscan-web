import streamlit as st
from PIL import Image
import time

# --- CONFIG ---
st.set_page_config(page_title="AI-ColoScan Professional", layout="wide")

# --- HEADER AREA (Логотип, который не исчезнет) ---
# Создаем две колонки: узкую для лого и широкую для текста
head_col1, head_col2 = st.columns([1, 6])

with head_col1:
    try:
        # Пробуем загрузить логотип
        st.image("logo.png", width=120)
    except:
        # Если файла еще нет, просто оставляем место
        st.write("Team Logo")

with head_col2:
    st.title("AI-ColoScan: Clinical Decision Support System")
    st.markdown("Precision analysis of colorectal pathologies using instance segmentation.")

st.divider() # Линия отделения шапки от контента

# --- SIDEBAR (Теперь здесь только настройки) ---
with st.sidebar:
    st.markdown("### Team AI-ColoScan")
    st.markdown("**Architecture:** YOLOv8-SEG")
    st.markdown("**Dataset:** Kvasir-SEG")
    st.success("Server Status: Online")

# --- REST OF THE CODE (Загрузка файла и вкладки) ---
uploaded_file = st.file_uploader("", type=['jpg', 'png', 'jpeg'])

# ... (далее идет твой код с вкладками без изменений)
