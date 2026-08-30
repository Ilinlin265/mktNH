import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(
    page_title="Quản lý khách hàng",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS - GIAO DIỆN MỚI HIỆN ĐẠI, DỄ NHÌN, CỠ CHỮ LỚN
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #F4F6F9;
}

#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

/* ========== SIDEBAR ========== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
    border-right: none;
}
section[data-testid="stSidebar"] > div {
    padding: 32px 20px;
}

.side-logo {
    text-align: center;
    margin-bottom: 48px;
}

.side-symbol {
    width: 64px;
    height: 64px;
    background: #EF4444;
    border-radius: 18px;
    margin: 0 auto 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    color: white;
    box-shadow: 0 8px 24px rgba(239, 68, 68, 0.35);
}

.side-brand {
    color: #FFFFFF !important;
    font-weight: 800;
    font-size: 42px !important;
    letter-spacing: -0.5px;
    margin: 0;
    line-height: 1.1;
}

.side-sub {
    color: #F87171 !important;
    font-size: 18px !important;
    font-weight: 600;
    letter-spacing: 3px;
    margin-top: 8px;
    text-transform: uppercase;
}

section[data-testid="stSidebar"] .stCaption,
section[data-testid="stSidebar"] [data-testid="stCaption"] {
    color: #94A3B8 !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase;
    margin-bottom: 12px !important;
    opacity: 1 !important;
}

section[data-testid="stSidebar"] .stRadio label {
    color: #E2E8F0 !important;
    padding: 16px 18px !important;
    border-radius: 14px !important;
    margin-bottom: 8px !important;
    font-size: 20px !important;
    font-weight: 500 !important;
    transition: all 0.2s ease;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,0.08) !important;
    color: #FFFFFF !important;
}

/* ========== MAIN CONTENT ========== */
.block-container {
    max-width: 1100px;
    padding-top: 40px;
    padding-bottom: 60px;
}

/* Titles */
.page-title {
    font-family: 'Playfair Display', serif;
    font-size: 56px !important;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 8px;
    line-height: 1.15;
}

.page-subtitle {
    font-size: 20px;
    color: #64748B;
    margin-bottom: 36px;
}

.section-title {
    font-size: 32px !important;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 6px;
}

.section-desc {
    font-size: 16px;
    color: #64748B;
    margin-bottom: 24px;
}

/* Cards */
.card {
    background: #FFFFFF;
    border-radius: 24px;
    padding: 36px 40px;
    box-shadow: 0 4px 24px rgba(15, 23, 42, 0.06);
    border: 1px solid #E2E8F0;
    margin-bottom: 28px;
}

.login-card {
    background: #FFFFFF;
    border-radius: 28px;
    padding: 48px 40px;
    max-width: 480px;
    margin: 40px auto;
    text-align: center;
    box-shadow: 0 10px 40px rgba(15, 23, 42, 0.08);
    border: 1px solid #E2E8F0;
}

.login-icon {
    width: 72px;
    height: 72px;
    background: linear-gradient(135deg, #EF4444, #DC2626);
    border-radius: 20px;
    margin: 0 auto 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    color: white;
    box-shadow: 0 8px 24px rgba(239, 68, 68, 0.3);
}

/* Inputs */
div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] {
    background: #F8FAFC !important;
    border: 1.5px solid #E2E8F0 !important;
    border-radius: 14px !important;
    min-height: 56px !important;
}

div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"]:focus-within {
    border-color: #EF4444 !important;
    box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.12) !important;
}

label {
    color: #334155 !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    margin-bottom: 6px !important;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {
    min-height: 56px !important;
    border-radius: 14px !important;
    border: none !important;
    background: linear-gradient(135deg, #EF4444, #DC2626) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 18px !important;
    letter-spacing: 0.3px;
    transition: all 0.25s ease;
    box-shadow: 0 4px 16px rgba(239, 68, 68, 0.25);
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 28px rgba(239, 68, 68, 0.35) !important;
    background: linear-gradient(135deg, #DC2626, #B91C1C) !important;
}

/* Metrics */
div[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 20px;
    padding: 24px 20px !important;
    box-shadow: 0 2px 12px rgba(15, 23, 42, 0.04);
}

div[data-testid="stMetricLabel"] {
    color: #64748B !important;
    font-size: 15px !important;
    font-weight: 500 !important;
}

div[data-testid="stMetricValue"] {
    color: #0F172A !important;
    font-size: 32px !important;
    font-weight: 800 !important;
}

/* Dataframe */
div[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid #E2E8F0;
}

/* Footer */
.footer {
    text-align: center;
    color: #94A3B8;
    font-size: 13px;
    letter-spacing: 1px;
    padding-top: 48px;
    font-weight: 500;
}

/* Image card */
.image-card {
    background: #FFFFFF;
    border-radius: 24px;
    padding: 20px;
    box-shadow: 0 4px 24px rgba(15, 23, 42, 0.06);
    border: 1px solid #E2E8F0;
    margin-bottom: 28px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# STATE
# =========================================================
if "customers" not in st.session_state:
    st.session_state.customers = []
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

def export_excel():
    df = pd.DataFrame(st.session_state.customers)
    buf = BytesIO()
    with pd.ExcelWriter(buf, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Khách hàng")
    return buf.getvalue()

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown("""
<div class="side-logo">
    <div class="side-symbol">◆</div>
    <div class="side-brand">QUẢN LÝ</div>
    <div class="side-sub">Khách hàng</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.caption("ĐIỀU HƯỚNG")
page = st.sidebar.radio(
    "Chọn trang",
    ["👤  Nhập khách hàng", "🔐  Quản trị"],
    label_visibility="collapsed"
)

# =========================================================
# TRANG NHẬP KHÁCH HÀNG
# =========================================================
if page == "👤  Nhập khách hàng":
    st.markdown('<div class="page-title">Thông tin khách hàng</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Nhập và lưu thông tin khách hàng một cách nhanh chóng</div>', unsafe_allow_html=True)

    # Logo
    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    _, col, _ = st.columns([1, 2.5, 1])
    with col:
        try:
            st.image("LOGO.jpg", use_container_width=True)
        except:
            st.info("📷 Chưa tìm thấy LOGO.jpg – hãy đặt file LOGO.jpg cùng thư mục với app")
    st.markdown('</div>', unsafe_allow_html=True)

    # Form
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Nhập thông tin</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">Điền đầy đủ các trường bên dưới rồi nhấn Lưu</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        phone = st.text_input("📱 Số điện thoại", placeholder="Ví dụ: 0901234567")
    with col2:
        name = st.text_input("👤 Tên khách hàng", placeholder="Họ và tên đầy đủ")

    address = st.text_input("📍 Địa chỉ", placeholder="Số nhà, đường, quận/huyện, tỉnh/thành")
    note = st.text_area("📝 Ghi chú", placeholder="Ghi chú thêm (nếu có)", height=120)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("💾  LƯU THÔNG TIN", type="primary", use_container_width=True):
        if not phone.strip():
            st.error("❌ Vui lòng nhập số điện thoại")
        elif not name.strip():
            st.error("❌ Vui lòng nhập tên khách hàng")
        else:
            st.session_state.customers.append({
                "Số điện thoại": phone.strip(),
                "Tên khách hàng": name.strip(),
                "Địa chỉ": address.strip(),
                "Ghi chú": note.strip()
            })
            st.success("✅ Đã lưu thông tin khách hàng thành công!")
            st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

    # Metrics
    if st.session_state.customers:
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        c1.metric("👥 Tổng khách hàng", len(st.session_state.customers))
        c2.metric("📋 Hồ sơ đã lưu", len(st.session_state.customers))
        c3.metric("🟢 Trạng thái", "Hoạt động")

# =========================================================
# TRANG QUẢN TRỊ
# =========================================================
else:
    st.markdown('<div class="page-title">Quản trị hệ thống</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Khu vực quản lý và xuất dữ liệu khách hàng</div>', unsafe_allow_html=True)

    if not st.session_state.admin_logged_in:
        st.markdown("""
        <div class="login-card">
            <div class="login-icon">🔐</div>
            <div style="font-size: 32px; font-weight: 700; color: #0F172A; margin-bottom: 8px;">
                Cổng quản trị
            </div>
            <div style="font-size: 16px; color: #64748B; margin-bottom: 8px;">
                Đăng nhập để truy cập dữ liệu khách hàng
            </div>
        </div>
        """, unsafe_allow_html=True)

        pwd = st.text_input("🔑 Mật khẩu quản trị", type="password", placeholder="Nhập mật khẩu...")
        if st.button("🔓  ĐĂNG NHẬP", type="primary", use_container_width=True):
            if pwd == "123456":
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("❌ Sai mật khẩu. Vui lòng thử lại.")
    else:
        # Header + Logout
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown('<div class="section-title">📊 Danh sách khách hàng</div>', unsafe_allow_html=True)
            st.markdown('<div class="section-desc">Xem, theo dõi và xuất dữ liệu</div>', unsafe_allow_html=True)
        with col2:
            if st.button("🚪 Đăng xuất", use_container_width=True):
                st.session_state.admin_logged_in = False
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        if not st.session_state.customers:
            st.info("📭 Chưa có khách hàng nào được lưu.")
        else:
            df = pd.DataFrame(st.session_state.customers)

            c1, c2, c3 = st.columns(3)
            c1.metric("👥 Tổng số khách hàng", len(df))
            c2.metric("📱 Hồ sơ liên hệ", len(df))
            c3.metric("🟢 Hệ thống", "Hoạt động")

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="section-title">Dữ liệu chi tiết</div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                height=420
            )

            st.markdown("<br>", unsafe_allow_html=True)
            st.download_button(
                "📥  XUẤT FILE EXCEL",
                data=export_excel(),
                file_name="danh_sach_khach_hang.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">
    HỆ THỐNG QUẢN LÝ KHÁCH HÀNG  •  THIẾT KẾ HIỆN ĐẠI  •  2026
</div>
""", unsafe_allow_html=True)
