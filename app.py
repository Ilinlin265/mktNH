# =========================================================
# TRANG NHẬP KHÁCH HÀNG
# =========================================================

if page == "👤 Nhập khách hàng":

    # -----------------------------------------
    # CSS RIÊNG CHO TRANG KHÁCH HÀNG
    # -----------------------------------------

    st.markdown("""
    <style>

    /* ===== KHUNG TRANG ===== */

    .customer-page {
        max-width: 1050px;
        margin: 0 auto;
    }

    /* ===== TIÊU ĐỀ ===== */

    .page-kicker {
        text-align: center;
        font-size: 10px;
        letter-spacing: 4px;
        color: #8b96a5;
        font-weight: 600;
        margin-bottom: 8px;
    }

    .page-heading {
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 36px;
        color: #0b1c30;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .page-desc {
        text-align: center;
        color: #8a95a3;
        font-size: 13px;
        margin-bottom: 30px;
    }

    /* ===== ẢNH ===== */

    .visual-box {
        background: white;
        border-radius: 26px;
        padding: 12px;
        border: 1px solid #e8edf2;
        box-shadow: 0 18px 50px rgba(15, 31, 49, .07);
        margin-bottom: 28px;
    }

    /* ===== FORM ===== */

    .customer-form {
        background: white;
        border-radius: 24px;
        padding: 34px 42px;
        border: 1px solid #e8edf2;
        box-shadow: 0 15px 45px rgba(15, 31, 49, .06);
    }

    .form-top {
        display: flex;
        align-items: center;
        gap: 14px;
        padding-bottom: 22px;
        border-bottom: 1px solid #edf0f3;
        margin-bottom: 25px;
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
    }

    .form-name {
        font-family: 'Playfair Display', serif;
        color: #0b1c30;
        font-size: 23px;
        font-weight: 700;
    }

    .form-small {
        color: #929ca9;
        font-size: 11px;
        margin-top: 2px;
    }

    /* ===== INPUT LABEL ===== */

    .stTextInput,
    .stTextArea {
        margin-bottom: 8px;
    }

    /* ===== BUTTON ===== */

    .save-space {
        margin-top: 10px;
    }

    /* ===== THỐNG KÊ ===== */

    .stats-title {
        text-align: center;
        color: #929ca9;
        font-size: 10px;
        letter-spacing: 2px;
        margin-top: 32px;
        margin-bottom: 14px;
    }

    </style>
    """, unsafe_allow_html=True)


    # =====================================================
    # HEADER
    # =====================================================

    st.markdown("""
    <div class="customer-page">

        <div class="page-kicker">
            CUSTOMER MANAGEMENT
        </div>

        <div class="page-heading">
            👤 THÔNG TIN KHÁCH HÀNG
        </div>

        <div class="page-desc">
            Vui lòng nhập thông tin khách hàng
        </div>

    </div>
    """, unsafe_allow_html=True)


    # =====================================================
    # ẢNH
    # =====================================================

    st.markdown(
        '<div class="visual-box">',
        unsafe_allow_html=True
    )

    # Ảnh nằm chính giữa
    col_left, col_center, col_right = st.columns(
        [1, 3, 1]
    )

    with col_center:

        st.image(
            "LOGO.jpg",
            use_container_width=True
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # FORM
    # =====================================================

    st.markdown(
        '<div class="customer-form">',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="form-top">

        <div class="form-icon">
            👤
        </div>

        <div>

            <div class="form-name">
                Thông tin khách hàng
            </div>

            <div class="form-small">
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


    # =====================================================
    # NÚT LƯU
    # =====================================================

    st.markdown(
        '<div class="save-space">',
        unsafe_allow_html=True
    )

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

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # THỐNG KÊ
    # =====================================================

    if len(st.session_state.customers) > 0:

        st.markdown(
            '<div class="stats-title">'
            'THỐNG KÊ HỒ SƠ KHÁCH HÀNG'
            '</div>',
            unsafe_allow_html=True
        )

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
