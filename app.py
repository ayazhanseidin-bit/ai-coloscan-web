import streamlit as st
from PIL import Image

# 1. Настройка страницы (дизайн)
st.set_page_config(page_title="AI-ColoScan MVP", layout="wide")

# 2. Шапка сайта
st.title("🔬 AI-ColoScan: Early Detection")
st.markdown("---")

# 3. Боковая панель для настроек
st.sidebar.header("Navigation")
uploaded_file = st.sidebar.file_uploader("Upload Colonoscopy Image", type=['jpg', 'jpeg', 'png'])

# 4. Основной контент
if uploaded_file is not None:
    # Разделяем экран на 2 колонки
    col1, col2 = st.columns(2)
    
    image = Image.open(uploaded_file)
    
    with col1:
        st.subheader("Original Scan")
        st.image(image, use_container_width=True)
        
    with col2:
        st.subheader("AI Insight (Demo)")
        # Пока модель не подключена, показываем ту же картинку
        # Когда ребята дадут код, мы заменим это на результат ИИ
        st.image(image, caption="AI Analysis Layer", use_container_width=True)
        st.info("AI is analyzing the frame for potential polyps...")

    # Блок с метриками
    st.markdown("---")
    st.subheader("Risk Indicators")
    m1, m2, m3 = st.columns(3)
    m1.metric("Detection", "Potential Polyp Found")
    m2.metric("Confidence", "89%")
    m3.metric("Action", "Biopsy Recommended")

else:
    # Текст, который видит пользователь до загрузки фото
    st.info("Please upload a medical image from the sidebar to begin analysis.")
    st.image("https://images.unsplash.com/photo-1576091160550-2173dad99901?auto=format&fit=crop&w=1000&q=80", caption="Standard Endoscopy Setup")
