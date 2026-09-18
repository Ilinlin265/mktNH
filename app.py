import streamlit as st
import pandas as pd
from io import BytesIO
import os

# ==========================================
# CẤU HÌNH TRANG
# ==========================================
st.set_page_config(
    page_title="Hệ Thống Quản Lý Vay - Vietcombank",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CSS THEME VIETCOMBANK (GREEN & LIGHT)
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] { 
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Nền xám nhạt hiện đại */
.stApp {
    background-color: #F4F7F5;
}

#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

/* Dynamic Layout Padding */
.block-container {
    max-width: 100% !important;
    padding: 1.5rem 2.5rem 3rem 2.5rem !important;
}

/* Sidebar Trắng sạch chuẩn VCB */
section[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1px solid #E1E8E3;
}

section[data-testid="stSidebar"] > div { 
    padding: 1.5rem 1rem; 
}

/* Brand Card Sidebar */
.side-brand-box {
    background: linear-gradient(135deg, #01502F 0%, #027A45 100%);
    border-radius: 16px;
    padding: 20px 16px;
    text-align: center;
    color: #FFFFFF;
    margin-bottom: 20px;
    box-shadow: 0 8px 20px rgba(1, 80, 47, 0.15);
}

.side-brand-title {
    font-size: 15px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-top: 8px;
    color: #FFFFFF;
}

.side-brand-sub {
    font-size: 11px;
    color: #A3E6CD;
    font-weight: 600;
    letter-spacing: 1px;
    margin-top: 2px;
}

/* Sidebar Radio Buttons */
section[data-testid="stSidebar"] .stRadio label {
    background: #F8FAF9;
    border: 1px solid #E1E8E3;
    color: #2D3748 !important;
    padding: 12px 16px;
    border-radius: 10px;
    margin-bottom: 8px;
    transition: all 0.2s ease;
    font-size: 14px !important;
    font-weight: 600 !important;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    border-color: #01502F;
    background: #E8F5E9;
    color: #01502F !important;
    transform: translateX(4px);
}

/* Header Banner - Xanh Vietcombank */
.vcb-banner {
    background: linear-gradient(135deg, #01502F 0%, #027A45 60%, #003820 100%);
    border-radius: 20px;
    padding: 24px 32px;
    color: #FFFFFF;
    margin-bottom: 28px;
    box-shadow: 0 10px 25px rgba(1, 80, 47, 0.18);
}

.vcb-title {
    font-size: 26px;
    font-weight: 800;
    margin: 0;
    letter-spacing: -0.5px;
}

.vcb-sub {
    font-size: 14px;
    color: #C8E6C9;
    margin-top: 4px;
}

/* White Card Content Box */
.vcb-card {
    background: #FFFFFF;
    border-radius: 18px;
    padding: 32px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
    margin-bottom: 24px;
}

/* Input Fields */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-baseweb="textarea"] {
    background: #F8FAF9 !important;
    border: 1.5px solid #E1E8E3 !important;
    border-radius: 10px !important;
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

/* VCB Green Button */
.stButton > button, .stDownloadButton > button {
    height: 50px;
    border-radius: 10px !important;
    border: none !important;
    background: linear-gradient(135deg, #01502F 0%, #027A45 100%) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 6px 18px rgba(1, 80, 47, 0.2);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #003820 0%, #01502F 100%) !important;
    transform: translateY(-2px);
    box-shadow: 0 10px 22px rgba(1, 80, 47, 0.3);
}

/* Metrics */
div[data-testid="stMetric"] {
    background: #F8FAF9;
    border: 1px solid #E1E8E3;
    border-radius: 14px;
    padding: 18px;
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
    font-size: 24px !important;
}

.footer-vcb {
    text-align: center;
    color: #A0AEC0;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 1px;
    padding-top: 30px;
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
# SIDEBAR (BỔ SUNG LOGO)
# ==========================================
with st.sidebar:
    # Kiểm tra hỗ trợ cả tên LOGO.jpg lẫn logo.jpg
    logo_file = "LOGO.jpg" if os.path.exists("LOGO.jpg") else "logo.jpg"
    if os.path.exists(logo_file):
        st.image(logo_file, use_container_width=True)

    st.markdown("""
    <div class="side-brand-box">
        <div class="side-brand-title">NHÓM CHIẾN LƯỢC</div>
        <div class="side-brand-sub">QUẢN LÝ TÀI CHÍNH VAY</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Menu Navigation",
        ["📝 Đăng ký nhu cầu vay", "🧮 Bảng tính trả góp", "🔐 Quản trị Admin"],
        label_visibility="collapsed"
    )

# ==========================================
# BANNER ĐẦU TRANG (ĐÃ SỬA LỖI THIẾU CỘT)
# ==========================================
logo_col, text_col = st.columns([1, 5], gap="medium")

with logo_col:
    logo_file = "LOGO.jpg" if os.path.exists("LOGO.jpg") else "logo.jpg"
    if os.path.exists(logo_file):
        st.image(logo_file, width=130)
    else:
        st.warning("⚠️ Thiếu logo.jpg")

with text_col:
    st.markdown("""
    <div class="vcb-banner">
        <div class="vcb-title">🏦 HỆ THỐNG PHÁT TRIỂN & QUẢN LÝ KHÁCH HÀNG VAY</div>
        <div class="vcb-sub">Giải pháp số hóa tiếp nhận nhu cầu vay vốn & phân tích tài chính | Nhóm Chiến Lược</div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# TRANG 1: ĐĂNG KÝ VAY VỐN
# ==========================================
if page == "📝 Đăng ký nhu cầu vay":
    st.markdown("### 💳 Đăng Ký Tư Vấn Vay Vốn")
    st.caption("Khách hàng vui lòng điền đầy đủ thông tin bên dưới để Nhóm Chiến Lược tư vấn gói vay phù hợp nhất.")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="vcb-card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        name = st.text_input("👤 Họ và tên khách hàng (*)", placeholder="Nguyễn Văn A")
        phone = st.text_input("📱 Số điện thoại liên hệ (*)", placeholder="0901234567")
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
    st.markdown("### 🧮 Bảng Tính Lãi & Gốc Trả Góp")
    st.caption("Công cụ tính toán khoản vay theo dư nợ giảm dần do Nhóm Chiến Lược phát triển.")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="vcb-card">', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        calc_amount = st.number_input("💰 Số tiền vay (VNĐ)", min_value=10000000, value=200000000, step=10000000)
    with c2:
        calc_interest = st.number_input("📈 Lãi suất (%/năm)", min_value=1.0, max_value=25.0, value=8.5, step=0.1)
    with c3:
        calc_months = st.slider("⏱️ Thời gian vay (Tháng)", min_value=6, max_value=120, value=36, step=6)

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
    st.markdown("### 🔐 Cổng Điều Hành Admin")
    st.caption("Xem danh sách khách hàng và trích xuất dữ liệu đăng ký.")
    st.markdown("<br>", unsafe_allow_html=True)

    if not st.session_state.admin_logged_in:
        st.markdown("""
        <div style="max-width: 400px; margin: 30px auto; padding: 32px; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 18px; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
            <div style="font-size: 36px; margin-bottom: 8px;">🔐</div>
            <h3 style="color: #1A202C; margin: 0 0 6px 0;">Đăng Nhập Admin</h3>
            <p style="color: #718096; font-size: 13px; margin-bottom: 20px;">Nhập mật khẩu để truy cập hệ thống</p>
        </div>
        """, unsafe_allow_html=True)

        pwd = st.text_input("🔑 Mật khẩu admin", type="password", placeholder="••••••••", label_visibility="collapsed")
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🔓 XÁC NHẬN ĐĂNG NHẬP", type="primary", use_container_width=True):
            if pwd == "123456":
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("❌ Mật khẩu không đúng.")

    else:
        top_col1, top_col2 = st.columns([5, 1])
        with top_col1:
            st.subheader("📊 Danh Sách Hồ Sơ Khách Hàng")
        with top_col2:
            if st.button("🚪 Đăng xuất", use_container_width=True):
                st.session_state.admin_logged_in = False
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        if not st.session_state.loan_requests:
            st.info("📭 Chưa có thông tin đăng ký mới nào.")
        else:
            df = pd.DataFrame(st.session_state.loan_requests)

            # Thống kê KPI
            m1, m2, m3 = st.columns(3)
            m1.metric("👥 Tổng hồ sơ tiếp nhận", f"{len(df)} hồ sơ")
            m2.metric("💰 Tổng nhu cầu vay", format_money(df["Số tiền vay"].sum()))
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
<div class="footer-vcb">
    HỆ THỐNG ĐĂNG KÝ VAY VỐN & QUẢN LÝ KHÁCH HÀNG • PHÁT TRIỂN BỞI NHÓM CHIẾN LƯỢC © 2026
</div>
""", unsafe_allow_html=True)
