import streamlit as st
import pandas as pd
from io import BytesIO

# ==========================================
# CẤU HÌNH
# ==========================================
st.set_page_config(
    page_title="Quản lý khách hàng",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CSS - THEME XANH VCB
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.stApp {
    background: linear-gradient(160deg, #F0F7F2 0%, #FFFFFF 45%, #E8F5E9 100%);
    background-attachment: fixed;
}

#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

/* ========== SIDEBAR ========== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #FFFFFF 0%, #E8F5E9 100%) !important;
    border-right: 1px solid #A5D6A7;
}
section[data-testid="stSidebar"] > div { padding: 28px 18px; }

.side-logo { text-align: center; margin-bottom: 28px; }
.side-brand {
    margin-top: 14px;
    color: #1A1A1A !important;
    font-weight: 700;
    letter-spacing: 3px;
    font-size: 26px;
}
.side-sub {
    margin-top: 4px;
    color: #01502F;
    font-size: 13px;
    letter-spacing: 2.5px;
    font-weight: 600;
}

section[data-testid="stSidebar"] .stRadio label {
    color: #1A1A1A !important;
    padding: 14px 12px;
    border-radius: 10px;
    margin-bottom: 6px;
    transition: .2s;
    font-size: 16.5px !important;
}
section[data-testid="stSidebar"] .stRadio label:hover {
    background: #C8E6C9;
    color: #01502F !important;
}
section[data-testid="stSidebar"] .stCaption,
section[data-testid="stSidebar"] [data-testid="stCaption"] {
    color: #666666 !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    letter-spacing: 1.5px !important;
    opacity: 1 !important;
}

/* ========== MAIN ========== */
.block-container {
    max-width: 1050px;
    padding-top: 36px;
    padding-bottom: 40px;
}
.page-kicker {
    text-align: center;
    color: #01502F;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 6px;
}
.page-title {
    text-align: center;
    color: #1A1A1A;
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 4px;
}
.page-description {
    text-align: center;
    color: #555;
    font-size: 15px;
    margin-bottom: 18px;
}

/* Card */
.image-card, .form-card, .login-box,
div[data-testid="stMetric"], div[data-testid="stDataFrame"] {
    background: #FFFFFF;
    border: 1px solid #A5D6A7;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(1, 80, 47, 0.08),
                0 4px 12px rgba(0,0,0,.04);
}
.image-card {
    padding: 16px;
    margin-bottom: 26px;
    border-radius: 22px;
    background: linear-gradient(135deg, #01502F 0%, #027A45 100%);
}
.image-card img { border-radius: 14px; }

.form-card {
    padding: 32px 38px;
    border-radius: 20px;
}
.login-box {
    padding: 42px 36px;
    max-width: 480px;
    margin: 36px auto 20px;
    text-align: center;
    border-radius: 22px;
}

/* Input */
div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] {
    background: #F1F8F4 !important;
    border: 1.5px solid #A5D6A7 !important;
    border-radius: 12px !important;
}
div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"]:focus-within {
    border-color: #01502F !important;
    box-shadow: 0 0 0 4px rgba(1, 80, 47, 0.15) !important;
}
label {
    color: #333 !important;
    font-size: 14px !important;
    font-weight: 600 !important;
}

/* BUTTON - XANH VCB */
.stButton > button, .stDownloadButton > button {
    min-height: 52px;
    border-radius: 12px !important;
    border: none !important;
    background: linear-gradient(135deg, #01502F, #027A45) !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    transition: .25s;
    box-shadow: 0 6px 20px rgba(1, 80, 47, 0.3);
}
.stButton > button:hover {
    background: linear-gradient(135deg, #013D24, #01502F) !important;
    transform: translateY(-3px);
    box-shadow: 0 10px 28px rgba(1, 80, 47, 0.4);
}

/* Metric */
div[data-testid="stMetric"] {
    padding: 18px 16px;
    border-radius: 16px;
}
div[data-testid="stMetricLabel"] { color: #666 !important; font-size: 14px !important; }
div[data-testid="stMetricValue"] { color: #01502F !important; font-weight: 700 !important; font-size: 26px !important; }

.login-symbol {
    width: 64px; height: 64px;
    background: linear-gradient(135deg, #01502F, #027A45);
    border-radius: 50%;
    margin: auto;
    display: flex; align-items: center; justify-content: center;
    color: #fff; font-size: 26px;
    box-shadow: 0 8px 24px rgba(1, 80, 47, 0.35);
}
.login-title {
    color: #1A1A1A;
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    margin-top: 14px;
}
.login-description { color: #555; font-size: 14px; margin-top: 4px; }

.section-title {
    color: #1A1A1A;
    font-family: 'Playfair Display', serif;
    font-size: 26px;
    font-weight: 700;
}
.section-description { color: #555; font-size: 14px; margin-top: 2px; }

.footer {
    text-align: center;
    color: #999;
    font-size: 12px;
    letter-spacing: 2px;
    padding-top: 36px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# KHỞI TẠO
# ==========================================
if "customers" not in st.session_state:
    st.session_state.customers = []
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# ==========================================
# HÀM XUẤT EXCEL
# ==========================================
def export_excel():
    df = pd.DataFrame(st.session_state.customers)
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Khách hàng")
    return output.getvalue()

# ==========================================
# SIDEBAR - LOGO VCB STYLE
# ==========================================
st.sidebar.markdown("""
<div class="side-logo">
    <div style="
        width: 72px;
        height: 72px;
        margin: 0 auto 12px;
        display: flex;
        align-items: center;
        justify-content: center;
    ">
        <svg width="68" height="68" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="vcbGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#4CAF50"/>
                    <stop offset="40%" stop-color="#2E7D32"/>
                    <stop offset="100%" stop-color="#1B5E20"/>
                </linearGradient>
            </defs>
            <!-- Hình logo VCB (tam giác xoắn / trái tim) -->
            <path d="M100 20 
                     C140 20, 175 50, 175 95 
                     C175 130, 150 155, 100 185 
                     C50 155, 25 130, 25 95 
                     C25 50, 60 20, 100 20 
                     Z
                     M100 55 
                     C75 55, 55 75, 55 100 
                     C55 120, 75 140, 100 155 
                     C125 140, 145 120, 145 100 
                     C145 75, 125 55, 100 55 
                     Z" 
                  fill="url(#vcbGrad)"/>
        </svg>
    </div>
    <div class="side-brand">QUẢN LÝ</div>
    <div class="side-sub">KHÁCH HÀNG</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.caption("ĐIỀU HƯỚNG")
page = st.sidebar.radio(
    "Chọn trang",
    
