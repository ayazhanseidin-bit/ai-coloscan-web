import streamlit as st
from PIL import Image
import cv2
import tempfile
import numpy as np
from ultralytics import YOLO

# --- НАСТРОЙКИ СТРАНИЦЫ ---
st.set_page_config(page_title="AI-ColoScan PRO", layout="wide")

# Загрузка модели
@st.cache_resource
def load_model():
    return YOLO('kvasir+polypDB.pt')

model = load_model()

# CSS (Дизайн без лишних элементов вкладок)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e6edf3; }
    .img-label { 
        text-align: center; 
        font-size: 18px; 
        font-weight: 700; 
        color: #ffffff; 
        text-transform: uppercase; 
        margin-bottom: 10px; 
    }
    .custom-card { 
        background-color: #1c2533; 
        border: 2px solid #3b82f6; 
        border-radius: 10px; 
        padding: 15px; 
        text-align: center; 
        margin-top: 10px;
    }
    .custom-label { color: #94a3b8; font-size: 14px; text-transform: uppercase; }
    .custom-value { color: #ffffff; font-size: 34px; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

# --- ШАПКА (Без лого) ---
st.title("AI-ColoScan: Clinical Diagnostic System")
st.write("Real-time polyp detection and analysis powered by YOLOv8")
st.divider()

# --- ОСНОВНОЙ БЛОК ДИАГНОСТИКИ ---
uploaded_file = st.file_uploader("Upload Video or Image", type=['mp4', 'mov', 'avi', 'jpg', 'png', 'jpeg'], label_visibility="collapsed")

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

        stop_button = st.button("Stop Analysis", use_container_width=True)
        stats_placeholder = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret or stop_button:
                break
            
            # Конвертация кадра для Streamlit
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            raw_video_placeholder.image(frame_rgb, use_container_width=True)
            
            # Предсказание модели
            results = model.predict(frame, conf=0.4, verbose=False)
            
            # Отрисовка аннотаций
            annotated_frame = results[0].plot()
            annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            processed_video_placeholder.image(annotated_frame_rgb, use_container_width=True)
            
            # Обновление метрик в реальном времени
            if len(results[0].boxes) > 0:
                conf = results[0].boxes.conf[0].item() * 100
                with stats_placeholder.container():
                    m1, m2, m3 = st.columns(3)
                    m1.markdown(f'<div class="custom-card"><span class="custom-label">Finding</span><span class="custom-value">POLYP</span></div>', unsafe_allow_html=True)
                    m2.markdown(f'<div class="custom-card"><span class="custom-label">Status</span><span class="custom-value">DETECTED</span></div>', unsafe_allow_html=True)
                    m3.markdown(f'<div class="custom-card"><span class="custom-label">Confidence</span><span class="custom-value">{conf:.1f}%</span></div>', unsafe_allow_html=True)
        
        cap.release()

    else:
        # --- ОБРАБОТКА ФОТО ---
        img = Image.open(uploaded_file)
        # Превращаем в массив для модели
        img_array = np.array(img)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="img-label">Input Photo</div>', unsafe_allow_html=True)
            st.image(img, use_container_width=True)
        with c2:
            st.markdown('<div class="img-label">AI Processed Photo</div>', unsafe_allow_html=True)
            results = model.predict(img_array, conf=0.3)
            res_plotted = results[0].plot()
            st.image(res_plotted, channels="BGR", use_container_width=True)
        
        if len(results[0].boxes) > 0:
            st.error(f"Diagnostic Result: Polyp Detected")
            # Карточки для фото
            m1, m2, m3 = st.columns(3)
            conf_photo = results[0].boxes.conf[0].item() * 100
            m1.markdown('<div class="custom-card"><span class="custom-label">Type</span><span class="custom-value">POLYP</span></div>', unsafe_allow_html=True)
            m2.markdown('<div class="custom-card"><span class="custom-label">Analysis</span><span class="custom-value">STATIC</span></div>', unsafe_allow_html=True)
            m3.markdown(f'<div class="custom-card"><span class="custom-label">Certainty</span><span class="custom-value">{conf_photo:.1f}%</span></div>', unsafe_allow_html=True)
        else:
            st.success("Diagnostic Result: No Pathologies Detected")

else:
    st.info("Please upload an endoscopic video or image to start the clinical analysis.")
