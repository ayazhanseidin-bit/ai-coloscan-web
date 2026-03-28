import streamlit as st
from PIL import Image
import time

# --- CONFIG ---
st.set_page_config(page_title="AI-ColoScan PRO", layout="wide")

# Кастомный стиль (убираем лишние отступы и настраиваем цвета)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border: 1px dotted #3b82f6; }
    /* Стиль для области загрузки */
    div[data-testid="stFileUploader"] {
        border: 2px dashed #3b82f6;
        padding: 20px;
        border-radius: 15px;
        background-color: #161b22;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Только статус) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2413/2413110.png", width=80)
    st.title("System Status")
    st.markdown("---")
    st.success("🛰 Server: Connected")
    st.info("🧠 Model: YOLOv8-SEG")
    st.write("Current version: 2.1.0-beta")

# --- MAIN WINDOW ---
st.title("🩺 AI-ColoScan: Интеллектуальный Ассистент")
st.markdown("Загрузите снимок для мгновенного анализа патологий ЖКТ")

# 1. ЗАГРУЗКА В ГЛАВНОМ ОКНЕ
uploaded_file = st.file_uploader("", type=['jpg', 'png', 'jpeg'], help="Drag and drop your endoscopy frames here")

st.divider()

if uploaded_file:
    # Если файл загружен, показываем вкладки и анализ
    tab1, tab2, tab3 = st.tabs(["🔍 Анализ", "📊 Метрики", "🧪 О проекте"])
    
    with tab1:
        img = Image.open(uploaded_file)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Исходный кадр")
            st.image(img, use_container_width=True)
            
        with col2:
            st.markdown("### Обработка ИИ")
            with st.spinner('Связь с сервером...'):
                time.sleep(1) # Имитация работы
                st.image(img, use_container_width=True) # Здесь будет маска
                st.success("Объект обнаружен: Polyp (94.2%)")

        st.markdown("---")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Тип", "Полип", "Аденома")
        m2.metric("Размер", "12.4 мм", "+0.5мм")
        m3.metric("Уверенность", "94.2%")
        m4.metric("Latency", "18ms")

else:
    # Что видит пользователь, когда ничего не загружено
    st.info("👆 Начните с загрузки изображения выше, чтобы запустить нейронную сеть.")
    
    # Можно добавить красивую инфографику или примеры
    st.image("https://images.unsplash.com/photo-1576091160550-2173dad99901?auto=format&fit=crop&q=80&w=1000", 
             caption="Example of Endoscopic Visual Intelligence", use_container_width=True)
