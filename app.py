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
# CSS - GIAO DIỆN
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f6f7f9;
}

/* ẨN MENU STREAMLIT */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}

/* =====================================================
   SIDEBAR
   ===================================================== */

section[data-testid="stSidebar"] {
    background: #0b1728;
    border-right: 1px solid #17283d;
}

section[data-testid="stSidebar"] > div {
    padding: 30px 20px;
}

section[data-testid="stSidebar"] label {
    color: #b9c5d4 !important;
}

/* LOGO SIDEBAR */

.side-logo {
    text-align: center;
    margin-bottom: 42px;
}

.side-symbol {
    width: 44px;
    height: 44px;
    border: 1px solid rgba(255,255,255,.5);
    transform: rotate(45deg);
    margin: auto;
    display: flex;
    align-items: center;
    justify-content: center;
}

.side-symbol span {
    transform: rotate(-45deg);
    color: white;
    font-size: 17px;
}

.side-brand {
    color: white;
    font-weight: 700;
    letter-spacing: 3px;
    font-size: 15px;
    margin-top: 19px;
}

.side-sub {
    color: #73859c;
    font-size: 9px;
    letter-spacing: 2px;
    margin-top: 6px;
}

/* MENU */

section[data-testid="stSidebar"] .stRadio label {
    padding: 12px 10px;
    border-radius: 10px;
    margin-bottom: 5px;
    transition: .2s;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: #14283f;
}

/* =====================================================
   MAIN
   ===================================================== */

.block-container {
    max-width: 1050px;
    padding-top: 42px;
    padding-bottom: 40px;
}

/* =====================================================
   HEADER
   ===================================================== */

.page-kicker {
    text-align: center;
    color: #8b96a5;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 4px;
    margin-bottom: 8px;
}

.page-title {
    text-align: center;
    color: #0b1c30;
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 5px;
}

.page-description {
    text-align: center;
    color: #8994a2;
    font-size: 13px;
    margin-bottom: 28px;
}

/* =====================================================
   IMAGE
   ===================================================== */

.image-card {
    background: white;
    border: 1px solid #e7ebf0;
    border-radius: 25px;
    padding: 14px;
    margin-bottom: 28px;
    box-shadow: 0 18px 55px rgba(16, 31, 48, .07);
}

.image-card img {
    border-radius: 17px;
}

/* =====================================================
   FORM CARD
   ===================================================== */

.form-card {
    background: white;
    border: 1px solid #e7ebf0;
    border-radius: 23px;
    padding: 32px 40px;
    box-shadow: 0 15px 45px rgba(16, 31, 48, .06);
}

.form-header {
    display: flex;
    align-items: center;
    gap: 14px;
    padding-bottom: 20px;
    margin-bottom: 24px;
    border-bottom: 1px solid #edf0f3;
}

.form-icon {
    width: 42px;
    height: 42px;
    border-radius: 12px;
    background: #0c2947;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 18px;
    flex-shrink: 0;
}

.form-title {
    color: #0b1c30;
    font-family: 'Playfair Display', serif;
    font-size: 23px;
    font-weight: 700;
}

.form-description {
    color: #929ca8;
    font-size: 11px;
    margin-top: 3px;
}

/* =====================================================
   INPUT
   ===================================================== */

div[data-baseweb="input"] > div {
    background: #f9fafb !important;
    border: 1px solid #e2e7ed !important;
    border-radius: 10px !important;
}

div[data-baseweb="textarea"] {
    background: #f9fafb !important;
    border: 1px solid #e2e7ed !important;
    border-radius: 10px !important;
}

div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"]:focus-within {
    border-color: #183d63 !important;
    box-shadow: 0 0 0 3px rgba(24,61,99,.08) !important;
}

label {
    color: #344154 !important;
    font-size: 12px !important;
    font-weight: 600 !important;
}

/* =====================================================
   BUTTON
   ===================================================== */

.stButton > button {
    min-height: 47px;
    border-radius: 10px !important;
    border: none !important;
    background: #0c2947 !important;
    color: white !important;
    font-weight: 700 !important;
    transition: .2s;
}

.stButton > button:hover {
    background: #173f67 !important;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(12,41,71,.18);
}

.stDownloadButton > button {
    min-height: 47px;
    border-radius: 10px !important;
    border: none !important;
    background: #0c2947 !important;
    color: white !important;
    font-weight: 700 !important;
}

/* =====================================================
   METRIC
   ===================================================== */

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e7ebf0;
    border-radius: 17px;
    padding: 18px 20px;
    box-shadow: 0 8px 25px rgba(16,31,48,.04);
}

div[data-testid="stMetricLabel"] {
    color: #7d8997 !important;
}

div[data-testid="stMetricValue"] {
    color: #0c2947 !important;
    font-weight: 700 !important;
}

/* =====================================================
   ADMIN LOGIN
   ===================================================== */

.login-box {
    background: white;
    border: 1px solid #e6ebf0;
    border-radius: 24px;
    padding: 40px;
    max-width: 500px;
    margin: 45px auto 25px auto;
    text-align: center;
    box-shadow: 0 20px 60px rgba(16,31,48,.09);
}

.login-symbol {
    width: 58px;
    height: 58px;
    background: #0c2947;
    border-radius: 50%;
    margin: auto;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 23px;
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

/* =====================================================
   SECTION
   ===================================================== */

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

/* =====================================================
   FOOTER
   ===================================================== */

.footer {
    text-align: center;
    color: #a1aab5;
    font-size: 10px;
    letter-spacing: 1.5px;
    padding-top: 35px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# KHỞI TẠO DANH SÁCH KHÁCH HÀNG
# =========================================================

if "customers" not in st.session_state:
    st.session_state.customers = []

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False


# =========================================================
# HÀM XUẤT EXCEL
# =========================================================

def export_excel():

    df = pd.DataFrame(
        st.session_state.customers
    )

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Khách hàng"
        )

    return output.getvalue()


# =========================================================
# MENU SIDEBAR
# =========================================================

st.sidebar.markdown("""
<div class="side-logo">

    <div class="side-symbol">
        <span>◆</span>
    </div>

    <div class="side-brand">
        CUSTOMER
    </div>

    <div class="side-sub">
        MANAGEMENT SYSTEM
    </div>

</div>
""", unsafe_allow_html=True)

st.sidebar.caption("ĐIỀU HƯỚNG")

page = st.sidebar.radio(
    "Chọn trang",
    [
        "👤 Nhập khách hàng",
        "🔐 Admin"
    ],
    label_visibility="collapsed"
)


# =========================================================
# TRANG NHẬP KHÁCH HÀNG
# =========================================================

if page == "👤 Nhập khách hàng":

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

    st.markdown(
        '<div class="page-kicker">'
        'CUSTOMER MANAGEMENT'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">'
        '👤 THÔNG TIN KHÁCH HÀNG'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">'
        'Vui lòng nhập thông tin khách hàng'
        '</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # ẢNH
    # -----------------------------------------------------

    st.markdown(
        '<div class="image-card">',
        unsafe_allow_html=True
    )

    # Tạo khoảng trống hai bên để ảnh nằm giữa
    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:

        try:

            st.image(
                "LOGO.jpg",
                use_container_width=True
            )

        except Exception:

            st.info(
                "📷 Chưa tìm thấy LOGO.jpg. "
                "Hãy đặt ảnh LOGO.jpg cùng thư mục với app.py."
            )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # FORM
    # -----------------------------------------------------

    st.markdown(
        '<div class="form-card">',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="form-header">

        <div class="form-icon">
            👤
        </div>

        <div>

            <div class="form-title">
                Thông tin khách hàng
            </div>

            <div class="form-description">
                Nhập thông tin vào các trường bên dưới
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


    # =====================================================
    # SỐ ĐIỆN THOẠI
    # =====================================================

    phone = st.text_input(
        "📱 Số điện thoại",
        placeholder="Nhập số điện thoại"
    )


    # =====================================================
    # TÊN KHÁCH HÀNG
    # =====================================================

    name = st.text_input(
        "👤 Tên khách hàng",
        placeholder="Nhập tên khách hàng"
    )


    # =====================================================
    # ĐỊA CHỈ
    # =====================================================

    address = st.text_input(
        "📍 Địa chỉ",
        placeholder="Nhập địa chỉ"
    )


    # =====================================================
    # GHI CHÚ
    # =====================================================

    note = st.text_area(
        "📝 Ghi chú",
        placeholder="Nhập ghi chú",
        height=100
    )


    st.markdown("<br>", unsafe_allow_html=True)


    # =====================================================
    # NÚT LƯU
    # =====================================================

    if st.button(
        "💾  LƯU THÔNG TIN",
        type="primary",
        use_container_width=True
    ):

        if phone.strip() == "":

            st.error(
                "❌ Vui lòng nhập số điện thoại."
            )

        elif name.strip() == "":

            st.error(
                "❌ Vui lòng nhập tên khách hàng."
            )

        else:

            customer = {
                "Số điện thoại": phone.strip(),
                "Tên khách hàng": name.strip(),
                "Địa chỉ": address.strip(),
                "Ghi chú": note.strip()
            }

            st.session_state.customers.append(
                customer
            )

            st.success(
                "✅ Đã lưu thông tin khách hàng!"
            )


    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # THỐNG KÊ
    # =====================================================

    if len(st.session_state.customers) > 0:

        st.markdown("<br>", unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "👥 Tổng khách hàng",
                len(st.session_state.customers)
            )

        with c2:

            st.metric(
                "📋 Hồ sơ đã lưu",
                len(st.session_state.customers)
            )

        with c3:

            st.metric(
                "🟢 Trạng thái",
                "Hoạt động"
            )


# =========================================================
# TRANG ADMIN
# =========================================================

elif page == "🔐 Admin":

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

    st.markdown(
        '<div class="page-kicker">'
        'SYSTEM ADMINISTRATION'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">'
        '🔐 ADMIN'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">'
        'Khu vực quản lý dữ liệu khách hàng'
        '</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # CHƯA ĐĂNG NHẬP
    # =====================================================

    if not st.session_state.admin_logged_in:

        st.markdown("""
        <div class="login-box">

            <div class="login-symbol">
                🔐
            </div>

            <div class="login-title">
                ADMIN PORTAL
            </div>

            <div class="login-description">
                Đăng nhập để truy cập hệ thống
                quản lý khách hàng
            </div>

        </div>
        """, unsafe_allow_html=True)


        password = st.text_input(
            "🔑 Mật khẩu",
            type="password",
            placeholder="Nhập mật khẩu Admin"
        )


        if st.button(
            "🔓  ĐĂNG NHẬP",
            type="primary",
            use_container_width=True
        ):

            if password == "123456":

                st.session_state.admin_logged_in = True

                st.rerun()

            else:

                st.error(
                    "❌ Sai mật khẩu."
                )


    # =====================================================
    # ADMIN ĐÃ ĐĂNG NHẬP
    # =====================================================

    else:

        col1, col2 = st.columns([6, 1])

        with col1:

            st.markdown(
                '<div class="section-title">'
                '📊 DANH SÁCH KHÁCH HÀNG'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="section-description">'
                'Quản lý và theo dõi dữ liệu khách hàng'
                '</div>',
                unsafe_allow_html=True
            )

        with col2:

            if st.button(
                "🚪 Đăng xuất",
                use_container_width=True
            ):

                st.session_state.admin_logged_in = False

                st.rerun()


        st.markdown("<br>", unsafe_allow_html=True)


        # =================================================
        # KIỂM TRA DỮ LIỆU
        # =================================================

        if len(st.session_state.customers) == 0:

            st.info(
                "📭 Chưa có khách hàng."
            )

        else:

            df = pd.DataFrame(
                st.session_state.customers
            )


            # =================================================
            # KPI
            # =================================================

            c1, c2, c3 = st.columns(3)

            with c1:

                st.metric(
                    "👥 Tổng số khách hàng",
                    len(df)
                )

            with c2:

                st.metric(
                    "📱 Hồ sơ liên hệ",
                    len(df)
                )

            with c3:

                st.metric(
                    "🟢 Trạng thái hệ thống",
                    "Hoạt động"
                )


            st.markdown("<br>", unsafe_allow_html=True)


            # =================================================
            # BẢNG
            # =================================================

            st.markdown(
                '<div class="section-title">'
                'Dữ liệu khách hàng'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown("<br>", unsafe_allow_html=True)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                height=420
            )


            st.markdown("<br>", unsafe_allow_html=True)


            # =================================================
            # XUẤT EXCEL
            # =================================================

            excel_file = export_excel()

            st.download_button(
                label="📥  XUẤT FILE EXCEL",
                data=excel_file,
                file_name="danh_sach_khach_hang.xlsx",
                mime=(
                    "application/vnd.openxmlformats-officedocument."
                    "spreadsheetml.sheet"
                ),
                use_container_width=True
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    CUSTOMER MANAGEMENT SYSTEM
    &nbsp; • &nbsp;
    PROFESSIONAL CUSTOMER EXPERIENCE
    &nbsp; • &nbsp;
    2026
</div>
""", unsafe_allow_html=True)
