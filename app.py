import streamlit as st
import pandas as pd
from io import BytesIO

# ==========================================
# CẤU HÌNH TRANG
# ==========================================
st.set_page_config(
    page_title="FinTech Platform - Nhóm Chiến Lược",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CSS DARK MODE NEUMORPHISM & NEON FINTECH
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Dynamic Dark Theme Base */
html, body, [class*="css"] { 
    font-family: 'Inter', sans-serif;
    color: #E2E8F0;
}

.stApp {
    background-color: #0A0E17;
    background-image: 
        radial-gradient(at 10% 10%, rgba(16, 185, 129, 0.08) 0px, transparent 50%),
        radial-gradient(at 90% 90%, rgba(59, 130, 246, 0.08) 0px, transparent 50%);
    background-attachment: fixed;
}

/* Hide Default Elements */
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

/* Custom Main Padding */
.block-container {
    max-width: 100% !important;
    padding: 2rem 3rem !important;
}

/* Dark Glassmorphism Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0F172A !important;
    border-right: 1px solid #1E293B;
}

section[data-testid="stSidebar"] > div { 
    padding: 2rem 1.2rem; 
}

/* Sidebar Brand Card */
.dark-brand-card {
    background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 20px 16px;
    text-align: center;
    margin-bottom: 24px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.dark-brand-icon {
    font-size: 24px;
    background: linear-gradient(135deg, #10B981, #059669);
    width: 48px;
    height: 48px;
    line-height: 48px;
    border-radius: 12px;
    margin: 0 auto 12px auto;
    color: #FFFFFF;
    box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);
}

.dark-brand-title {
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #F8FAFC;
    margin: 0;
}

.dark-brand-sub {
    font-size: 11px;
    color: #10B981;
    font-weight: 600;
    letter-spacing: 1px;
    margin-top: 4px;
}

/* Custom Navigation Buttons */
section[data-testid="stSidebar"] .stRadio label {
    background: #1E293B;
    border: 1px solid #334155;
    color: #94A3B8 !important;
    padding: 14px 18px;
    border-radius: 12px;
    margin-bottom: 10px;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    font-size: 14px !important;
    font-weight: 600 !important;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    border-color: #10B981;
    color: #10B981 !important;
    background: #0F172A;
    transform: translateX(4px);
    box-shadow: 0 0 12px rgba(16, 185, 129, 0.15);
}

/* Neon Hero Banner */
.neon-hero-card {
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(30, 41, 59, 0.9) 100%);
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 20px;
    padding: 32px;
    margin-bottom: 28px;
    box-shadow: 0 0 25px rgba(16, 185, 129, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.hero-text-title {
    font-size: 26px;
    font-weight: 800;
    color: #FFFFFF;
    margin: 0;
    letter-spacing: -0.5px;
    background: linear-gradient(90deg, #FFFFFF, #94A3B8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-text-sub {
    font-size: 14px;
    color: #10B981;
    margin-top: 6px;
    font-weight: 500;
}

.hero-tag {
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid #10B981;
    color: #10B981;
    padding: 8px 16px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
}

/* Glassmorphism Custom Card */
.glass-card {
    background: #0F172A;
    border: 1px solid #1E293B;
    border-radius: 20px;
    padding: 32px;
    margin-bottom: 24px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
}

/* Dark Mode Inputs */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-baseweb="textarea"] {
    background: #1E293B !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
    color: #F8FAFC !important;
}

div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"]:focus-within {
    border-color: #10B981 !important;
    box-shadow: 0 0 12px rgba(16, 185, 129, 0.25) !important;
}

label {
    color: #94A3B8 !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Glowing Neon Button */
.stButton > button, .stDownloadButton > button {
    height: 52px;
    border-radius: 12px !important;
    border: none !important;
    background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    letter-spacing: 0.5px;
    transition: all 0.3s ease !important;
    box-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 30px rgba(16, 185, 129, 0.5) !important;
}

/* Dark Metric Boxes */
div[data-testid="stMetric"] {
    background: #1E293B;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 20px;
}

div[data-testid="stMetricLabel"] {
    color: #64748B !important;
    font-size: 12px !important;
    font-weight: 700 !important;
}

div[data-testid="stMetricValue"] {
    color: #10B981 !important;
    font-weight: 800 !important;
    font-size: 26px !important;
}

/* Section Header */
.section-title-dark {
    font-size: 22px;
    font-weight: 800;
    color: #F8FAFC;
    margin-bottom: 4px;
}
.section-sub-dark {
    font-size: 13px;
    color: #64748B;
    margin-bottom: 20px;
}

/* Footer */
.footer-dark {
    text-align: center;
    color: #475569;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 1.5px;
    padding-top: 40px;
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
    <div class="dark-brand-card">
        <div class="dark-brand-icon">⚡</div>
        <div class="dark-brand-title">NHÓM CHIẾN LƯỢC</div>
        <div class="dark-brand-sub">FINTECH SYSTEM v2.0</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Menu Navigation",
        ["📝 Đăng ký nhu cầu vay", "🧮 Bảng tính trả góp", "🔐 Quản trị Admin"],
        label_visibility="collapsed"
    )

# ==========================================
# HERO BANNER
# ==========================================
st.markdown("""
<div class="neon-hero-card">
    <div>
        <div class="hero-text-title">⚡ FINTECH LOAN MANAGEMENT PLATFORM</div>
        <div class="hero-text-sub">Nền tảng số hóa thu thập nhu cầu vay & phân tích dữ liệu tài chính | Nhóm Chiến Lược</div>
    </div>
    <div class="hero-tag">DARK NEON v2.0</div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# TRANG 1: ĐĂNG KÝ VAY VỐN
# ==========================================
if page == "📝 Đăng ký nhu cầu vay":
    st.markdown("""
    <div class="section-title-dark">📝 ĐĂNG KÝ HỒ SƠ TƯ VẤN VAY</div>
    <div class="section-sub-dark">Điền thông tin bên dưới để kết nối trực tiếp với hệ thống xử lý hồ sơ tự động.</div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        name = st.text_input("👤 Họ và tên khách hàng (*)", placeholder="Nguyễn Văn A")
        phone = st.text_input("📱 Số điện thoại liên hệ (*)", placeholder="090xxxxxxx")
        address = st.text_input("📍 Tỉnh / Thành phố", placeholder="TP. Hồ Chí Minh")
        income = st.number_input("💵 Thu nhập hàng tháng (VNĐ)", min_value=0, step=1000000, value=15000000)

    with col2:
        loan_type = st.selectbox(
            "🏷️ Nhu cầu gói vay (*)",
            ["Vay Tín Chấp Theo Lương", "Vay Mua Nhà / BĐS", "Vay Mua Ô TÔ", "Vay Sản Xuất Kinh Doanh", "Vay Thấu Chi"]
        )
        loan_amount = st.number_input("💰 Số tiền đề xuất vay (VNĐ) (*)", min_value=10000000, step=10000000, value=100000000)
        tenure = st.selectbox("⏱️ Thời hạn vay mong muốn", ["12 tháng", "24 tháng", "36 tháng", "48 tháng", "60 tháng", "120 tháng"])
        income_type = st.radio("💳 Hình thức nhận lương", ["Chuyển khoản Ngân hàng", "Tiền mặt"], horizontal=True)

    note = st.text_area("📝 Ghi chú bổ sung", placeholder="Chi tiết nhu cầu hoặc thời gian tiện nghe điện thoại...", height=90)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⚡ KHỞI TẠO & GỬI HỒ SƠ TỰ ĐỘNG", type="primary", use_container_width=True):
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
            st.success("✅ Đã tiếp nhận hồ sơ thành công lên hệ thống Nhóm Chiến Lược!")
            st.balloons()
            
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TRANG 2: CÔNG CỤ TÍNH TRẢ GÓP
# ==========================================
elif page == "🧮 Bảng tính trả góp":
    st.markdown("""
    <div class="section-title-dark">🧮 DỰ TOÁN KHOẢN VAY (INTERACTIVE CALCULATOR)</div>
    <div class="section-sub-dark">Tính toán khoản vay theo phương thức dư nợ giảm dần tự động.</div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
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
    res3.metric("🔥 Tổng trả tháng đầu", format_money(total_first_month))

    st.caption("⚡ *Bảng tính mang tính chất tham khảo dựa trên lãi suất chuẩn.*")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TRANG 3: ADMIN QUẢN LÝ
# ==========================================
elif page == "🔐 Quản trị Admin":
    st.markdown("""
    <div class="section-title-dark">🔐 CỔNG ĐIỀU HÀNH ADMIN</div>
    <div class="section-sub-dark">Quản lý cơ sở dữ liệu đăng ký realtime và trích xuất báo cáo.</div>
    """, unsafe_allow_html=True)

    if not st.session_state.admin_logged_in:
        st.markdown("""
        <div style="max-width: 400px; margin: 40px auto; padding: 32px; background: #0F172A; border: 1px solid #1E293B; border-radius: 20px; text-align: center;">
            <div style="font-size: 36px; margin-bottom: 12px;">🔐</div>
            <h3 style="color: #F8FAFC; margin: 0 0 8px 0;">Xác thực Admin</h3>
            <p style="color: #64748B; font-size: 13px; margin-bottom: 24px;">Nhập mật khẩu quản trị để truy cập dữ liệu</p>
        </div>
        """, unsafe_allow_html=True)
        
        pwd = st.text_input("Mật khẩu truy cập", type="password", placeholder="••••••••", label_visibility="collapsed")
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🔓 TRUY CẬP DỮ LIỆU", type="primary", use_container_width=True):
            if pwd == "123456":
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("❌ Mật khẩu truy cập không chính xác.")
        
    else:
        top_col1, top_col2 = st.columns([5, 1])
        with top_col1:
            st.markdown('<div class="section-title-dark">📊 BẢNG DỮ LIỆU ĐĂNG KÝ VAY</div>', unsafe_allow_html=True)
        with top_col2:
            if st.button("🚪 Đăng xuất", use_container_width=True):
                st.session_state.admin_logged_in = False
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        if not st.session_state.loan_requests:
            st.info("📭 Chưa có hồ sơ mới gửi lên hệ thống.")
        else:
            df = pd.DataFrame(st.session_state.loan_requests)

            # Metrics
            m1, m2, m3 = st.columns(3)
            m1.metric("👥 Tổng hồ sơ tiếp nhận", f"{len(df)} hồ sơ")
            m2.metric("💰 Tổng nhu cầu vay vốn", format_money(df["Số tiền vay"].sum()))
            m3.metric("📊 Giá trị vay trung bình", format_money(df["Số tiền vay"].mean()))

            st.markdown("<br>", unsafe_allow_html=True)
            
            # Data Table
            st.dataframe(df, use_container_width=True, hide_index=True, height=380)

            st.markdown("<br>", unsafe_allow_html=True)
            excel_data = export_excel()
            st.download_button(
                label="📥 XUẤT DỮ LIỆU EXCEL (.XLSX)",
                data=excel_data,
                file_name="danh_sach_khach_hang_nhom_chien_luoc.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

# ==========================================
# FOOTER
# ==========================================
st.markdown("""
<div class="footer-dark">
    FINTECH PLATFORM • POWERED BY NHÓM CHIẾN LƯỢC © 2026
</div>
""", unsafe_allow_html=True)
