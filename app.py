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
    # Текст для главной страницы, когда ничего не загружено
    st.info("👋 Welcome! Please upload a colonoscopy frame in the sidebar to test the AI.")
    
    st.subheader("Why AI-ColoScan?")
    st.markdown("""
    * **Early Detection:** Helps identify polyps that are often missed by the human eye.
    * **Explainable AI:** Our system uses Grad-CAM heatmaps to show exactly *where* the AI is looking.
    * **Low Cost:** Compatible with existing endoscopy hardware.
    """)
    
    # Добавим видео или картинку из интернета, которая точно работает
    st.image("https://cdn.pixabay.com/photo/2016/11/23/17/56/cells-1854060_1280.jpg", caption="Microscopic view of intestinal tissues")
