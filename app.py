import streamlit as st
from PIL import Image

# 1. Настройка внешнего вида
st.set_page_config(page_title="AI-ColoScan Pro", layout="wide")

# 2. Сайдбар (Боковое меню)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2413/2413110.png", width=100)
st.sidebar.title("AI-ColoScan Control")
st.sidebar.info("Данная система использует модель на базе датасета Kvasir-SEG для обнаружения патологий ЖКТ.")

# 3. Основные вкладки сайта
tab1, tab2, tab3 = st.tabs(["🚀 Диагностика (Demo)", "📊 Точность модели", "📝 О проекте"])

with tab1:
    st.header("Система анализа изображений в реальном времени")
    uploaded_file = st.file_uploader("Загрузите снимок колоноскопии...", type=['jpg', 'png', 'jpeg'])
    
    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        img = Image.open(uploaded_file)
        
        with col1:
            st.subheader("Оригинал")
            st.image(img, use_container_width=True)
            
        with col2:
            st.subheader("Результат ИИ")
            st.image(img, use_container_width=True) # Здесь будет наложение позже
            st.success("Анализ завершен: Обнаружен полип (уверенность 94%)")
            
        st.divider()
        st.subheader("Клинические показатели")
        m1, m2, m3 = st.columns(3)
        m1.metric("Тип объекта", "Adenoma")
        m2.metric("Размер", "~12 мм")
        m3.metric("Риск", "Высокий", delta="-15% пропусков")

with tab2:
    st.header("Метрики обучения (из Google Colab)")
    st.write("Модель обучена на 2392 изображениях из Roboflow.")
    # Тут можно вставить скриншот графиков, когда ребята их пришлют
    st.image("https://raw.githubusercontent.com/ultralytics/yolov5/master/data/images/bus.jpg", caption="График точности (mAP)")

with tab3:
    st.header("О проекте iGEM AI-ColoScan")
    st.markdown("""
    Наш проект решает проблему человеческого фактора в эндоскопии. 
    **Ключевые особенности:**
    * Интеграция с любым оборудованием.
    * Интерпретируемость (врач видит, куда смотрит ИИ).
    * Снижение стоимости ранней диагностики рака.
    """)
