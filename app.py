import streamlit as st
import pandas as pd
from io import BytesIO

# ==========================================
# CẤU HÌNH TRANG
# ==========================================
st.set_page_config(
    page_title="Đăng Ký Vay Vốn Ngân Hàng",
    page_icon="💳",
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

/* SIDEBAR */
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
    font-size: 20px;
}
.side-brand {
    margin-top: 18px;
    color: #1A1A1A !important;
    font-weight: 700;
    letter-spacing: 2px;
    font-size: 22px;
}
.side-sub {
    margin-top: 4px;
    color: #01502F;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 600;
}

section[data-testid="stSidebar"] .stRadio label {
    color: #1A1A1A !important;
    padding: 12px 10px;
    border-radius: 10px;
    margin-bottom: 6px;
    transition: .2s;
    font-size: 15px !important;
}
section[data-testid="stSidebar"] .stRadio label:hover {
    background: #C8E6C9;
    color: #01502F !important;
}

/* MAIN CONTAINERS */
.block-container {
    max-width: 1080px;
    padding-top: 30px;
    padding-bottom: 40px;
}
.page-kicker {
    text-align: center;
    color: #01502F;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 3px;
    margin-bottom: 4px;
}
.page-title {
    text-align: center;
    color: #1A1A1A;
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 4px;
}
.page-description {
    text-align: center;
    color: #555;
    font-size: 15px;
    margin-bottom: 24px;
}

/* Cards & Containers */
.image-card, .form-card, .login-box, .calc-card,
div[data-testid="stMetric"], div[data-testid="stDataFrame"] {
    background: #FFFFFF;
    border: 1px solid #A5D6A7;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(1, 80, 47, 0.08), 0 4px 12px rgba(0,0,0,.04);
}
.image-card {
    padding: 16px;
    margin-bottom: 24px;
    border-radius: 20px;
    background: linear-gradient(135deg, #01502F 0%, #027A45 100%);
}
.form-card { padding: 32px 36px; border-radius: 20px; }
.calc-card { padding: 24px; border-radius: 20px; background: #F1F8F4; margin-bottom: 20px; }

.login-box {
    padding: 42px 36px;
    max-width: 480px;
    margin: 36px auto 20px;
    text-align: center;
}

/* Inputs */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
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
label { color: #333 !important; font-size: 14px !important; font-weight: 600 !important; }

/* Buttons */
.stButton > button, .stDownloadButton > button {
    min-height: 50px;
    border-radius: 12px !important;
    border: none !important;
    background: linear-gradient(135deg, #01502F, #027A45) !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    transition: .25s;
    box-shadow: 0 6px 20px rgba(1, 80, 47, 0.25);
}
.stButton > button:hover {
    background: linear-gradient(135deg, #013D24, #01502F) !important;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(1, 80, 47, 0.35);
}

/* Metrics */
div[data-testid="stMetric"] { padding: 18px 16px; border-radius: 16px; }
div[data-testid="stMetricLabel"] { color: #666 !important; font-size: 13px !important; }
div[data-testid="stMetricValue"] { color: #01502F !important; font-weight: 700 !important; font-size: 24px !important; }

.login-symbol {
    width: 60px; height: 60px;
    background: linear-gradient(135deg, #01502F, #027A45);
    border-radius: 50%;
    margin: auto;
    display: flex; align-items: center; justify-content: center;
    color: #fff; font-size: 24px;
    box-shadow: 0 8px 20px rgba(1, 80, 47, 0.3);
}
.login-title { color: #1A1A1A; font-family: 'Playfair Display', serif; font-size: 26px; margin-top: 14px; }
.login-description { color: #555; font-size: 14px; margin-top: 4px; }

.section-title { color: #1A1A1A; font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 700; }
.section-description { color: #555; font-size: 14px; margin-top: 2px; }

.footer { text-align: center; color: #888; font-size: 12px; letter-spacing: 2px; padding-top: 40px; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# KHỞI TẠO STATE
# ==========================================
if "loan_requests" not in st.session_state:
    st.session_state.loan_requests = []
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# ==========================================
# HÀM TÍNH TOÁN & EXCEL
# ==========================================
def export_excel():
    df = pd.DataFrame(st.session_state.loan_requests)
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Nhu_cau_vay")
    return output.getvalue()

def format_money(amount):
    return f"{amount:,.0f} VNĐ".replace(",", ".")

# ==========================================
# SIDEBAR
# ==========================================
st.sidebar.markdown("""
<div class="side-logo">
    <div class="side-symbol"><span>%</span></div>
    <div class="side-brand">TÀI CHÍNH</div>
    <div class="side-sub">ĐĂNG KÝ VAY VỐN</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.caption("MENU CHÍNH")
page = st.sidebar.radio(
    "Điều hướng",
    ["📝 Đăng ký nhu cầu vay", "🧮 Bảng tính trả góp", "🔐 Quản trị Admin"],
    label_visibility="collapsed"
)

# ==========================================
# TRANG 1: ĐĂNG KÝ VAY VỐN
# ==========================================
if page == "📝 Đăng ký nhu cầu vay":
    st.markdown('<div class="page-kicker">DỊCH VỤ TÀI CHÍNH CÁ NHÂN</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">💳 ĐĂNG KÝ TƯ VẤN VAY VỐN</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Hoàn tất thông tin bên dưới để nhận tư vấn gói vay lãi suất ưu đãi nhất</div>', unsafe_allow_html=True)

    # Header Banner Image
    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    _, col_img, _ = st.columns([2, 2, 2])
    with col_img:
        try:
            st.image("LOGO.jpg", width=260)
        except:
            st.info("📷 LOGO BANK")
    st.markdown('</div>', unsafe_allow_html=True)

    # Form Nhập
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.subheader("📋 Thông tin hồ sơ đăng ký")
    st.caption("Các trường có dấu (*) là bắt buộc")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Họ và tên (*)", placeholder="Nguyễn Văn A")
        phone = st.text_input("📱 Số điện thoại (*)", placeholder="0901234567")
        address = st.text_input("📍 Tỉnh/Thành phố sinh sống", placeholder="Ví dụ: Hà Nội, TP.HCM")
        income = st.number_input("💵 Thu nhập hàng tháng (VNĐ)", min_value=0, step=1000000, value=15000000)

    with col2:
        loan_type = st.selectbox(
            "🏷️ Nhu cầu gói vay (*)",
            ["Vay Tín Chấp Theo Lương", "Vay Mua Nhà / BĐS", "Vay Mua Ô Tô", "Vay Kinh Doanh", "Vay Thấu Chi"]
        )
        loan_amount = st.number_input("💰 Số tiền muốn vay (VNĐ) (*)", min_value=10000000, step=10000000, value=100000000)
        tenure = st.selectbox("⏱️ Thời hạn vay mong muốn", ["12 tháng", "24 tháng", "36 tháng", "48 tháng", "60 tháng", "120 tháng"])
        income_type = st.radio("💳 Hình thức nhận lương", ["Chuyển khoản Ngân hàng", "Tiền mặt"], horizontal=True)

    note = st.text_area("📝 Ghi chú / Yêu cầu thêm", placeholder="VD: Muốn tư vấn gói lãi suất cố định 12 tháng...", height=80)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 GỬI YÊU CẦU TƯ VẤN", type="primary", use_container_width=True):
        if not name.strip():
            st.error("❌ Vui lòng nhập Họ và tên.")
        elif not phone.strip():
            st.error("❌ Vui lòng nhập Số điện thoại.")
        else:
            new_request = {
                "Họ và tên": name.strip(),
                "Số điện thoại": phone.strip(),
                "Khu vực": address.strip(),
                "Thu nhập": income,
                "Gói vay": loan_type,
                "Số tiền vay": loan_amount,
                "Thời hạn": tenure,
                "Hình thức lương": income_type,
                "Ghi chú": note.strip(),
                "Trạng thái": "Chờ liên hệ"
            }
            st.session_state.loan_requests.append(new_request)
            st.success("🎉 Đăng ký thành công! Chuyên viên tài chính sẽ liên hệ với bạn trong thời gian sớm nhất.")
            st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TRANG 2: CÔNG CỤ TÍNH TRẢ GÓP
# ==========================================
elif page == "🧮 Bảng tính trả góp":
    st.markdown('<div class="page-kicker">CÔNG CỤ HỖ TRỢ</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">🧮 TÍNH KHOẢN VAY DỰ KIẾN</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Ước tính số tiền cần trả hàng tháng theo phương thức dư nợ giảm dần</div>', unsafe_allow_html=True)

    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        calc_amount = st.number_input("Số tiền vay (VNĐ)", min_value=10000000, value=200000000, step=10000000)
    with c2:
        calc_interest = st.number_input("Lãi suất ưu đãi (%/năm)", min_value=1.0, max_value=25.0, value=8.5, step=0.1)
    with c3:
        calc_months = st.slider("Thời gian vay (Tháng)", min_value=6, max_value=120, value=36, step=6)

    # Tính toán cơ bản
    monthly_rate = (calc_interest / 100) / 12
    principal_monthly = calc_amount / calc_months
    first_month_interest = calc_amount * monthly_rate
    total_first_month = principal_monthly + first_month_interest

    st.markdown("<br>", unsafe_allow_html=True)
    res1, res2, res3 = st.columns(3)
    res1.metric("📌 Gốc trả hàng tháng", format_money(principal_monthly))
    res2.metric("💸 Lãi tháng đầu tiên", format_money(first_month_interest))
    res3.metric("🔥 Tổng trả tháng đầu", format_money(total_first_month))

    st.caption("⚡ *Lưu ý: Bảng tính mang tính chất tham khảo, lãi suất thực tế phụ thuộc vào hồ sơ phê duyệt của ngân hàng.*")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TRANG 3: ADMIN QUẢN LÝ HỒ SƠ VAY
# ==========================================
elif page == "🔐 Quản trị Admin":
    st.markdown('<div class="page-kicker">HỆ THỐNG QUẢN TRỊ</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">🔐 CỔNG QUẢN LÝ HỒ SƠ VAY</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Kiểm tra & Xuất dữ liệu khách hàng đăng ký tư vấn</div>', unsafe_allow_html=True)

    if not st.session_state.admin_logged_in:
        st.markdown("""
        <div class="login-box">
            <div class="login-symbol">🔐</div>
            <div class="login-title">ĐĂNG NHẬP ADMIN</div>
            <div class="login-description">Nhập mật khẩu quản trị viên để tiếp tục</div>
        </div>
        """, unsafe_allow_html=True)

        pwd = st.text_input("🔑 Mật khẩu", type="password", placeholder="Nhập mật khẩu...")
        if st.button("🔓 XÁC NHẬN ĐĂNG NHẬP", type="primary", use_container_width=True):
            if pwd == "123456":
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("❌ Mật khẩu không chính xác.")
    else:
        top_col1, top_col2 = st.columns([5, 1])
        with top_col1:
            st.markdown('<div class="section-title">📊 DANH SÁCH YÊU CẦU VAY VỐN</div>', unsafe_allow_html=True)
        with top_col2:
            if st.button("🚪 Đăng xuất", use_container_width=True):
                st.session_state.admin_logged_in = False
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        if not st.session_state.loan_requests:
            st.info("📭 Hiện chưa có khách hàng nào đăng ký nhu cầu vay.")
        else:
            df = pd.DataFrame(st.session_state.loan_requests)

            # Thống kê nhanh
            m1, m2, m3 = st.columns(3)
            m1.metric("👥 Tổng hồ sơ", len(df))
            m2.metric("💰 Tổng nhu cầu vay", format_money(df["Số tiền vay"].sum()))
            m3.metric("📊 Giá trị vay trung bình", format_money(df["Số tiền vay"].mean()))

            st.markdown("<br>", unsafe_allow_html=True)
            st.dataframe(df, use_container_width=True, hide_index=True, height=380)

            st.markdown("<br>", unsafe_allow_html=True)
            excel_data = export_excel()
            st.download_button(
                label="📥 XUẤT DANH SÁCH RA EXCEL (.XLSX)",
                data=excel_data,
                file_name="danh_sach_dang_ky_vay.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

# ==========================================
# FOOTER
# ==========================================
st.markdown("""
<div class="footer">
    HỆ THỐNG ĐĂNG KÝ TƯ VẤN TÀI CHÍNH & VAY VỐN • TỰ ĐỘNG & BẢO MẬT
</div>
""", unsafe_allow_html=True)
