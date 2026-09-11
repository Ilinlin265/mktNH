import streamlit as st
import pandas as pd
from io import BytesIO

# ==========================================
# CẤU HÌNH TRANG
# ==========================================
st.set_page_config(
    page_title="Hệ Thống Quản Lý & Đăng Ký Vay - Nhóm Chiến Lược",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CSS - THEME XANH VCB & CĂN SÁT LỀ TRÁI
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

/* CĂN SÁT LỀ TRÁI TOÀN BỘ KHÔNG GIAN MAIN */
.block-container {
    max-width: 100% !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-top: 20px !important;
    padding-bottom: 40px !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #FFFFFF 0%, #E8F5E9 100%) !important;
    border-right: 1px solid #A5D6A7;
}
section[data-testid="stSidebar"] > div { padding: 24px 16px; }

.side-logo { text-align: center; margin-bottom: 24px; }
.side-symbol {
    width: 48px; height: 48px;
    border: 2.5px solid #01502F;
    transform: rotate(45deg);
    margin: auto;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 0 16px rgba(1, 80, 47, 0.3);
    background: #FFFFFF;
}
.side-symbol span {
    color: #01502F;
    transform: rotate(-45deg);
    font-size: 18px;
}
.side-brand {
    margin-top: 16px;
    color: #1A1A1A !important;
    font-weight: 700;
    letter-spacing: 2px;
    font-size: 20px;
}
.side-sub {
    margin-top: 4px;
    color: #01502F;
    font-size: 11px;
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

/* BANNER NHÓM CHIẾN LƯỢC SÁT LỀ TRÁI */
.team-header-card {
    background: linear-gradient(135deg, #01502F 0%, #027A45 100%);
    border-radius: 16px;
    padding: 24px 30px;
    color: #FFFFFF;
    margin-bottom: 24px;
    box-shadow: 0 8px 24px rgba(1, 80, 47, 0.2);
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.team-title {
    font-family: 'Playfair Display', serif;
    font-size: 26px;
    font-weight: 700;
    margin: 0;
    color: #FFFFFF;
}
.team-sub {
    font-size: 14px;
    color: #C8E6C9;
    margin-top: 4px;
    letter-spacing: 1px;
}
.team-badge {
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1px;
}

/* Page Header Text - Left Aligned */
.page-kicker {
    text-align: left;
    color: #01502F;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 3px;
    margin-bottom: 4px;
}
.page-title {
    text-align: left;
    color: #1A1A1A;
    font-family: 'Playfair Display', serif;
    font-size: 34px;
    font-weight: 700;
    margin-bottom: 4px;
}
.page-description {
    text-align: left;
    color: #555;
    font-size: 14px;
    margin-bottom: 20px;
}

/* CARDS */
.form-card, .login-box, .calc-card,
div[data-testid="stMetric"], div[data-testid="stDataFrame"] {
    background: #FFFFFF;
    border: 1px solid #A5D6A7;
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(1, 80, 47, 0.06);
}
.form-card { padding: 28px 32px; border-radius: 16px; margin-bottom: 20px; }
.calc-card { padding: 24px; border-radius: 16px; background: #F1F8F4; margin-bottom: 20px; }

.login-box {
    padding: 36px 30px;
    max-width: 450px;
    margin: 20px 0;
    text-align: center;
}

/* INPUTS */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-baseweb="textarea"] {
    background: #F1F8F4 !important;
    border: 1.5px solid #A5D6A7 !important;
    border-radius: 10px !important;
}
div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"]:focus-within {
    border-color: #01502F !important;
    box-shadow: 0 0 0 3px rgba(1, 80, 47, 0.15) !important;
}
label { color: #333 !important; font-size: 14px !important; font-weight: 600 !important; }

/* BUTTONS */
.stButton > button, .stDownloadButton > button {
    min-height: 48px;
    border-radius: 10px !important;
    border: none !important;
    background: linear-gradient(135deg, #01502F, #027A45) !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    transition: .25s;
    box-shadow: 0 6px 18px rgba(1, 80, 47, 0.2);
}
.stButton > button:hover {
    background: linear-gradient(135deg, #013D24, #01502F) !important;
    transform: translateY(-2px);
    box-shadow: 0 8px 22px rgba(1, 80, 47, 0.3);
}

/* METRICS */
div[data-testid="stMetric"] { padding: 16px; border-radius: 14px; }
div[data-testid="stMetricLabel"] { color: #666 !important; font-size: 13px !important; }
div[data-testid="stMetricValue"] { color: #01502F !important; font-weight: 700 !important; font-size: 24px !important; }

.login-symbol {
    width: 56px; height: 56px;
    background: linear-gradient(135deg, #01502F, #027A45);
    border-radius: 50%;
    margin: auto;
    display: flex; align-items: center; justify-content: center;
    color: #fff; font-size: 22px;
}
.login-title { color: #1A1A1A; font-family: 'Playfair Display', serif; font-size: 24px; margin-top: 12px; }
.login-description { color: #555; font-size: 13px; margin-top: 4px; }

.section-title { color: #1A1A1A; font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; text-align: left; }
.section-description { color: #555; font-size: 13px; margin-top: 2px; text-align: left; }

.footer { text-align: left; color: #888; font-size: 12px; letter-spacing: 1.5px; padding-top: 30px; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# KHỞI TẠO SESSION STATE
# ==========================================
if "loan_requests" not in st.session_state:
    st.session_state.loan_requests = []
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# ==========================================
# HÀM BỔ TRỢ
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
    <div class="side-brand">QUẢN LÝ KHÁCH HÀNG</div>
    <div class="side-sub">NHÓM CHIẾN LƯỢC</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.caption("ĐIỀU HƯỚNG BẢNG ĐIỀU KHIỂN")
page = st.sidebar.radio(
    "Menu",
    ["📝 Đăng ký nhu cầu vay", "🧮 Bảng tính trả góp", "🔐 Quản trị Admin"],
    label_visibility="collapsed"
)

# ==========================================
# BANNER ĐẦU TRANG - THÔNG TIN NHÓM CHIẾN LƯỢC
# ==========================================
st.markdown("""
<div class="team-header-card">
    <div>
        <div class="team-title">🏛️ NHÓM CHIẾN LƯỢC - HỆ THỐNG PHÁT TRIỂN KHÁCH HÀNG</div>
        <div class="team-sub">Giải pháp thu thập & phân tích nhu cầu vay vốn tài chính cao cấp</div>
    </div>
    <div class="team-badge">
        DỰ ÁN TÀI CHÍNH 2026
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# TRANG 1: ĐĂNG KÝ VAY VỐN
# ==========================================
if page == "📝 Đăng ký nhu cầu vay":
    st.markdown('<div class="page-kicker">DỊCH VỤ TÀI CHÍNH CÁ NHÂN</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">💳 ĐĂNG KÝ TƯ VẤN VAY VỐN</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Khách hàng vui lòng điền đầy đủ thông tin bên dưới để Nhóm Chiến Lược hỗ trợ gói vay tối ưu nhất.</div>', unsafe_allow_html=True)

    # Form Nhập
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.subheader("📋 Thông tin hồ sơ vay")
    st.caption("Điền thông tin chính xác để chuyên viên thẩm định liên hệ nhanh nhất")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Họ và tên khách hàng (*)", placeholder="Nguyễn Văn A")
        phone = st.text_input("📱 Số điện thoại liên hệ (*)", placeholder="0901234567")
        address = st.text_input("📍 Tỉnh / Thành phố sinh sống", placeholder="Ví dụ: Hà Nội, TP.HCM")
        income = st.number_input("💵 Thu nhập hàng tháng (VNĐ)", min_value=0, step=1000000, value=15000000)

    with col2:
        loan_type = st.selectbox(
            "🏷️ Nhu cầu sản phẩm vay (*)",
            ["Vay Tín Chấp Theo Lương", "Vay Mua Nhà / BĐS", "Vay Mua Ô TÔ", "Vay Sản Xuất Kinh Doanh", "Vay Thấu Chi"]
        )
        loan_amount = st.number_input("💰 Số tiền đề xuất vay (VNĐ) (*)", min_value=10000000, step=10000000, value=100000000)
        tenure = st.selectbox("⏱️ Thời hạn vay mong muốn", ["12 tháng", "24 tháng", "36 tháng", "48 tháng", "60 tháng", "120 tháng"])
        income_type = st.radio("💳 Hình thức nhận lương", ["Chuyển khoản Ngân hàng", "Tiền mặt"], horizontal=True)

    note = st.text_area("📝 Ghi chú thêm (Nếu có)", placeholder="Nhu cầu chi tiết hoặc thời gian tiện nghe điện thoại...", height=80)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 GỬI THÔNG TIN VỀ NHÓM CHIẾN LƯỢC", type="primary", use_container_width=True):
        if not name.strip():
            st.error("❌ Vui lòng nhập Họ và tên khách hàng.")
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
                "Trạng thái": "Chờ Nhóm Chiến Lược xử lý"
            }
            st.session_state.loan_requests.append(new_request)
            st.success("✅ Đã gửi thông tin thành công! Nhóm Chiến Lược sẽ ghi nhận và xử lý hồ sơ ngay.")
            st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TRANG 2: CÔNG CỤ TÍNH TRẢ GÓP
# ==========================================
elif page == "🧮 Bảng tính trả góp":
    st.markdown('<div class="page-kicker">CÔNG CỤ HỖ TRỢ TÀI CHÍNH</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">🧮 BẢNG TÍNH LÃI VÀ GỐC TRẢ GÓP</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Công cụ tính khoản vay theo dư nợ giảm dần do Nhóm Chiến Lược phát triển.</div>', unsafe_allow_html=True)

    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        calc_amount = st.number_input("Số tiền vay (VNĐ)", min_value=10000000, value=200000000, step=10000000)
    with c2:
        calc_interest = st.number_input("Lãi suất (%/năm)", min_value=1.0, max_value=25.0, value=8.5, step=0.1)
    with c3:
        calc_months = st.slider("Thời gian vay (Tháng)", min_value=6, max_value=120, value=36, step=6)

    # Tính toán
    monthly_rate = (calc_interest / 100) / 12
    principal_monthly = calc_amount / calc_months
    first_month_interest = calc_amount * monthly_rate
    total_first_month = principal_monthly + first_month_interest

    st.markdown("<br>", unsafe_allow_html=True)
    res1, res2, res3 = st.columns(3)
    res1.metric("📌 Gốc cố định hàng tháng", format_money(principal_monthly))
    res2.metric("💸 Lãi tháng đầu tiên", format_money(first_month_interest))
    res3.metric("🔥 Tổng trả tháng đầu", format_money(total_first_month))

    st.caption("⚡ *Bảng tính mang tính tham khảo. Chi tiết sẽ được Nhóm Chiến Lược phê duyệt chính xác theo hồ sơ.*")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TRANG 3: ADMIN QUẢN LÝ
# ==========================================
elif page == "🔐 Quản trị Admin":
    st.markdown('<div class="page-kicker">QUẢN TRỊ DỮ LIỆU Nội BỘ</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">🔐 CỔNG ĐIỀU HÀNH - NHÓM CHIẾN LƯỢC</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-description">Xem danh sách khách hàng và trích xuất dữ liệu đăng ký.</div>', unsafe_allow_html=True)

    if not st.session_state.admin_logged_in:
        st.markdown("""
        <div class="login-box">
            <div class="login-symbol">🔐</div>
            <div class="login-title">ĐĂNG NHẬP ADMIN</div>
            <div class="login-description">Nhập mật khẩu để truy cập hệ thống quản trị</div>
        </div>
        """, unsafe_allow_html=True)

        pwd = st.text_input("🔑 Mật khẩu", type="password", placeholder="Nhập mật khẩu admin...")
        if st.button("🔓 XÁC NHẬN ĐĂNG NHẬP", type="primary", use_container_width=True):
            if pwd == "123456":
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("❌ Mật khẩu không đúng.")
    else:
        top_col1, top_col2 = st.columns([6, 1])
        with top_col1:
            st.markdown('<div class="section-title">📊 DANH SÁCH DỮ LIỆU KHÁCH HÀNG</div>', unsafe_allow_html=True)
            st.markdown('<div class="section-description">Cập nhật realtime từ người dùng đăng ký</div>', unsafe_allow_html=True)
        with top_col2:
            if st.button("🚪 Đăng xuất", use_container_width=True):
                st.session_state.admin_logged_in = False
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        if not st.session_state.loan_requests:
            st.info("📭 Chưa có thông tin đăng ký mới nào.")
        else:
            df = pd.DataFrame(st.session_state.loan_requests)

            # Thống kê
            m1, m2, m3 = st.columns(3)
            m1.metric("👥 Tổng hồ sơ tiếp nhận", len(df))
            m2.metric("💰 Tổng nhu cầu vay vốn", format_money(df["Số tiền vay"].sum()))
            m3.metric("📊 Nhu cầu trung bình", format_money(df["Số tiền vay"].mean()))

            st.markdown("<br>", unsafe_allow_html=True)
            st.dataframe(df, use_container_width=True, hide_index=True, height=380)

            st.markdown("<br>", unsafe_allow_html=True)
            excel_data = export_excel()
            st.download_button(
                label="📥 XUẤT FILE EXCEL CHO NHÓM CHIẾN LƯỢC (.XLSX)",
                data=excel_data,
                file_name="danh_sach_khach_hang_nhom_chien_luoc.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

# ==========================================
# FOOTER
# ==========================================
st.markdown("""
<div class="footer">
    HỆ THỐNG ĐĂNG KÝ VAY VỐN & QUẢN LÝ KHÁCH HÀNG • PHÁT TRIỂN BỞI NHÓM CHIẾN LƯỢC
</div>
""", unsafe_allow_html=True)
