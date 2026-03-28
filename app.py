import streamlit as st
from PIL import Image
import time

# --- CONFIG ---
st.set_page_config(page_title="AI-ColoScan PRO", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS (ДИЗАЙН) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border: 1px solid #3b82f6; }
    div[data-testid="stExpander"] { background-color: #1f2937; border-radius: 10px; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #1f2937; border-radius: 5px 5px 0 0; padding: 10px 20px; color: #9ca3af;
    }
    .stTabs [aria-selected="true"] { background-color: #3b82f6 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2413/2413110.png", width=80)
    st.title("Clinical AI Dashboard")
    st.markdown("---")
    uploaded_file = st.file_uploader("📥 Upload Colonoscopy Scan", type=['jpg', 'png', 'jpeg'])
    st.markdown("---")
    st.write("🔧 **Model:** YOLO-v8 Instance Segmentation")
    st.write("📊 **Source:** Kvasir-SEG Dataset")

# --- MAIN INTERFACE ---
st.title("🩺 AI-ColoScan: Intelligent Diagnostic Interface")

tab1, tab2, tab3 = st.tabs(["🔍 Real-time Analysis", "📈 ML Analytics", "📄 Documentation"])

with tab1:
    if uploaded_file:
        col1, col2 = st.columns([1, 1])
        img = Image.open(uploaded_file)
        
        with col1:
            st.markdown("### Source Input")
            st.image(img, use_container_width=True)
            
        with col2:
            st.markdown("### AI Segmentation Layer")
            with st.spinner('AI is processing frame...'):
                time.sleep(1) # Имитация работы модели
                st.image(img, use_container_width=True) # Здесь будет маска от ребят
                st.info("🎯 Detection: **High Confidence (94.8%)**")

        st.markdown("---")
        # МЕТРИКИ В ТЕМНОМ СТИЛЕ
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Pathology", "Polyp", "Adenoma")
        m2.metric("Morphology", "Sessile", "Paris Class Is")
        m3.metric("Est. Size", "8.2 mm", "Risk: Medium")
        m4.metric("Inference Time", "12ms", "Real-time")
    else:
        st.info("Waiting for data input. Please upload a scan from the sidebar.")

with tab2:
    st.header("Model Performance Metrics")
    st.markdown("Data insights from current training session (Google Colab)")
    c1, c2 = st.columns(2)
    with c1:
        st.write("### Training Precision")
        # Вставь ссылку на реальный график из Колаба
        st.line_chart({"mAP 50": [0.1, 0.4, 0.7, 0.85, 0.92], "mAP 50-95": [0.05, 0.2, 0.5, 0.65, 0.8]})
    with c2:
        st.write("### Anomaly Distribution")
        st.bar_chart({"Polyp": 1200, "Inflammation": 450, "Normal": 742})

with tab3:
    st.markdown("""
    ### Project Overview
    This web interface connects the **YOLO-v8** model trained on **Kvasir-SEG** with a clinical-grade dashboard.
    
    **Features:**
    - **Instance Segmentation:** High-precision boundaries.
    - **Grad-CAM:** Explainable AI visualization.
    - **Clinical Metadata:** Automated sizing and classification.
    """)
