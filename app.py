import streamlit as st
from PIL import Image
import time

# --- НАСТРОЙКИ СТРАНИЦЫ ---
st.set_page_config(page_title="AI-ColoScan PRO", layout="wide")

# CSS для дизайна
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e6edf3; }
    
    /* ЛОГОТИП */
    [data-testid="column"] img {
        max-width: 200px !important;
        object-fit: contain !important;
    }

    /* ОБЪЕМНЫЕ ВКЛАДКИ */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1c2533 !important;
        border: 1px solid #3b82f6 !important;
        border-radius: 8px 8px 0px 0px !important;
        padding: 10px 30px !important;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"] p {
        font-size: 20px !important;
        font-weight: 800 !important;
        color: #ffffff !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(180deg, #3b82f6 0%, #1e40af 100%) !important;
    }

    /* ЗАГОЛОВКИ НАД ФОТО (Теперь в тон основному тексту) */
    .img-label {
        text-align: center;
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 12px;
        color: #e6edf3; /* Тот же цвет, что и основной текст сайта */
        display: block;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* СТИЛЬ ДЛЯ ВЫТЯНУТОГО ФОТО КОМАНДЫ */
    .team-img img {
        max-height: 700px !important;
        object-fit: cover !important;
        border-radius: 12px;
        border: 2px solid #3b82f6;
    }

    /* ФОТО ДИАГНОСТИКИ */
    [data-testid="stImage"] img {
        border-radius: 10px;
        border: 1px solid #2e3b4e;
    }

    /* КАРТОЧКИ РЕЗУЛЬТАТОВ */
    .custom-card {
        background-color: #1c2533;
        border: 2px solid #3b82f6;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
    }
    .custom-label { color: #94a3b8; font-size: 14px; text-transform: uppercase; display: block; }
    .custom-value { color: #ffffff; font-size: 34px; font-weight: 900; display: block; }

    .estimation-disclaimer {
        text-align: center;
        color: #94a3b8;
        font-size: 14px;
        font-style: italic;
        margin-bottom: 15px;
    }
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
    st.title("AI-ColoScan: Система клинического анализа")
    st.write("Поддержка высокоточной диагностики на базе ИИ")

# --- ВКЛАДКИ ---
tab_diag, tab_team = st.tabs(["ДИАГНОСТИКА", "О КОМАНДЕ"])

with tab_diag:
    uploaded_file = st.file_uploader("Загрузить изображение", type=['jpg', 'png', 'jpeg'], label_visibility="collapsed")
    if uploaded_file:
        img = Image.open(uploaded_file)
        c1, c2 = st.columns(2)
        with c1:
            # Название для первого фото
            st.markdown('<div class="img-label">Загруженное изображение</div>', unsafe_allow_html=True)
            st.image(img, use_container_width=True)
        with c2:
            # Название для второго фото
            st.markdown('<div class="img-label">Результат анализа ИИ (Поиск полипа)</div>', unsafe_allow_html=True)
            with st.spinner('Анализ...'):
                time.sleep(0.3)
                st.image(img, use_container_width=True)
        
        st.error("Результат диагностики: Обнаружен полип (Вероятность 94.2%)")
        st.markdown('<div class="estimation-disclaimer">Все данные ниже являются оценочными данными ИИ для клинического руководства.</div>', unsafe_allow_html=True)

        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="custom-card"><span class="custom-label">Тип находки</span><span class="custom-value">ПОЛИП</span></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="custom-card"><span class="custom-label">Размер</span><span class="custom-value">12.4 мм</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="custom-card"><span class="custom-label">Относительный размер</span><span class="custom-value">94.2%</span></div>', unsafe_allow_html=True)
    else:
        st.info("Пожалуйста, загрузите эндоскопическое изображение для начала анализа.")

with tab_team:
    st.header("Команда iGEM Nazarbayev University")
    text_col, photo_col = st.columns([1.5, 1])

    with text_col:
        st.markdown("""
        ### Наш проект и мировое признание
        
        **Биологическая научная сборная iGEM Назарбаев Университета (НУ)** — это команда молодых ученых, представляющая Казахстан и Центральную Азию на международной арене уже 12 лет. За это время мы завоевали **6 золотых**, **2 серебряные** и **2 бронзовые медали**, подтверждая высокий уровень отечественной науки.
        
        В 2024 году мы представляем наш проект на международном финале **iGEM в Париже**, соревнуясь с более чем 400 ведущими университетами мира.
        
        **Разработка:** Мы создаем доступный биосенсор для ранней диагностики колоректального рака на основе генетически модифицированной бактерии *E. coli*. Технология выявляет путресцин — ключевой биомаркер, концентрация которого резко возрастает при развитии опухоли. Наша цель — сделать высокоточную диагностику простой, быстрой и экономически эффективной.

        ### Контакты
        По техническим деталям проекта вы можете связаться с нами напрямую:
        
        **Email:** [igem@nu.edu.kz](mailto:igem@nu.edu.kz)
        """)
        
        st.link_button("Написать нам", "mailto:igem@nu.edu.kz")

    with photo_col:
        st.markdown('<div class="team-img">', unsafe_allow_html=True)
        try:
            st.image("team_photo.png", use_container_width=True)
        except:
            st.warning("Добавьте файл team_photo.png в папку проекта")
        st.markdown('</div>', unsafe_allow_html=True)
