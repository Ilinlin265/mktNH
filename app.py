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
.side-symbol {
    width: 52px; height: 52px;
    border: 2.5px solid #01502F;
    transform: rotate(45deg);
    margin: auto;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 0 18px rgba(1, 80, 47, 0.35);
    background: #FFFFFF;
}
.side-symbol span {
    color: #01502F;
    transform: rotate(-45deg);
    font-size: 18px;
}
.side-brand {
    margin-top: 18px;
    color: #1A1A1A !important;
    font-weight: 700;
    letter-spacing: 3px;
    font-size: 28px;
}
.side-sub {
    margin-top: 6px;
    color: #01502F;
    font-size: 14px;
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
# SIDEBAR
# ==========================================
st.sidebar.markdown("""
<div class="side-logo">
    <div class="side-symbol"><span>◆</span></div>
    <div class="side-brand">QUẢN LÝ</div>
    <div class="side-sub">KHÁCH HÀNG</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.caption("ĐIỀU HƯỚNG")
page = st.sidebar.radio(
    "Chọn trang",
    ["👤 Nhập khách hàng", "🔐 Admin"],
    label_visibility="collapsed"
)

# ==========================================
# TRANG NHẬP KHÁCH HÀNG
# ==========================================
if page == "👤 Nhập khách hàng":
    st.markdown('<div class="page-kicker">HỆ THỐNG QUẢN LÝ</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">👤 THÔNG TIN KHÁCH HÀNG</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Vui lòng nhập thông tin khách hàng một cách đầy đủ</div>', unsafe_allow_html=True)

    # Logo với nền VCB
    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    _, col, _ = st.columns([1, 3, 1])
    with col:
        try:
            st.image("LOGO.jpg", use_container_width=True)
        except:
            st.info("📷 Chưa tìm thấy LOGO.jpg")
    st.markdown('</div>', unsafe_allow_html=True)

    # Form nhập
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.subheader("👤 Thông tin khách hàng")
    st.caption("Nhập thông tin vào các trường bên dưới")
    st.markdown("<br>", unsafe_allow_html=True)

    phone = st.text_input("📱 Số điện thoại", placeholder="Nhập số điện thoại")
    name = st.text_input("👤 Tên khách hàng", placeholder="Nhập tên khách hàng")
    address = st.text_input("📍 Địa chỉ", placeholder="Nhập địa chỉ")
    note = st.text_area("📝 Ghi chú", placeholder="Nhập ghi chú", height=100)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("💾 LƯU THÔNG TIN", type="primary", use_container_width=True):
        if phone.strip() == "":
            st.error("❌ Vui lòng nhập số điện thoại.")
        elif name.strip() == "":
            st.error("❌ Vui lòng nhập tên khách hàng.")
        else:
            customer = {
                "Số điện thoại": phone.strip(),
                "Tên khách hàng": name.strip(),
                "Địa chỉ": address.strip(),
                "Ghi chú": note.strip()
            }
            st.session_state.customers.append(customer)
            st.success("✅ Đã lưu thông tin khách hàng!")
            st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

    # Metrics
    if st.session_state.customers:
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        c1.metric("👥 Tổng khách hàng", len(st.session_state.customers))
        c2.metric("📋 Hồ sơ đã lưu", len(st.session_state.customers))
        c3.metric("🟢 Trạng thái", "Hoạt động")

# ==========================================
# TRANG ADMIN
# ==========================================
elif page == "🔐 Admin":
    st.markdown('<div class="page-kicker">QUẢN TRỊ HỆ THỐNG</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">🔐 ADMIN</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Khu vực quản lý dữ liệu khách hàng</div>', unsafe_allow_html=True)

    if not st.session_state.admin_logged_in:
        st.markdown("""
        <div class="login-box">
            <div class="login-symbol">🔐</div>
            <div class="login-title">CỔNG QUẢN TRỊ</div>
            <div class="login-description">Đăng nhập để truy cập hệ thống quản lý khách hàng</div>
        </div>
        """, unsafe_allow_html=True)

        password = st.text_input("🔑 Mật khẩu", type="password", placeholder="Nhập mật khẩu quản trị")
        if st.button("🔓 ĐĂNG NHẬP", type="primary", use_container_width=True):
            if password == "123456":
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("❌ Sai mật khẩu.")
    else:
        col1, col2 = st.columns([6, 1])
        with col1:
            st.markdown('<div class="section-title">📊 DANH SÁCH KHÁCH HÀNG</div>', unsafe_allow_html=True)
            st.markdown('<div class="section-description">Quản lý và theo dõi dữ liệu khách hàng</div>', unsafe_allow_html=True)
        with col2:
            if st.button("🚪 Đăng xuất", use_container_width=True):
                st.session_state.admin_logged_in = False
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        if len(st.session_state.customers) == 0:
            st.info("📭 Chưa có khách hàng.")
        else:
            df = pd.DataFrame(st.session_state.customers)
            c1, c2, c3 = st.columns(3)
            c1.metric("👥 Tổng số khách hàng", len(df))
            c2.metric("📱 Hồ sơ liên hệ", len(df))
            c3.metric("🟢 Trạng thái hệ thống", "Hoạt động")

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="section-title">📋 Dữ liệu khách hàng</div>', unsafe_allow_html=True)
            st.dataframe(df, use_container_width=True, hide_index=True, height=400)

            st.markdown("<br>", unsafe_allow_html=True)
            excel_file = export_excel()
            st.download_button(
                label="📥 XUẤT FILE EXCEL",
                data=excel_file,
                file_name="danh_sach_khach_hang.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

# ==========================================
# FOOTER
# ==========================================
st.markdown("""
<div class="footer">
    HỆ THỐNG QUẢN LÝ KHÁCH HÀNG  •  NHÓM CHIẾN LƯỢC
</div>
""", unsafe_allow_html=True)
