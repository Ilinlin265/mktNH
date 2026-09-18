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
# CSS PREMIUM UI - STYLE VIETCOMBANK MODERN
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* Global Font & Smooth Theme */
html, body, [class*="css"] { 
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
    background: #F4F7F5;
}

/* Hide default elements */
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

/* Main Layout Padding */
.block-container {
    max-width: 100% !important;
    padding: 1.5rem 2.5rem 3rem 2.5rem !important;
}

/* Custom Glassmorphism Sidebar */
section[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1px solid #E1E8E3;
}

section[data-testid="stSidebar"] > div { 
    padding: 2rem 1.2rem; 
}

/* Sidebar Brand Styling */
.brand-card {
    background: linear-gradient(135deg, #013D24 0%, #01502F 100%);
    border-radius: 16px;
    padding: 20px 16px;
    text-align: center;
    color: white;
    box-shadow: 0 10px 20px rgba(1, 80, 47, 0.15);
    margin-bottom: 24px;
}

.brand-icon {
    font-size: 28px;
    background: rgba(255, 255, 255, 0.15);
    width: 52px;
    height: 52px;
    line-height: 52px;
    border-radius: 12px;
    margin: 0 auto 12px auto;
    border: 1px solid rgba(255, 255, 255, 0.25);
}

.brand-title {
    font-size: 15px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #FFFFFF;
    margin: 0;
}

.brand-subtitle {
    font-size: 11px;
    color: #A3E6CD;
    font-weight: 600;
    letter-spacing: 1px;
    margin-top: 4px;
}

/* Custom Navigation Radio Buttons */
section[data-testid="stSidebar"] .stRadio label {
    background: #F8FAF9;
    border: 1px solid #E1E8E3;
    color: #2D3748 !important;
    padding: 14px 16px;
    border-radius: 12px;
    margin-bottom: 8px;
    transition: all 0.25s ease;
    font-size: 14px !important;
    font-weight: 600 !important;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    border-color: #01502F;
    background: #E8F5E9;
    color: #01502F !important;
    transform: translateX(4px);
}

/* Hero Header Banner */
.hero-banner {
    background: linear-gradient(135deg, #01502F 0%, #027A45 60%, #004D25 100%);
    border-radius: 20px;
    padding: 32px 40px;
    color: #FFFFFF;
    margin-bottom: 28px;
    box-shadow: 0 12px 30px rgba(1, 80, 47, 0.18);
    position: relative;
    overflow: hidden;
}

.hero-banner::after {
    content: "";
    position: absolute;
    right: -50px;
    bottom: -50px;
    width: 220px;
    height: 220px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 50%;
}

.hero-title {
    font-size: 28px;
    font-weight: 800;
    margin: 0;
    letter-spacing: -0.5px;
}

.hero-sub {
    font-size: 15px;
    color: #C8E6C9;
    margin-top: 6px;
    font-weight: 400;
}

/* Custom Modern Cards */
.custom-card {
    background: #FFFFFF;
    border-radius: 18px;
    padding: 32px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
    margin-bottom: 24px;
}

/* Form Controls Styling */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-baseweb="textarea"] {
    background: #F8FAF9 !important;
    border: 1.5px solid #E1E8E3 !important;
    border-radius: 12px !important;
    font-size: 14px !important;
}

div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"]:focus-within {
    border-color: #01502F !important;
    box-shadow: 0 0 0 3px rgba(1, 80, 47, 0.12) !important;
    background: #FFFFFF !important;
}

label { 
    color: #2D3748 !important; 
    font-size: 13px !important; 
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px !important;
}

/* Primary Button Styling */
.stButton > button, .stDownloadButton > button {
    height: 52px;
    border-radius: 12px !important;
    border: none !important;
    background: linear-gradient(135deg, #01502F 0%, #027A45 100%) !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    letter-spacing: 0.5px;
    transition: all 0.3s ease !important;
    box-shadow: 0 6px 18px rgba(1, 80, 47, 0.22);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #013D24 0%, #01502F 100%) !important;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(1, 80, 47, 0.32);
}

/* Modern Metric Cards */
div[data-testid="stMetric"] {
    background: #F8FAF9;
    border: 1px solid #E1E8E3;
    border-radius: 16px;
    padding: 20px;
    box-shadow: none;
}

div[data-testid="stMetricLabel"] { 
    color: #718096 !important; 
    font-size: 12px !important; 
    font-weight: 700 !important;
    text-transform: uppercase;
}

div[data-testid="stMetricValue"] { 
    color: #01502F !important; 
    font-weight: 800 !important; 
    font-size: 26px !important; 
}

/* Section Titles */
.page-header {
    margin-bottom: 24px;
}
.page-title {
    font-size: 26px;
    font-weight: 800;
    color: #1A202C;
    margin: 0;
}
.page-desc {
    font-size: 14px;
    color: #718096;
    margin-top: 4px;
}

/* Admin Login Card */
.admin-card {
    max-width: 420px;
    margin: 40px auto;
    padding: 40px;
    background: #FFFFFF;
    border-radius: 20px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 15px 35px rgba(0,0,0,0.05);
    text-align: center;
}

.footer {
    text-align: center;
    color: #A0AEC0;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 1px;
    padding-top: 40px;
    padding-bottom: 20px;
}
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
with st.sidebar:
    st.markdown("""
    <div class="brand-card">
        <div class="brand-icon">🏛️</div>
        <div class="brand-title">NHÓM CHIẾN LƯỢC</div>
        <div class="brand-subtitle">HỆ THỐNG QUẢN LÝ VAY</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Menu Điều Hướng",
        ["📝 Đăng ký nhu cầu vay", "🧮 Bảng tính trả góp", "🔐 Quản trị Admin"],
        label_visibility="collapsed"
    )

# ==========================================
# BANNER ĐẦU TRANG
# ==========================================
st.markdown("""
<div class="hero-banner">
    <div class="hero-title">🏛️ HỆ THỐNG PHÁT TRIỂN & QUẢN LÝ KHÁCH HÀNG VAY</div>
    <div class="hero-sub">Giải pháp số hóa tiếp nhận nhu cầu vay vốn & phân tích tài chính tối ưu | Nhóm Chiến Lược</div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# TRANG 1: ĐĂNG KÝ VAY VỐN
# ==========================================
if page == "📝 Đăng ký nhu cầu vay":
    st.markdown("""
    <div class="page-header">
        <div class="page-title">💳 Đăng Ký Tư Vấn Vay Vốn</div>
        <div class="page-desc">Vui lòng hoàn thiện thông tin bên dưới, chuyên viên Nhóm Chiến Lược sẽ liên hệ hỗ trợ trong thời gian sớm nhất.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        name = st.text_input("👤 Họ và tên khách hàng (*)", placeholder="Nhập đầy đủ họ tên")
        phone = st.text_input("📱 Số điện thoại liên hệ (*)", placeholder="Ví dụ: 0901234567")
        address = st.text_input("📍 Tỉnh / Thành phố sinh sống", placeholder="Ví dụ: TP. Hồ Chí Minh, Hà Nội")
        income = st.number_input("💵 Thu nhập hàng tháng (VNĐ)", min_value=0, step=1000000, value=15000000)

    with col2:
        loan_type = st.selectbox(
            "🏷️ Nhu cầu sản phẩm vay (*)",
            ["Vay Tín Chấp Theo Lương", "Vay Mua Nhà / BĐS", "Vay Mua Ô TÔ", "Vay Sản Xuất Kinh Doanh", "Vay Thấu Chi"]
        )
        loan_amount = st.number_input("💰 Số tiền đề xuất vay (VNĐ) (*)", min_value=10000000, step=10000000, value=100000000)
        tenure = st.selectbox("⏱️ Thời hạn vay mong muốn", ["12 tháng", "24 tháng", "36 tháng", "48 tháng", "60 tháng", "120 tháng"])
        income_type = st.radio("💳 Hình thức nhận lương", ["Chuyển khoản Ngân hàng", "Tiền mặt"], horizontal=True)

    note = st.text_area("📝 Ghi chú thêm (Nếu có)", placeholder="Nhập nhu cầu chi tiết hoặc mốc thời gian tiện nghe máy...", height=90)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 GỬI HỒ SƠ ĐĂNG KÝ VAY", type="primary", use_container_width=True):
        if not name.strip():
            st.error("❌ Vui lòng nhập Họ và tên khách hàng.")
        elif not phone.strip():
            st.error("❌ Vui lòng nhập Số điện thoại liên hệ.")
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
            st.success("✅ Đã gửi hồ sơ thành công! Chuyên viên Nhóm Chiến Lược sẽ tiếp nhận và liên hệ ngay.")
            st.balloons()
            
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TRANG 2: CÔNG CỤ TÍNH TRẢ GÓP
# ==========================================
elif page == "🧮 Bảng tính trả góp":
    st.markdown("""
    <div class="page-header">
        <div class="page-title">🧮 Mô Phỏng Khoản Vay & Lãi Suất</div>
        <div class="page-desc">Công cụ dự toán lịch trả nợ theo phương thức dư nợ giảm dần do Nhóm Chiến Lược phát triển.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        calc_amount = st.number_input("💰 Số tiền vay (VNĐ)", min_value=10000000, value=200000000, step=10000000)
    with c2:
        calc_interest = st.number_input("📈 Lãi suất năm (%/năm)", min_value=1.0, max_value=25.0, value=8.5, step=0.1)
    with c3:
        calc_months = st.select_slider("⏱️ Thời gian vay (Tháng)", options=[6, 12, 18, 24, 36, 48, 60, 84, 120], value=36)

    # Tính toán
    monthly_rate = (calc_interest / 100) / 12
    principal_monthly = calc_amount / calc_months
    first_month_interest = calc_amount * monthly_rate
    total_first_month = principal_monthly + first_month_interest

    st.markdown("<br>", unsafe_allow_html=True)
    res1, res2, res3 = st.columns(3)
    res1.metric("📌 Gốc cố định hàng tháng", format_money(principal_monthly))
    res2.metric("💸 Lãi tháng đầu tiên", format_money(first_month_interest))
    res3.metric("🔥 Tổng gốc + lãi tháng đầu", format_money(total_first_month))

    st.caption("⚡ *Lưu ý: Bảng tính mang tính chất tham khảo. Lịch trả nợ chi tiết sẽ được phê duyệt chính xác theo từng hồ sơ thực tế.*")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TRANG 3: ADMIN QUẢN LÝ
# ==========================================
elif page == "🔐 Quản trị Admin":
    st.markdown("""
    <div class="page-header">
        <div class="page-title">🔐 Cổng Quản Trị Hệ Thống</div>
        <div class="page-desc">Khu vực dành riêng cho chuyên viên Nhóm Chiến Lược quản lý hồ sơ và trích xuất dữ liệu.</div>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.admin_logged_in:
        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        st.markdown("""
            <div style="font-size: 40px; margin-bottom: 8px;">🔐</div>
            <h3 style="margin: 0; color: #1A202C;">Đăng Nhập Admin</h3>
            <p style="color: #718096; font-size: 13px; margin-bottom: 24px;">Vui lòng nhập mật khẩu quản trị viên</p>
        """, unsafe_allow_html=True)
        
        pwd = st.text_input("Mật khẩu truy cập", type="password", placeholder="••••••••", label_visibility="collapsed")
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🔓 XÁC NHẬN ĐĂNG NHẬP", type="primary", use_container_width=True):
            if pwd == "123456":
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("❌ Mật khẩu xác thực không đúng.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        top_col1, top_col2 = st.columns([5, 1])
        with top_col1:
            st.subheader("📊 Danh Sách Hồ Sơ Khách Hàng Đăng Ký")
        with top_col2:
            if st.button("🚪 Đăng xuất", use_container_width=True):
                st.session_state.admin_logged_in = False
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        if not st.session_state.loan_requests:
            st.info("📭 Hiện tại chưa có dữ liệu hồ sơ đăng ký mới.")
        else:
            df = pd.DataFrame(st.session_state.loan_requests)

            # Thống kê KPI
            m1, m2, m3 = st.columns(3)
            m1.metric("👥 Tổng hồ sơ tiếp nhận", f"{len(df)} hồ sơ")
            m2.metric("💰 Tổng nhu cầu vay", format_money(df["Số tiền vay"].sum()))
            m3.metric("📊 Nhu cầu vay trung bình", format_money(df["Số tiền vay"].mean()))

            st.markdown("<br>", unsafe_allow_html=True)
            
            # Data Table
            st.dataframe(
                df, 
                use_container_width=True, 
                hide_index=True, 
                height=380
            )

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
    HỆ THỐNG ĐĂNG KÝ VAY VỐN & QUẢN LÝ KHÁCH HÀNG • PHÁT TRIỂN BỞI NHÓM CHIẾN LƯỢC © 2026
</div>
""", unsafe_allow_html=True)
