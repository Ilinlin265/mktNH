import streamlit as st
import pandas as pd
from io import BytesIO

# =========================================================
# CẤU HÌNH
# =========================================================
st.set_page_config(
    page_title="Quản lý khách hàng",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS - GIAO DIỆN PREMIUM
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
.stApp {
    background: #f5f6f8;
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #091a2e;
    border-right: 1px solid #1a3048;
}
section[data-testid="stSidebar"] > div {
    padding: 30px 20px;
}
.side-logo { text-align: center; margin-bottom: 42px; }
.side-symbol {
    width: 42px; height: 42px;
    border: 1px solid #c9a96e;
    transform: rotate(45deg);
    margin: auto;
    display: flex; align-items: center; justify-content: center;
}
.side-symbol span {
    color: #c9a96e;
    transform: rotate(-45deg);
    font-size: 15px;
}
.side-brand {
    margin-top: 18px;
    color: #ffffff;
    font-weight: 700;
    letter-spacing: 3px;
    font-size: 14px;
}
.side-sub {
    margin-top: 6px;
    color: #788ca3;
    font-size: 8px;
    letter-spacing: 2px;
}
section[data-testid="stSidebar"] .stRadio label {
    color: #bdc9d7 !important;
    padding: 12px 10px;
    border-radius: 9px;
    margin-bottom: 5px;
    transition: .2s;
}
section[data-testid="stSidebar"] .stRadio label:hover {
    background: #132b45;
}

/* MAIN */
.block-container {
    max-width: 1050px;
    padding-top: 42px;
    padding-bottom: 40px;
}

/* HEADER */
.page-kicker {
    text-align: center;
    color: #b18b50;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 8px;
}
.page-title {
    text-align: center;
    color: #0b1d32;
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 5px;
}
.page-description {
    text-align: center;
    color: #8793a2;
    font-size: 12px;
    margin-bottom: 28px;
}

/* ẢNH */
.image-card {
    background: #ffffff;
    border: 1px solid #e5e9ee;
    border-radius: 25px;
    padding: 14px;
    margin-bottom: 28px;
    box-shadow: 0 18px 55px rgba(16, 31, 48, .07);
}
.image-card img { border-radius: 17px; }

/* FORM CARD */
.form-card {
    background: #ffffff;
    border: 1px solid #e5e9ee;
    border-radius: 23px;
    padding: 32px 40px;
    box-shadow: 0 15px 45px rgba(16, 31, 48, .06);
}

/* INPUT */
div[data-baseweb="input"] > div {
    background: #fafbfc !important;
    border: 1px solid #dfe5eb !important;
    border-radius: 10px !important;
}
div[data-baseweb="textarea"] {
    background: #fafbfc !important;
    border: 1px solid #dfe5eb !important;
    border-radius: 10px !important;
}
div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"]:focus-within {
    border-color: #b8945f !important;
    box-shadow: 0 0 0 3px rgba(184,148,95,.10) !important;
}
label {
    color: #344154 !important;
    font-size: 12px !important;
    font-weight: 600 !important;
}

/* BUTTON */
.stButton > button {
    min-height: 48px;
    border-radius: 10px !important;
    border: none !important;
    background: #0c2947 !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    letter-spacing: .4px;
    transition: .25s;
}
.stButton > button:hover {
    background: #173e64 !important;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(12,41,71,.18);
}
.stDownloadButton > button {
    min-height: 48px;
    border-radius: 10px !important;
    background: #0c2947 !important;
    color: #ffffff !important;
    border: none !important;
    font-weight: 700 !important;
}

/* METRIC */
div[data-testid="stMetric"] {
    background: #ffffff;
    border: 1px solid #e5e9ee;
    border-radius: 17px;
    padding: 18px 20px;
    box-shadow: 0 8px 25px rgba(16,31,48,.04);
}
div[data-testid="stMetricLabel"] { color: #7d8997 !important; }
div[data-testid="stMetricValue"] {
    color: #0c2947 !important;
    font-weight: 700 !important;
}

/* ADMIN LOGIN */
.login-box {
    background: #ffffff;
    border: 1px solid #e5e9ee;
    border-radius: 24px;
    padding: 42px;
    max-width: 500px;
    margin: 45px auto 25px auto;
    text-align: center;
    box-shadow: 0 20px 60px rgba(16,31,48,.09);
}
.login-symbol {
    width: 58px; height: 58px;
    background: #0c2947;
    border-radius: 50%;
    margin: auto;
    display: flex; align-items: center; justify-content: center;
    color: #c9a96e;
    font-size: 22px;
}
.login-title {
    color: #0b1c30;
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    margin-top: 17px;
}
.login-description {
    color: #8994a2;
    font-size: 12px;
    margin-top: 5px;
}

/* SECTION ADMIN */
.section-title {
    color: #0b1c30;
    font-family: 'Playfair Display', serif;
    font-size: 23px;
    font-weight: 700;
}
.section-description {
    color: #8994a2;
    font-size: 12px;
    margin-top: 3px;
}

/* TABLE */
div[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid #e5e9ee;
    box-shadow: 0 8px 25px rgba(16,31,48,.04);
}

/* FOOTER */
.footer {
    text-align: center;
    color: #a1aab5;
    font-size: 9px;
    letter-spacing: 2px;
    padding-top: 35px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# KHỞI TẠO
# =========================================================
if "customers" not in st.session_state:
    st.session_state.customers = []
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# =========================================================
# HÀM XUẤT EXCEL
# =========================================================
def export_excel():
    df = pd.DataFrame(st.session_state.customers)
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Khách hàng")
    return output.getvalue()

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown("""
    <div class="side-logo">
        <div class="side-symbol"><span>◆</span></div>
        <div class="side-brand">CUSTOMER</div>
        <div class="side-sub">MANAGEMENT SYSTEM</div>
    </div>
""", unsafe_allow_html=True)

st.sidebar.caption("ĐIỀU HƯỚNG")
page = st.sidebar.radio(
    "Chọn trang",
    ["👤 Nhập khách hàng", "🔐 Admin"],
    label_visibility="collapsed"
)

# =========================================================
# TRANG NHẬP KHÁCH HÀNG
# =========================================================
if page == "👤 Nhập khách hàng":
    st.title("👤 THÔNG TIN KHÁCH HÀNG")
    st.write("Vui lòng nhập thông tin khách hàng.")
    st.divider()

    # ẢNH
    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    col_left, col_center, col_right = st.columns([1, 3, 1])
    with col_center:
        try:
            st.image("LOGO.jpg", use_container_width=True)
        except:
            st.info("📷 Chưa tìm thấy LOGO.jpg")
    st.markdown('</div>', unsafe_allow_html=True)

    # FORM
    st.markdown('<div class="form-card">', unsafe_allow_html=True)

    # ===== TIÊU ĐỀ FORM (ĐÃ SỬA - DÙNG STREAMLIT THUẦN) =====
    st.subheader("👤 Thông tin khách hàng")
    st.caption("Nhập thông tin vào các trường bên dưới")
    st.markdown("<br>", unsafe_allow_html=True)
    # ========================================================

    phone = st.text_input("📱 Số điện thoại", placeholder="Nhập số điện thoại")
    name = st.text_input("👤 Tên khách hàng", placeholder="Nhập tên khách hàng")
    address = st.text_input("📍 Địa chỉ", placeholder="Nhập địa chỉ")
    note = st.text_area("📝 Ghi chú", placeholder="Nhập ghi chú", height=110)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("💾  LƯU THÔNG TIN", type="primary", use_container_width=True):
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

    st.markdown('</div>', unsafe_allow_html=True)

    # THỐNG KÊ
    if len(st.session_state.customers) > 0:
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("👥 Tổng khách hàng", len(st.session_state.customers))
        with c2:
            st.metric("📋 Hồ sơ đã lưu", len(st.session_state.customers))
        with c3:
            st.metric("🟢 Trạng thái", "Hoạt động")

# =========================================================
# TRANG ADMIN
# =========================================================
elif page == "🔐 Admin":
    st.markdown('<div class="page-kicker">SYSTEM ADMINISTRATION</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">🔐 ADMIN</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Khu vực quản lý dữ liệu khách hàng</div>', unsafe_allow_html=True)

    if not st.session_state.admin_logged_in:
        st.markdown("""
            <div class="login-box">
                <div class="login-symbol">🔐</div>
                <div class="login-title">ADMIN PORTAL</div>
                <div class="login-description">
                    Đăng nhập để truy cập hệ thống quản lý khách hàng
                </div>
            </div>
        """, unsafe_allow_html=True)

        password = st.text_input("🔑 Mật khẩu", type="password", placeholder="Nhập mật khẩu Admin")
        if st.button("🔓  ĐĂNG NHẬP", type="primary", use_container_width=True):
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
            with c1:
                st.metric("👥 Tổng số khách hàng", len(df))
            with c2:
                st.metric("📱 Hồ sơ liên hệ", len(df))
            with c3:
                st.metric("🟢 Trạng thái hệ thống", "Hoạt động")

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="section-title">Dữ liệu khách hàng</div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

            st.dataframe(df, use_container_width=True, hide_index=True, height=420)

            st.markdown("<br>", unsafe_allow_html=True)

            excel_file = export_excel()
            st.download_button(
                label="📥  XUẤT FILE EXCEL",
                data=excel_file,
                file_name="danh_sach_khach_hang.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
    <div class="footer">
        CUSTOMER MANAGEMENT SYSTEM &nbsp; • &nbsp;
        PROFESSIONAL CUSTOMER EXPERIENCE &nbsp; • &nbsp; 2026
    </div>
""", unsafe_allow_html=True)
