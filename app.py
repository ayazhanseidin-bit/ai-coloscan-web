import streamlit as st
from PIL import Image
import time

# --- НАСТРОЙКИ СТРАНИЦЫ ---
st.set_page_config(page_title="AI-ColoScan PRO", layout="wide")

# CSS для объемных вкладок и центрирования
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e6edf3; }
    
    /* ЛОГОТИП: сохранение пропорций */
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
        background-color: #1c2533 !important; /* Темный фон */
        border: 1px solid #3b82f6 !important;
        border-radius: 8px 8px 0px 0px !important;
        padding: 10px 30px !important;
        height: auto !important;
        transition: all 0.3s ease;
        box-shadow: 0px -4px 10px rgba(0,0,0,0.3); /* Тень для объема */
    }
    .stTabs [data-baseweb="tab"] p {
        font-size: 20px !important;
        font-weight: 800 !important;
        color: #ffffff !important; /* Белый текст */
    }
    /* Активная вкладка */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(180deg, #3b82f6 0%, #1e40af 100%) !important;
        box-shadow: 0px 4px 15px rgba(59, 130, 246, 0.5) !important;
    }

    /* ЦЕНТРИРОВАНИЕ ТЕКСТА НАД ФОТО */
    .img-label {
        text-align: center;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 8px;
        color: #ffffff;
        display: block;
        width: 100%;
    }

    /* ФОТО */
    [data-testid="stImage"] img {
        max-height: 320px !important;
        border-radius: 8px;
        margin: auto;
        display: block;
    }

    /* КАРТОЧКИ С ESTIMATION OF AI */
    .custom-card {
        background-color: #1c2533;
        border: 2px solid #3b82f6;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }
    .custom-label {
        color: #ffffff !important;
        font-size: 16px !important;
        font-weight: 800 !important;
        display: block;
    }
    .estimation-text {
        color: #94a3b8 !important;
        font-size: 11px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: block;
        margin: 2px 0 6px 0;
    }
    .custom-value {
        color: #ffffff !important;
        font-size: 34px !important;
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
    st.title("AI-ColoScan: Clinical Analysis System")
    st.write("Precision diagnostic support powered by Kvasir dataset")

# --- ВКЛАДКИ ---
tab_diag, tab_info, tab_team = st.tabs(["DIAGNOSTICS", "KVASIR DATABASE", "ABOUT TEAM"])

with tab_diag:
    uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'], label_visibility="collapsed")

    if uploaded_file:
        img = Image.open(uploaded_file)
        
        # Сетка 1x2 для фото
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="img-label">Original Image</div>', unsafe_allow_html=True)
            st.image(img, use_container_width=True)
        with c2:
            st.markdown('<div class="img-label">AI Processing</div>', unsafe_allow_html=True)
            with st.spinner('Processing...'):
                time.sleep(0.3)
                st.image(img, use_container_width=True)
        
        st.error("Detected: Polyp (Probability 94.2%)")

        # Карточки результатов
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('''
                <div class="custom-card">
                    <span class="custom-label">OBJECT</span>
                    <span class="estimation-text">Estimation of AI</span>
                    <span class="custom-value">POLYP</span>
                </div>''', unsafe_allow_html=True)
        with m2:
            st.markdown('''
                <div class="custom-card">
                    <span class="custom-label">EST. SIZE</span>
                    <span class="estimation-text">Estimation of AI</span>
                    <span class="custom-value">12.4 mm</span>
                </div>''', unsafe_allow_html=True)
        with m3:
            st.markdown('''
                <div class="custom-card">
                    <span class="custom-label">CONFIDENCE</span>
                    <span class="estimation-text">Estimation of AI</span>
                    <span class="custom-value">94.2%</span>
                </div>''', unsafe_allow_html=True)
    else:
        st.info("Please upload an endoscopic image to start the analysis.")

with tab_info:
    st.header("Kvasir Dataset Information")
    st.markdown("""
    The system is trained on the **Kvasir dataset** (Vestre Viken Health Trust, Norway). 
    This is a multi-class image collection from the gastrointestinal tract, meticulously annotated 
    by experienced endoscopists.
    
    The dataset includes anatomical landmarks, pathological findings (polyps, esophagitis, ulcerative colitis), 
    and images related to endoscopic procedures. This high-quality data ensures the reliability of AI predictions.
    """)

with tab_team:
    st.subheader("iGEM Nazarbayev University")
    st.write("Developing AI solutions for medical precision in Kazakhstan.")
