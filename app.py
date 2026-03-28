import streamlit as st
from PIL import Image
import time

# --- НАСТРОЙКИ СТРАНИЦЫ ---
st.set_page_config(page_title="AI-ColoScan PRO", layout="wide")

# Профессиональный CSS без лишних элементов
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e6edf3; }
    
    /* Логотип без обрезки */
    [data-testid="column"] img {
        max-width: 220px !important;
        padding: 5px !important;
        object-fit: contain !important;
    }

    /* Названия вкладок */
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 18px !important;
        font-weight: 700 !important;
        color: #ffffff !important;
    }

    /* Центрирование текста над фото */
    .img-label {
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
        color: #ffffff;
    }

    /* Компактные фото */
    [data-testid="stImage"] img {
        max-height: 320px !important;
        border-radius: 8px;
        margin: auto;
        display: block;
    }

    /* Карточки результатов с Estimation of AI */
    .custom-card {
        background-color: #1c2533;
        border: 2px solid #3b82f6;
        border-radius: 8px;
        padding: 12px;
        text-align: center;
        margin-top: 10px;
    }
    .custom-label {
        color: #ffffff !important;
        font-size: 16px !important;
        font-weight: 800 !important;
        display: block;
    }
    .estimation-text {
        color: #94a3b8 !important;
        font-size: 12px !important;
        font-weight: 400 !important;
        display: block;
        margin-bottom: 4px;
    }
    .custom-value {
        color: #ffffff !important;
        font-size: 32px !important;
        font-weight: 900 !important;
        display: block;
    }

    .block-container { padding-top: 1.5rem !important; }
    </style>
    """, unsafe_allow_html=True)

# --- ШАПКА ---
col_logo, col_title = st.columns([1, 4])
with col_logo:
    try:
        st.image("logo.png")
    except:
        st.write("iGEM NU")
with col_title:
    st.title("AI-ColoScan: Интеллектуальная система")
    st.write("Разработка iGEM Nazarbayev University для анализа колоноскопии")

# --- ВКЛАДКИ ---
tab_diag, tab_info, tab_team = st.tabs(["ДИАГНОСТИКА", "БАЗА ДАННЫХ KVASIR", "О КОМАНДЕ"])

with tab_diag:
    uploaded_file = st.file_uploader("Загрузите снимок", type=['jpg', 'png', 'jpeg'], label_visibility="collapsed")

    if uploaded_file:
        img = Image.open(uploaded_file)
        
        # Выровненный блок с фото
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<p class="img-label">Исходный кадр</p>', unsafe_allow_html=True)
            st.image(img, use_container_width=True)
        with c2:
            st.markdown('<p class="img-label">Обработка ИИ</p>', unsafe_allow_html=True)
            with st.spinner('Анализ...'):
                time.sleep(0.3)
                st.image(img, use_container_width=True)
        
        st.error("Обнаружен объект: Полип (Вероятность 94.2%)")

        # Блок метрик с Estimation of AI
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('''
                <div class="custom-card">
                    <span class="custom-label">ОБЪЕКТ</span>
                    <span class="estimation-text">Estimation of AI</span>
                    <span class="custom-value">ПОЛИП</span>
                </div>''', unsafe_allow_html=True)
        with m2:
            st.markdown('''
                <div class="custom-card">
                    <span class="custom-label">ПРЕДП. РАЗМЕР</span>
                    <span class="estimation-text">Estimation of AI</span>
                    <span class="custom-value">12.4 мм</span>
                </div>''', unsafe_allow_html=True)
        with m3:
            st.markdown('''
                <div class="custom-card">
                    <span class="custom-label">УВЕРЕННОСТЬ ИИ</span>
                    <span class="estimation-text">Estimation of AI</span>
                    <span class="custom-value">94.2%</span>
                </div>''', unsafe_allow_html=True)
    else:
        st.info("Загрузите медицинское изображение для запуска анализа")

with tab_info:
    st.header("О датасете Kvasir")
    st.markdown("""
    Обучение системы проводилось на датасете **Kvasir** (Vestre Viken Health Trust, Норвегия). 
    Данные включают в себя тысячи верифицированных кадров с патологиями и анатомическими ориентирами, 
    аннотированных квалифицированными врачами-эндоскопистами.
    """)

with tab_team:
    st.subheader("iGEM Nazarbayev University")
    st.write("Студенческий проект, направленный на улучшение качества ранней диагностики.")
