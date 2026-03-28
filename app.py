import streamlit as st
from PIL import Image
import time

# --- НАСТРОЙКА СТИЛЯ (UI/UX) ---
st.set_page_config(page_title="AI-ColoScan PRO", layout="wide", initial_sidebar_state="expanded")

# Кастомный CSS для "крутого" вида
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #161b22; border-radius: 4px 4px 0 0; color: white; padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] { background-color: #238636 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- БОКОВАЯ ПАНЕЛЬ ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2413/2413110.png", width=80)
    st.title("Система управления")
    st.markdown("---")
    uploaded_file = st.file_uploader("📥 Загрузить снимок (JPG/PNG)", type=['jpg', 'png', 'jpeg'])
    st.markdown("---")
    st.write("🛰 **Server Status:** <span style='color: #238636'>Connected</span>", unsafe_allow_html=True)
    st.write("🧠 **Model:** YOLOv8-SEG (Kvasir)")

# --- ГЛАВНЫЙ ИНТЕРФЕЙС ---
st.title("🩺 AI-ColoScan: Интеллектуальный Эндоскопический Ассистент")

# Вкладки для разных разделов проекта
tab1, tab2, tab3 = st.tabs(["🔍 Анализ в реальном времени", "📊 Метрики обучения", "🧪 О проекте"])

with tab1:
    if uploaded_file:
        col1, col2 = st.columns(2)
        img = Image.open(uploaded_file)
        
        with col1:
            st.markdown("### Исходный кадр")
            st.image(img, use_container_width=True)
            
        with col2:
            st.markdown("### Обработка ИИ")
            with st.spinner('Сервер анализирует изображение...'):
                time.sleep(1) # Имитация задержки сервера
                # Сюда мы вставим вывод с сервера ребят
                st.image(img, use_container_width=True) 
                st.success("Объект обнаружен: Полип (Вероятность 94.2%)")

        # Метрики под картинками
        st.markdown("---")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Тип патологии", "Полип", "Аденома")
        m2.metric("Приблизительный размер", "12.4 мм", "+0.5мм")
        m3.metric("Уверенность ИИ", "94.2%", "High")
        m4.metric("Скорость (Latency)", "18ms", "Real-time")
    else:
        st.info("Пожалуйста, загрузите снимок в боковой панели для начала анализа.")

with tab2:
    st.header("Результаты обучения (ML Analytics)")
    st.write("Данные получены из Google Colab и Roboflow.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("#### Матрица ошибок (Confusion Matrix)")
        # Здесь должен быть скриншот из вашего Colab
        st.image("https://raw.githubusercontent.com/ultralytics/yolov5/master/data/images/bus.jpg", caption="Пример графика обучения")
    
    with col_b:
        st.write("#### Распределение данных (Roboflow)")
        st.bar_chart({"Полипы": 2092, "Воспаления": 450, "Норма": 742})

with tab3:
    st.markdown("""
    ### iGEM Project: AI-ColoScan
    Наша миссия — снизить процент пропусков патологий во время колоноскопии.
    - **Dataset:** Kvasir-SEG (2392 изображения).
    - **Hardware:** Анализ проводится на удаленном GPU сервере.
    - **Frontend:** Интерактивный дашборд для врача.
    """)
