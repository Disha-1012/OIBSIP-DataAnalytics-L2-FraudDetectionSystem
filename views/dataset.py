import streamlit as st

def load_css():
    st.markdown(
        """
        <style>
        /* ================= Global Layout ================= */
        .main {
            background-color: #ffffff;
        }

        body, [class*="css"] {
            font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1300px;
        }

        /* ================= Headings ================= */
        h1 {
            background: linear-gradient(90deg, #1E3A8A, #2563EB);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            font-weight: 800;
            padding-bottom: 0.3rem;
            margin-bottom: 0.5rem;
        }

        h2 {
            color: #2563EB;
            font-weight: 700;
            margin-top: 0.5rem;
            margin-bottom: 0.6rem;
            border-left: 5px solid #2563EB;
            padding-left: 10px;
        }

        h3 {
            color: #374151;
            font-weight: 600;
        }

        /* ================= Buttons ================= */
        .stButton>button {
            background: linear-gradient(90deg, #2563EB, #1E40AF);
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-size: 18px;
            font-weight: 600;
            border: none;
            transition: all 0.25s ease-in-out;
            box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25);
        }

        .stButton>button:hover {
            background: linear-gradient(90deg, #1E40AF, #1E3A8A);
            color: white;
            box-shadow: 0 6px 14px rgba(30, 64, 175, 0.35);
            transform: translateY(-1px);
        }

        /* ================= Metric Cards ================= */
        div[data-testid="metric-container"] {
            background-color: #ffffff;
            border-radius: 14px;
            padding: 18px 16px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            transition: box-shadow 0.2s ease-in-out;
        }

        div[data-testid="metric-container"]:hover {
            box-shadow: 0 6px 18px rgba(37, 99, 235, 0.15);
        }

        div[data-testid="stMetricValue"] {
            color: #1E3A8A;
            font-weight: 800;
            font-size: 1.8rem;
        }

        div[data-testid="stMetricLabel"] {
            color: #6B7280;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.8rem;
            letter-spacing: 0.03em;
        }

        /* ================= Info / Success Boxes ================= */
        div[data-testid="stAlert"] {
            border-radius: 12px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.04);
            padding: 0.9rem 1.1rem;
        }

        div[data-testid="stAlert"] p {
            font-weight: 500;
        }

        /* ================= Dataframe / Table ================= */
        div[data-testid="stDataFrame"] {
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 3px 10px rgba(0,0,0,0.04);
            overflow: hidden;
        }

        /* ================= Divider ================= */
        hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, #d1d5db, transparent);
            margin: 0.8em 0;
        }

        /* ================= Sidebar ================= */
        section[data-testid="stSidebar"] {
            background-color: #ffffff;
            border-right: 1px solid #e5e7eb;
        }

        section[data-testid="stSidebar"] .stRadio label {
            font-weight: 500;
        }

        /* ================= Expander ================= */
        div[data-testid="stExpander"] {
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 3px 10px rgba(0,0,0,0.04);
        }

        /* ================= Subheaders spacing tightening ================= */
        .stMarkdown {
            margin-bottom: 0.3rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def show():

    load_css()

    st.title("Dataset Overview")

    st.markdown("---")

    st.subheader("Dataset Shape")

    c1, c2 = st.columns(2)

    c1.metric(
        "Rows",
        "284,807"
    )

    c2.metric(
        "Columns",
        "31"
    )

    st.markdown("---")

    st.subheader("Fraud Statistics")

    c1, c2, c3 = st.columns(3)

    legitimate = 284315
    fraud = 492
    fraud_percent = (fraud / 284807) * 100

    c1.metric(
        "Legitimate",
        legitimate
    )

    c2.metric(
        "Fraud",
        fraud
    )

    c3.metric(
        "Fraud %",
        f"{fraud_percent:.4f}%"
    )

    st.markdown("---")

    st.subheader("Dataset Preview")

    st.info("""
        The original dataset is intentionally excluded from deployment.

        Dataset Information:

        • Rows: 284,807

        • Columns: 31

        • PCA Features: V1–V28

        • Target Column: Class

        • Fraud Cases: 492
        """)

    st.markdown("---")

    st.subheader("Class Distribution")

    st.info("""
        Dataset Summary

        • Legitimate Transactions : 284,315

        • Fraudulent Transactions : 492

        • Fraud Percentage : 0.172%
        """)

    st.markdown("---")

    st.subheader("Transaction Amount Distribution")

    st.info("""
        The deployed application does not include the original dataset.

        Therefore, the transaction amount distribution chart is not displayed.
        """)

    st.markdown("---")

    with st.expander("Model Evaluation Charts"):

        st.image(
            "saved_models/confusion_matrix.png",
            caption="Confusion Matrix",
            use_container_width=True
        )

        st.image(
            "saved_models/roc_curve.png",
            caption="ROC Curve",
            use_container_width=True
        )

        st.image(
            "saved_models/feature_importance.png",
            caption="Feature Importance",
            use_container_width=True
        )