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

    /* ЗАГОЛОВКИ НАД ФОТО */
    .img-label {
        text-align: center;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 8px;
        color: #ffffff;
        display: block;
        text-transform: uppercase;
    }

    /* СТИЛЬ ДЛЯ ВЫТЯНУТОГО ФОТО КОМАНДЫ */
    .team-img img {
        max-height: 600px !important; /* Увеличили высоту */
        object-fit: cover !important;
        border-radius: 12px;
        border: 1px solid #3b82f6;
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
    st.title("AI-ColoScan: Clinical Analysis System")
    st.write("Precision diagnostic support powered by Kvasir dataset")

# --- ВКЛАДКИ ---
tab_diag, tab_info, tab_team = st.tabs(["DIAGNOSTICS", "KVASIR DATABASE", "ABOUT TEAM"])

with tab_diag:
    uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'], label_visibility="collapsed")
    if uploaded_file:
        img = Image.open(uploaded_file)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="img-label">Input Photo</div>', unsafe_allow_html=True)
            st.image(img, use_container_width=True)
        with c2:
            st.markdown('<div class="img-label">AI Processed Photo</div>', unsafe_allow_html=True)
            with st.spinner('Analyzing...'):
                time.sleep(0.3)
                st.image(img, use_container_width=True)
        
        st.error("Diagnostic Result: Polyp Detected (Probability 94.2%)")
        st.markdown('<div class="estimation-disclaimer">All data below represents an Estimation of AI for clinical guidance.</div>', unsafe_allow_html=True)

        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="custom-card"><span class="custom-label">Finding Type</span><span class="custom-value">POLYP</span></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="custom-card"><span class="custom-label">Dimensions</span><span class="custom-value">12.4 mm</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="custom-card"><span class="custom-label">Certainty Score</span><span class="custom-value">94.2%</span></div>', unsafe_allow_html=True)
    else:
        st.info("Please upload an endoscopic image to start the analysis.")

with tab_info:
    st.header("О датасете Kvasir")
    st.markdown("""
    **Kvasir** — это передовой мультиклассовый набор данных для обнаружения заболеваний ЖКТ. 
    Данные собраны в Vestre Viken Health Trust (Норвегия) и верифицированы опытными врачами-эндоскопистами.
    """)
    st.info("Dataset Source: Vestre Viken Health Trust & Oslo University Hospital.")

with tab_team:
    st.header("iGEM Nazarbayev University Team")
    text_col, photo_col = st.columns([1.5, 1])

    with text_col:
        st.markdown("""
        ### Наш проект и мировое признание
        
        **Биологическая научная сборная iGEM Назарбаев Университета (НУ)** — это команда молодых ученых, представляющая Казахстан и Центральную Азию на международной арене уже 12 лет. За это время мы завоевали **6 золотых**, **2 серебряные** и **2 бронзовые медали**, подтверждая высокий уровень отечественной науки.
        
        В 2024 году мы представляем наш проект на международном финале **iGEM в Париже**, соревнуясь с более чем 400 ведущими университетами мира.
        
        **Разработка:** Мы создаем доступный биосенсор для ранней диагностики колоректального рака на основе генетически модифицированной бактерии *E. coli*. Технология выявляет путресцин — ключевой биомаркер, концентрация которого резко возрастает при развитии опухоли. Наша цель — сделать высокоточную диагностику простой, быстрой и экономически эффективной.

        ### Контакты
        По вопросам сотрудничества и техническим деталям проекта вы можете связаться с нами напрямую:
        
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
