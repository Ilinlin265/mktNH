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
# CSS - GIAO DIỆN ĐỎ TECHCOMBANK (TCB)
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: #F8F8F8; }
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

/* SIDEBAR - ĐEN ĐẬM TCB */
section[data-testid="stSidebar"] {
    background: #1A1A1A;
    border-right: 1px solid #333;
}
section[data-testid="stSidebar"] > div { padding: 28px 18px; }
.side-logo { text-align: center; margin-bottom: 36px; }
.side-symbol {
    width: 44px; height: 44px;
    border: 2px solid #ED1C24;
    transform: rotate(45deg);
    margin: auto;
    display: flex; align-items: center; justify-content: center;
}
.side-symbol span {
    color: #ED1C24;
    transform: rotate(-45deg);
    font-size: 16px;
}
.side-brand {
    margin-top: 16px;
    color: #ffffff;
    font-weight: 700;
    letter-spacing: 3px;
    font-size: 24px;          /* to hơn */
}
.side-sub {
    margin-top: 6px;
    color: #ED1C24;
    font-size: 13px;          /* to hơn */
    letter-spacing: 2.5px;
    font-weight: 600;
}

/* Menu + ĐIỀU HƯỚNG tăng ~10% */
section[data-testid="stSidebar"] .stRadio label {
    color: #ffffff !important;
    padding: 13px 12px;
    border-radius: 9px;
    margin-bottom: 5px;
    transition: .2s;
    font-size: 15.5px !important;   /* tăng ~10% */
}
section[data-testid="stSidebar"] .stRadio label:hover {
    background: #2a2a2a;
    color: #ED1C24 !important;
}
section[data-testid="stSidebar"] .stCaption,
section[data-testid="stSidebar"] [data-testid="stCaption"] {
    color: #ffffff !important;
    font-size: 14.5px !important;   /* tăng ~10% */
    font-weight: 600 !important;
    letter-spacing: 1.5px !important;
    opacity: 1 !important;
}

/* MAIN */
.block-container { max-width: 1050px; padding-top: 38px; padding-bottom: 36px; }
.page-kicker { text-align: center; color: #ED1C24; font-size: 10px; font-weight: 700; letter-spacing: 4px; margin-bottom: 6px; }
.page-title { text-align: center; color: #1A1A1A; font-family: 'Playfair Display', serif; font-size: 34px; font-weight: 700; margin-bottom: 4px; }
.page-description { text-align: center; color: #666; font-size: 13px; margin-bottom: 24px; }

.image-card, .form-card, .login-box, div[data-testid="stMetric"], div[data-testid="stDataFrame"] {
    background: #ffffff;
    border: 1px solid #e5e5e5;
    border-radius: 18px;
    box-shadow: 0 8px 25px rgba(0,0,0,.05);
}
.image-card { padding: 12px; margin-bottom: 24px; border-radius: 20px; }
.image-card img { border-radius: 14px; }
.form-card { padding: 28px 36px; border-radius: 18px; }
.login-box { padding: 38px; max-width: 480px; margin: 40px auto 20px; text-align: center; border-radius: 20px; }

div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] {
    background: #fafafa !important;
    border: 1px solid #e0e0e0 !important;
    border-radius: 10px !important;
}
div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"]:focus-within {
    border-color: #ED1C24 !important;
    box-shadow: 0 0 0 3px rgba(237,28,36,.15) !important;
}
label { color: #333 !important; font-size: 13px !important; font-weight: 600 !important; }

/* BUTTON - ĐỎ TCB */
.stButton > button, .stDownloadButton > button {
    min-height: 48px;
    border-radius: 10px !important;
    border: none !important;
    background: #ED1C24 !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    transition: .25s;
}
.stButton > button:hover {
    background: #c41720 !important;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(237,28,36,.3);
}

div[data-testid="stMetric"] { padding: 16px 18px; border-radius: 14px; }
div[data-testid="stMetricLabel"] { color: #666 !important; }
div[data-testid="stMetricValue"] { color: #ED1C24 !important; font-weight: 700 !important; }

.login-symbol {
    width: 56px; height: 56px;
    background: #ED1C24;
    border-radius: 50%;
    margin: auto;
    display: flex; align-items: center; justify-content: center;
    color: #fff; font-size: 22px;
}
.login-title { color: #1A1A1A; font-family: 'Playfair Display', serif; font-size: 26px; margin-top: 14px; }
.login-description { color: #666; font-size: 13px; margin-top: 4px; }
.section-title { color: #1A1A1A; font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; }
.section-description { color: #666; font-size: 13px; margin-top: 2px; }
.footer { text-align: center; color: #999; font-size: 10px; letter-spacing: 2px; padding-top: 30px; }
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
    <div class="side-symbol"><span>◆</span></div>
    <div class="side-brand">QUẢN LÝ</div>
    <div class="side-sub">KHÁCH HÀNG</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.caption("ĐIỀU HƯỚNG")
page = st.sidebar.radio(
    "Chọn trang",
    ["👤 Nhập khách hàng", "🔐 Quản trị"],
    label_visibility="collapsed"
)

# =========================================================
# TRANG NHẬP
# =========================================================
if page == "👤 Nhập khách hàng":
    st.title("👤 THÔNG TIN KHÁCH HÀNG")
    st.write("Vui lòng nhập thông tin khách hàng.")
    st.divider()

    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    _, col, _ = st.columns([1, 3, 1])
    with col:
        try:
            st.image("LOGO.jpg", use_container_width=True)
        except:
            st.info("📷 Chưa tìm thấy LOGO.jpg")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.subheader("👤 Thông tin khách hàng")
    st.caption("Nhập thông tin vào các trường bên dưới")
    st.markdown("<br>", unsafe_allow_html=True)

    phone = st.text_input("📱 Số điện thoại", placeholder="Nhập số điện thoại")
    name = st.text_input("👤 Tên khách hàng", placeholder="Nhập tên khách hàng")
    address = st.text_input("📍 Địa chỉ", placeholder="Nhập địa chỉ")
    note = st.text_area("📝 Ghi chú", placeholder="Nhập ghi chú", height=100)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("💾  LƯU THÔNG TIN", type="primary", use_container_width=True):
        if not phone.strip():
            st.error("❌ Vui lòng nhập số điện thoại.")
        elif not name.strip():
            st.error("❌ Vui lòng nhập tên khách hàng.")
        else:
            st.session_state.customers.append({
                "Số điện thoại": phone.strip(),
                "Tên khách hàng": name.strip(),
                "Địa chỉ": address.strip(),
                "Ghi chú": note.strip()
            })
            st.success("✅ Đã lưu thông tin khách hàng!")
    st.markdown('</div>', unsafe_allow_html=True)

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
    st.markdown('<div class="page-kicker">QUẢN TRỊ HỆ THỐNG</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">🔐 QUẢN TRỊ</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Khu vực quản lý dữ liệu khách hàng</div>', unsafe_allow_html=True)

    if not st.session_state.admin_logged_in:
        st.markdown("""
        <div class="login-box">
            <div class="login-symbol">🔐</div>
            <div class="login-title">CỔNG QUẢN TRỊ</div>
            <div class="login-description">Đăng nhập để truy cập hệ thống quản lý khách hàng</div>
        </div>
        """, unsafe_allow_html=True)

        pwd = st.text_input("🔑 Mật khẩu", type="password", placeholder="Nhập mật khẩu quản trị")
        if st.button("🔓  ĐĂNG NHẬP", type="primary", use_container_width=True):
            if pwd == "123456":
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

        if not st.session_state.customers:
            st.info("📭 Chưa có khách hàng.")
        else:
            df = pd.DataFrame(st.session_state.customers)
            c1, c2, c3 = st.columns(3)
            c1.metric("👥 Tổng số khách hàng", len(df))
            c2.metric("📱 Hồ sơ liên hệ", len(df))
            c3.metric("🟢 Trạng thái hệ thống", "Hoạt động")

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="section-title">Dữ liệu khách hàng</div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.dataframe(df, use_container_width=True, hide_index=True, height=400)

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
    HỆ THỐNG QUẢN LÝ KHÁCH HÀNG &nbsp; • &nbsp; TRẢI NGHIỆM CHUYÊN NGHIỆP &nbsp; • &nbsp; 2026
</div>
""", unsafe_allow_html=True)
