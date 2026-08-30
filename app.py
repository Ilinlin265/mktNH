import streamlit as st
import pandas as pd
from io import BytesIO

# ==========================================
# CẤU HÌNH
# ==========================================

st.set_page_config(
    page_title="Quản lý khách hàng",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.image("logo.jpg")

# ==========================================
# CSS - GIAO DIỆN PREMIUM
# ==========================================

st.markdown("""
<style>

/* ==============================
   FONT + NỀN CHUNG
   ============================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 85% 5%, rgba(30, 64, 175, 0.08), transparent 25%),
        radial-gradient(circle at 5% 80%, rgba(59, 130, 246, 0.05), transparent 25%),
        #f5f7fb;
}

/* ==============================
   ẨN HEADER MẶC ĐỊNH
   ============================== */

header[data-testid="stHeader"] {
    background: transparent;
}

/* ==============================
   SIDEBAR
   ============================== */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #071A33 0%,
            #0A2342 55%,
            #0D2D52 100%
        );
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] > div {
    padding-top: 2rem;
}

section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

section[data-testid="stSidebar"] .stRadio label {
    padding: 13px 15px;
    border-radius: 12px;
    transition: all 0.25s ease;
    font-weight: 600;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,0.10);
    transform: translateX(3px);
}

section[data-testid="stSidebar"] [data-baseweb="radio"] {
    margin-bottom: 8px;
}

/* ==============================
   TITLE
   ============================== */

.main-title {
    font-size: 36px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #0B1F3A;
    margin-bottom: 5px;
}

.main-subtitle {
    color: #64748B;
    font-size: 15px;
    margin-bottom: 25px;
}

/* ==============================
   HEADER CARD
   ============================== */

.hero-card {
    position: relative;
    overflow: hidden;
    background:
        linear-gradient(
            135deg,
            #071A33 0%,
            #0C315C 60%,
            #124B7A 100%
        );
    padding: 34px 38px;
    border-radius: 24px;
    margin-bottom: 28px;
    box-shadow: 0 18px 45px rgba(7, 26, 51, 0.18);
}

.hero-card::before {
    content: "";
    position: absolute;
    width: 240px;
    height: 240px;
    border-radius: 50%;
    right: -80px;
    top: -100px;
    background: rgba(255,255,255,0.06);
}

.hero-card::after {
    content: "";
    position: absolute;
    width: 160px;
    height: 160px;
    border-radius: 50%;
    right: 120px;
    bottom: -100px;
    background: rgba(255,255,255,0.04);
}

.hero-title {
    position: relative;
    z-index: 2;
    color: white;
    font-size: 31px;
    font-weight: 800;
    margin: 0;
}

.hero-text {
    position: relative;
    z-index: 2;
    color: #C9D8EA;
    margin-top: 8px;
    font-size: 14px;
}

/* ==============================
   FORM CARD
   ============================== */

.form-card {
    background: rgba(255,255,255,0.95);
    border: 1px solid #E2E8F0;
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 10px 35px rgba(15, 23, 42, 0.06);
}

/* ==============================
   INPUT
   ============================== */

div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] {
    border-radius: 11px !important;
    border: 1px solid #D8E0EA !important;
    background: #FBFCFE !important;
    transition: all 0.2s ease;
}

div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"]:focus-within {
    border-color: #2563EB !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.10) !important;
}

label {
    font-weight: 600 !important;
    color: #334155 !important;
}

/* ==============================
   BUTTON
   ============================== */

.stButton > button,
.stDownloadButton > button {
    border-radius: 11px !important;
    min-height: 46px;
    font-weight: 700 !important;
    border: none !important;
    transition: all 0.25s ease !important;
}

.stButton > button[kind="primary"] {
    background:
        linear-gradient(
            135deg,
            #0B3B78,
            #1769AA
        ) !important;
    color: white !important;
    box-shadow: 0 8px 20px rgba(23,105,170,0.20);
}

.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(23,105,170,0.30);
}

.stDownloadButton > button {
    background:
        linear-gradient(
            135deg,
            #0B3B78,
            #1769AA
        ) !important;
    color: white !important;
}

.stDownloadButton > button:hover {
    transform: translateY(-2px);
}

/* ==============================
   METRIC CARD
   ============================== */

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #E2E8F0;
    padding: 20px 24px;
    border-radius: 18px;
    box-shadow: 0 8px 25px rgba(15,23,42,0.05);
}

div[data-testid="stMetricLabel"] {
    color: #64748B !important;
    font-weight: 600 !important;
}

div[data-testid="stMetricValue"] {
    color: #0B3B78 !important;
    font-weight: 800 !important;
}

/* ==============================
   DATAFRAME
   ============================== */

div[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid #E2E8F0;
    box-shadow: 0 8px 25px rgba(15,23,42,0.05);
}

/* ==============================
   ALERT
   ============================== */

div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* ==============================
   LOGIN CARD
   ============================== */

.login-wrapper {
    max-width: 520px;
    margin: 50px auto;
    background: white;
    padding: 42px;
    border-radius: 24px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 20px 55px rgba(15,23,42,0.10);
    text-align: center;
}

.login-icon {
    width: 72px;
    height: 72px;
    margin: auto;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    background:
        linear-gradient(
            135deg,
            #0B3B78,
            #1769AA
        );
    color: white;
    font-size: 34px;
    box-shadow: 0 12px 25px rgba(23,105,170,0.25);
}

.login-title {
    margin-top: 18px;
    font-size: 28px;
    font-weight: 800;
    color: #0B1F3A;
}

.login-text {
    color: #64748B;
    font-size: 14px;
    margin-bottom: 28px;
}

/* ==============================
   SECTION HEADER
   ============================== */

.section-title {
    font-size: 19px;
    font-weight: 800;
    color: #0B1F3A;
    margin-bottom: 4px;
}

.section-description {
    color: #64748B;
    font-size: 13px;
}

/* ==============================
   FOOTER
   ============================== */

.footer {
    text-align: center;
    margin-top: 50px;
    padding: 18px;
    color: #94A3B8;
    font-size: 12px;
    border-top: 1px solid #E2E8F0;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# KHỞI TẠO DANH SÁCH KHÁCH HÀNG
# ==========================================

if "customers" not in st.session_state:
    st.session_state.customers = []


# ==========================================
# HÀM XUẤT EXCEL
# ==========================================

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


# ==========================================
# MENU
# ==========================================

st.sidebar.markdown(
    """
    <div style="
        text-align:center;
        padding:10px 0 25px 0;
    ">
        <div style="
            font-size:42px;
            margin-bottom:8px;
        ">◆</div>

        <div style="
            font-size:19px;
            font-weight:800;
            letter-spacing:1px;
        ">
            CUSTOMER
        </div>

        <div style="
            font-size:11px;
            color:#9FB4CC !important;
            letter-spacing:2px;
            margin-top:4px;
        ">
            MANAGEMENT SYSTEM
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div style="
        font-size:11px;
        color:#9FB4CC !important;
        font-weight:700;
        letter-spacing:1.5px;
        margin:10px 0 8px 5px;
    ">
        ĐIỀU HƯỚNG
    </div>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Chọn trang",
    [
        "👤 Nhập khách hàng",
        "🔐 Admin"
    ],
    label_visibility="collapsed"
)

st.sidebar.markdown(
    """
    <div style="
        position:fixed;
        bottom:25px;
        color:#7890AA !important;
        font-size:11px;
        text-align:center;
        width:210px;
    ">
        © 2026 Customer Management
    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================
# TRANG NHẬP KHÁCH HÀNG
# ==========================================

if page == "👤 Nhập khách hàng":

    st.markdown(
        """
        <div class="hero-card">

            <div class="hero-title">
                👤 THÔNG TIN KHÁCH HÀNG
            </div>

            <div class="hero-text">
                Quản lý và lưu trữ thông tin khách hàng
                một cách chuyên nghiệp, nhanh chóng và bảo mật.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="form-card">
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-title">
            Thông tin khách hàng
        </div>

        <div class="section-description">
            Vui lòng nhập đầy đủ thông tin bên dưới.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------
    # NHẬP THÔNG TIN
    # --------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        phone = st.text_input(
            "📱 Số điện thoại",
            placeholder="Nhập số điện thoại"
        )

    with col2:

        name = st.text_input(
            "👤 Tên khách hàng",
            placeholder="Nhập tên khách hàng"
        )

    address = st.text_input(
        "📍 Địa chỉ",
        placeholder="Nhập địa chỉ"
    )

    note = st.text_area(
        "📝 Ghi chú",
        placeholder="Nhập ghi chú",
        height=120
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------
    # NÚT LƯU
    # --------------------------------------

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

            # Tạo khách hàng mới

            customer = {
                "Số điện thoại": phone.strip(),
                "Tên khách hàng": name.strip(),
                "Địa chỉ": address.strip(),
                "Ghi chú": note.strip()
            }

            # Lưu vào session

            st.session_state.customers.append(
                customer
            )

            st.success(
                "✅ Đã lưu thông tin khách hàng!"
            )

            st.balloons()

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    # --------------------------------------
    # THỐNG KÊ NHANH
    # --------------------------------------

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
                "📱 Thông tin đã lưu",
                len(st.session_state.customers)
            )

        with c3:
            st.metric(
                "🟢 Trạng thái",
                "Hoạt động"
            )


# ==========================================
# TRANG ADMIN
# ==========================================

elif page == "🔐 Admin":

    st.markdown(
        """
        <div class="hero-card">

            <div class="hero-title">
                🔐 ADMIN
            </div>

            <div class="hero-text">
                Khu vực quản trị dữ liệu khách hàng
                và xuất báo cáo.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ======================================
    # ĐĂNG NHẬP
    # ======================================

    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

    if not st.session_state.admin_logged_in:

        st.markdown(
            """
            <div class="login-wrapper">

                <div class="login-icon">
                    🔐
                </div>

                <div class="login-title">
                    ADMIN PORTAL
                </div>

                <div class="login-text">
                    Đăng nhập để truy cập hệ thống
                    quản lý khách hàng.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        password = st.text_input(
            "🔑 Mật khẩu",
            type="password",
            placeholder="Nhập mật khẩu Admin",
            label_visibility="visible"
        )

        if st.button(
            "🔓  ĐĂNG NHẬP",
            type="primary",
            use_container_width=True
        ):

            if password == "123456":

                st.session_state.admin_logged_in = True

                st.success(
                    "✅ Đăng nhập thành công."
                )

                st.rerun()

            else:

                st.error(
                    "❌ Sai mật khẩu."
                )


    # ======================================
    # ADMIN ĐÃ ĐĂNG NHẬP
    # ======================================

    else:

        col1, col2 = st.columns(
            [5, 1]
        )

        with col1:

            st.markdown(
                """
                <div class="section-title">
                    📊 DANH SÁCH KHÁCH HÀNG
                </div>

                <div class="section-description">
                    Theo dõi, kiểm tra và xuất dữ liệu khách hàng.
                </div>
                """,
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

        # ==================================
        # KIỂM TRA DỮ LIỆU
        # ==================================

        if len(st.session_state.customers) == 0:

            st.info(
                "📭 Chưa có khách hàng."
            )

        else:

            # ==============================
            # CHUYỂN SANG DATAFRAME
            # ==============================

            df = pd.DataFrame(
                st.session_state.customers
            )

            # ==============================
            # TỔNG KHÁCH HÀNG
            # ==============================

            c1, c2, c3 = st.columns(3)

            with c1:

                st.metric(
                    "👥 Tổng số khách hàng",
                    len(df)
                )

            with c2:

                st.metric(
                    "📱 Số điện thoại",
                    df["Số điện thoại"].notna().sum()
                )

            with c3:

                st.metric(
                    "🟢 Trạng thái hệ thống",
                    "Đang hoạt động"
                )

            st.markdown("<br>", unsafe_allow_html=True)

            # ==============================
            # HIỂN THỊ DANH SÁCH
            # ==============================

            st.markdown(
                """
                <div class="section-title">
                    Danh sách dữ liệu
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("<br>", unsafe_allow_html=True)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                height=430
            )

            st.markdown("<br>", unsafe_allow_html=True)

            # ==============================
            # XUẤT EXCEL
            # ==============================

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


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
    <div class="footer">
        CUSTOMER MANAGEMENT SYSTEM
        &nbsp; • &nbsp;
        Professional Customer Data Management
        &nbsp; • &nbsp;
        2026
    </div>
    """,
    unsafe_allow_html=True
)
