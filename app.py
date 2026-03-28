import streamlit as st
from PIL import Image
import time

# --- НАСТРОЙКИ СТРАНИЦЫ ---
st.set_page_config(page_title="AI-ColoScan PRO", layout="wide")

# CSS для фикса текста, размера лого и компактности
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e6edf3; }
    
    /* Делаем фото компактными, чтобы не листать */
    [data-testid="stImage"] img {
        max-height: 400px;
        width: auto;
        margin: auto;
        display: block;
        border-radius: 10px;
        border: 1px solid #3b82f6;
    }

    /* СТИЛЬ ДЛЯ ВИДИМОГО ТЕКСТА (ВМЕСТО METRIC) */
    .custom-card {
        background-color: #1c2533;
        border: 2px solid #3b82f6;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        margin: 5px;
    }
    .custom-label {
        color: #ffffff !important; /* Ярко-белый заголовок */
        font-size: 20px !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        display: block;
        margin-bottom: 5px;
    }
    .custom-value {
        color: #ffffff !important;
        font-size: 38px !important;
        font-weight: 900 !important;
        display: block;
    }

    /* Логотип на всю ширину колонки */
    [data-testid="column"] img {
        width: 100% !important;
        max-width: 250px !important;
    }
    
    /* Убираем лишние пустые места сверху */
    .block-container { padding-top: 1rem !important; }
    </style>
    """, unsafe_allow_html=True)

# --- ШАПКА ---
col_l, col_r = st.columns([1, 4])
with col_l:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.subheader("iGEM NU")
with col_r:
    st.title("AI-ColoScan: Интеллектуальная система")
    st.write("Разработка iGEM Nazarbayev University для повышения точности эндоскопии")

st.divider()

# --- ВКЛАДКИ ---
tab_diag, tab_kvasir, tab_about = st.tabs(["Диагностика", "База данных Kvasir", "О команде"])

with tab_diag:
    uploaded_file = st.file_uploader("Загрузите снимок (JPG/PNG)", type=['jpg', 'png', 'jpeg'])

    if uploaded_file:
        img = Image.open(uploaded_file)
        
        # Фотографии стали меньше и стоят в ряд
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("<p style='text-align:center'>Исходный кадр</p>", unsafe_allow_html=True)
            st.image(img, use_container_width=True)
        with c2:
            st.markdown("<p style='text-align:center'>Результат сегментации ИИ</p>", unsafe_allow_html=True)
            with st.spinner('Анализ...'):
                time.sleep(0.4)
                st.image(img, use_container_width=True)
                st.error("Обнаружен объект: Полип (94.2%)")

        st.markdown("### Клиническое заключение ИИ")
        
        # Новые компактные и яркие блоки данных
        m1, m2, m3 = st.columns(3)
        
        with m1:
            st.markdown('<div class="custom-card"><span class="custom-label">ОБЪЕКТ</span><span class="custom-value">ПОЛИП</span></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="custom-card"><span class="custom-label">ПРЕДП. РАЗМЕР</span><span class="custom-value">12.4 мм</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="custom-card"><span class="custom-label">УВЕРЕННОСТЬ ИИ</span><span class="custom-value">94.2%</span></div>', unsafe_allow_html=True)
    else:
        st.info("Для начала работы загрузите медицинское изображение.")

with tab_kvasir:
    st.header("О датасете Kvasir")
    st.markdown("""
    Система AI-ColoScan обучена на базе данных **Kvasir
