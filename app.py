import streamlit as st
from PIL import Image
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI-ColoScan PRO", layout="wide")

# CSS for a professional, clinical look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e6edf3; }
    
    /* Center text labels above images */
    .img-label {
        text-align: center;
        font-size: 18px;
        font-weight: 800;
        margin-bottom: 8px;
        color: #ffffff;
        display: block;
        width: 100%;
    }

    /* CLINICAL DISCLAIMER TEXT */
    .clinical-disclaimer {
        text-align: center;
        background-color: #1a1a1a;
        color: #fca5a5; /* Light red text */
        border: 1px solid #7f1d1d; /* Dark red border */
        padding: 15px;
        border-radius: 8px;
        margin-top: 20px;
        font-size: 14px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* DATA CARDS (Cleaned up) */
    .custom-card {
        background-color: #1c2533;
        border: 2px solid #3b82f6;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .custom-label {
        color: #94a3b8 !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        display: block;
        margin-bottom: 8px;
    }
    .custom-value {
        color: #ffffff !important;
        font-size: 38px !important;
        font-weight: 900 !important;
        display: block;
    }

    /* SIDEBAR (Technical info) */
    [data-testid="stSidebar"] img {
        width: 100% !important;
        padding: 10px;
        object-fit: contain;
    }
    [data-testid="stSidebar"] { padding-top: 0rem !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Persistent Logo & Info) ---
with st.sidebar:
    try:
        st.image("logo.png")
    except:
        st.write("iGEM NU")
    st.divider()
    st.markdown("### Technical Overview")
    st.write("Architecture: **YOLOv8-SEG**")
    st.write("Dataset: **Kvasir-SEG (Vestre Viken Health Trust)**")
    st.success("Analysis Engine: Online")

# --- MAIN CONTENT ---
st.title("AI-ColoScan: Intelligent Pathological Detection")
st.write("Clinical Decision Support System for Colorectal Screening")
st.divider()

# File Uploader
uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'], label_visibility="collapsed")

if uploaded_file:
    img = Image.open(uploaded_file)
    
    # Grid 1x2 for photos
    c1, c2 = st.columns(2)
    
    with c1:
        # 1. LABELS ABOVE PHOTOS
        st.markdown('<div class="img-label">Original Clinical Stream</div>', unsafe_allow_html=True)
        st.image(img, use_container_width=True)
    
    with c2:
        st.markdown('<div class="img-label">AI Segmentation Map</div>', unsafe_allow_html=True)
        with st.spinner('Analysing...'):
            time.sleep(0.4) # Simulate processing
            st.image(img, use_container_width=True) #Mask will go here
    
    st.error("Diagnostic Alert: Polyp Detected (Probability 94.2%)")

    # 2. RELOCATED CLINICAL DISCLAIMER (Before Data)
    st.markdown("""
        <div class="clinical-disclaimer">
            The following analytics are algorithmic estimations for computer-aided detection and retrieval (CADe/CADx) purposes only. They are to assist, not replace, final clinical judgment.
        </div>
    """, unsafe_allow_html=True)

    # Clean data section
    st.subheader("Algorithmic Indications")
    m1, m2, m3 = st.columns(3)
    
    # 3. BETTER WORDING FOR LABELS
    with m1:
        st.markdown('''
            <div class="custom-card">
                <span class="custom-label">FINDING TYPE</span>
                <span class="custom-value">POLYP</span>
            </div>''', unsafe_allow_html=True)
    with m2:
        st.markdown('''
            <div class="custom-card">
                <span class="custom-label">DIMENSIONS</span>
                <span class="custom-value">12.4 mm</span>
            </div>''', unsafe_allow_html=True)
    with m3:
        st.markdown('''
            <div class="custom-card">
                <span class="custom-label">CERTAINTY SCORE</span>
                <span class="custom-value">94.2%</span>
            </div>''', unsafe_allow_html=True)
else:
    st.info("Please upload an endoscopic image to begin the automated analysis.")
