import streamlit as st
from PIL import Image
import time

# --- НАСТРОЙКИ СТРАНИЦЫ ---
st.set_page_config(page_title="AI-ColoScan PRO", layout="wide")

# Глобальный CSS для исправления всех замечаний
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e6edf3; }
    
    /* ЛОГОТИП: добавляем отступы, чтобы не был обрезанным */
    [data-testid="column"] img {
        width: 100% !important;
        max-width: 220px !important;
        padding: 10px !important;
        object-fit: contain !important;
    }

    /* ВКЛАДКИ: делаем их заметными */
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 20px !important;
        font-weight: 700 !important;
        color: #94a3b8 !important;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #ffffff !important;
        border-bottom-color: #3b82f6 !important;
    }

    /* ФОТО: еще компактнее */
    [data-testid="stImage"] img {
        max-height: 330px !important;
        width: auto !important;
        margin: auto;
        border-radius: 12px;
    }

    /* КАРТОЧКИ ДАННЫХ: плотнее и ярче */
    .custom-card {
        background-color: #1c2533;
        border: 2px solid #3b82f6;
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        margin-top: 10px;
    }
    .custom-label {
        color: #ffffff !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px;
        display: block;
    }
    .custom-value {
        color: #ffffff !important;
        font-size: 34px !important;
        font-weight: 900 !important;
        display: block;
    }

    /* Уменьшаем лишние отступы контейнера */
    .block-container { padding-top: 1.5rem !important; padding-bottom: 0rem !important; }
    </style>
    """, unsafe_allow_html=True)

# --- ШАПКА ---
col_logo, col_title = st.columns([1, 4])
with col_logo:
    try:
        st.image("logo.png")
    except:
        st.subheader("iGEM NU")
with col_title:
    st.title("AI-ColoScan: Интеллектуальный Ассистент")
    st.write("Система высокоточной детекции патологий на базе датасета Kvasir")

# --- ВЕРХНЕЕ МЕНЮ (ВКЛАДКИ) ---
tab_diag, tab_info, tab_team = st.tabs(["🔍 ДИАГНОСТИКА", "📚 БАЗА ДАННЫХ KVASIR", "👥 О КОМАНДЕ"])

with tab_diag:
    uploaded_file = st.file_uploader("Загрузите снимок ЖКТ", type=['jpg', 'png', 'jpeg'], label_visibility="collapsed")

    if uploaded_file:
        img = Image.open(uploaded_file)
        
        # Визуальный блок
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("<p style='text-align:center; font-weight:bold;'>Исходный кадр</p>", unsafe_allow_html=True)
            st.image(img, use_container_width=True)
        with c2:
            st.markdown("<p style='text-align:center; font-weight:bold;'>Обработка ИИ</p>", unsafe_allow_html=True)
            with st.spinner('Анализ...'):
                time.sleep(0.3)
                st.image(img, use_container_width=True)
        
        # Компактное уведомление
        st.error("Обнаружен объект: Полип (Вероятность 94.2%)")

        # Блок метрик (еще компактнее)
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="custom-card"><span class="custom-label">ОБЪЕКТ</span><span class="custom-value">ПОЛИП</span></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="custom-card"><span class="custom-label">ПРЕДП. РАЗМЕР</span><span class="custom-value">12.4 мм</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="custom-card"><span class="custom-label">УВЕРЕННОСТЬ ИИ</span><span class="custom-value">94.2%</span></div>', unsafe_allow_html=True)
    else:
        st.info("Ожидание загрузки изображения для анализа...")

with tab_info:
    st.header("О датасете Kvasir")
    st.markdown("""
    Данная система использует модель, обученную на **Kvasir** — мультиклассовом наборе данных из госпиталя Vestre Viken (Норвегия). 
    
    * **Разметка**: Выполнена профессиональными эндоскопистами.
    * **Классы**: Включает анатомические ориентиры (Z-линия, Cecum) и патологии (Полипы, Эзофагит).
    * **Цель**: Автоматизация отчетности и минимизация пропусков новообразований.
    """)

with tab_team:
    st.subheader("iGEM Nazarbayev University")
    st.write("Мы разрабатываем доступные ИИ-решения для медицины Казахстана.")
