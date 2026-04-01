import streamlit as st
from PIL import Image
import cv2
import tempfile
import numpy as np
from ultralytics import YOLO

# --- НАСТРОЙКИ СТРАНИЦЫ ---
st.set_page_config(page_title="AI-ColoScan PRO Video", layout="wide")

# Загрузка модели
@st.cache_resource
def load_model():
    return YOLO('kvasir+polypDB.pt')

model = load_model()

# CSS (Ваш оригинальный дизайн)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e6edf3; }
    [data-testid="column"] img { max-width: 200px !important; object-fit: contain !important; }
    .stTabs [data-baseweb="tab"] {
        background-color: #1c2533 !important;
        border: 1px solid #3b82f6 !important;
        border-radius: 8px 8px 0px 0px !important;
        padding: 10px 30px !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(180deg, #3b82f6 0%, #1e40af 100%) !important;
    }
    .img-label { text-align: center; font-size: 18px; font-weight: 700; color: #ffffff; text-transform: uppercase; margin-bottom: 10px; }
    .custom-card { background-color: #1c2533; border: 2px solid #3b82f6; border-radius: 10px; padding: 15px; text-align: center; }
    .custom-label { color: #94a3b8; font-size: 14px; text-transform: uppercase; }
    .custom-value { color: #ffffff; font-size: 34px; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

# --- ШАПКА ---
col_logo, col_title = st.columns([1, 4])

with col_title:
    st.title("AI-ColoScan: Video Analysis System")
    st.write("Polyp detection ")

# --- ВКЛАДКИ ---
tab_diag, tab_info, tab_team = st.tabs(["DIAGNOSTICS", "KVASIR DATABASE", "ABOUT TEAM"])

with tab_diag:
    # Теперь принимаем и видео, и фото
    uploaded_file = st.file_uploader("Upload Video or Image", type=['mp4', 'mov', 'avi', 'jpg', 'png'], label_visibility="collapsed")

    if uploaded_file:
        file_type = uploaded_file.type.split('/')[0]
        
        if file_type == 'video':
            # --- ОБРАБОТКА ВИДЕО ---
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_file.read())
            
            cap = cv2.VideoCapture(tfile.name)
            
            c1, c2 = st.columns(2)
            with c1:
                st.markdown('<div class="img-label">Original Feed</div>', unsafe_allow_html=True)
                raw_video_placeholder = st.empty()
            with c2:
                st.markdown('<div class="img-label">AI Diagnostic Stream</div>', unsafe_allow_html=True)
                processed_video_placeholder = st.empty()

            stop_button = st.button("Stop Analysis")
            
            # Статистика для карточек (будет обновляться)
            stats_placeholder = st.empty()

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret or stop_button:
                    break
                
                # Конвертация для отображения
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                raw_video_placeholder.image(frame_rgb, use_container_width=True)
                
                # Анализ ИИ
                results = model.predict(frame, conf=0.4, verbose=False)
                
                # Отрисовка предсказаний
                annotated_frame = results[0].plot()
                annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
                processed_video_placeholder.image(annotated_frame_rgb, use_container_width=True)
                
                # Обновление карточек (берем данные последнего кадра)
                if len(results[0].boxes) > 0:
                    conf = results[0].boxes.conf[0].item() * 100
                    with stats_placeholder.container():
                        m1, m2, m3 = st.columns(3)
                        m1.markdown(f'<div class="custom-card"><span class="custom-label">Finding</span><span class="custom-value">POLYP</span></div>', unsafe_allow_html=True)
                        m2.markdown(f'<div class="custom-card"><span class="custom-label">Frames</span><span class="custom-value">Active</span></div>', unsafe_allow_html=True)
                        m3.markdown(f'<div class="custom-card"><span class="custom-label">Max Certainty</span><span class="custom-value">{conf:.1f}%</span></div>', unsafe_allow_html=True)
            
            cap.release()

        else:
            # --- ОБРАБОТКА ФОТО (Ваша старая логика, но с моделью) ---
            img = Image.open(uploaded_file)
            c1, c2 = st.columns(2)
            with c1:
                st.markdown('<div class="img-label">Input Photo</div>', unsafe_allow_html=True)
                st.image(img, use_container_width=True)
            with c2:
                st.markdown('<div class="img-label">AI Processed Photo</div>', unsafe_allow_html=True)
                results = model.predict(img, conf=0.3)
                res_plotted = results[0].plot()
                st.image(res_plotted, channels="BGR", use_container_width=True)
            
            if len(results[0].boxes) > 0:
                st.error(f"Polyp Detected! Certainty: {results[0].boxes.conf[0].item()*100:.1f}%")
            else:
                st.success("No Pathologies Detected")

    else:
        st.info("Please upload an endoscopic video or image to start.")


