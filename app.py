import streamlit as st

from views import home
from views import dataset
from views import prediction
from views import model
from views import about

st.set_page_config(
    page_title="Fraud Detection System",
    layout="wide"
)

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

    /* ================= Info / Success Boxes (main content) ================= */
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

    /* ================= Sidebar / Navbar ================= */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1E3A8A 0%, #1E293B 100%);
        border-right: none;
        box-shadow: 3px 0 15px rgba(0,0,0,0.15);
    }

    section[data-testid="stSidebar"] * {
        color: #E5E7EB;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        background: none;
    }

    /* Navigation radio group */
    section[data-testid="stSidebar"] .stRadio > label {
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    section[data-testid="stSidebar"] .stRadio [role="radiogroup"] label {
        padding: 0.5rem 0.8rem;
        border-radius: 8px;
        margin-bottom: 4px;
        transition: background-color 0.2s ease-in-out;
        font-weight: 500;
    }

    section[data-testid="stSidebar"] .stRadio [role="radiogroup"] label:hover {
        background-color: rgba(255, 255, 255, 0.08);
    }

    section[data-testid="stSidebar"] .stRadio [role="radiogroup"] label div:first-child {
        border-color: #93C5FD !important;
    }

    /* Sidebar divider */
    section[data-testid="stSidebar"] hr {
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.25), transparent);
    }

    /* Sidebar success box - "Best Model" */
    section[data-testid="stSidebar"] div[data-testid="stAlert"] {
        background-color: rgba(34, 197, 94, 0.15);
        border: 1px solid rgba(34, 197, 94, 0.35);
        box-shadow: none;
    }

    /* Sidebar info box - "Fraud Detection" */
    section[data-testid="stSidebar"] div[data-testid="stAlertContainer"],
    section[data-testid="stSidebar"] div[data-testid="stAlert"]:has(p) {
        border-radius: 12px;
    }

    /* Sidebar plain text (Extra Trees Classifier) */
    section[data-testid="stSidebar"] .stMarkdown p {
        color: #CBD5E1;
        font-weight: 500;
    }

    /* ================= Subheaders spacing tightening ================= */
    .stMarkdown {
        margin-bottom: 0.3rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Dataset",
        "Prediction",
        "Model Performance",
        "About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("🏆 Best Model")

st.sidebar.write("Extra Trees Classifier")

st.sidebar.markdown("---")

st.sidebar.info(
"""
💳 Fraud Detection

Machine Learning Project
"""
)

if page == "Home":
    home.show()

elif page == "Dataset":
    dataset.show()

elif page == "Prediction":
    prediction.show()
elif page == "Model Performance":
    model.show()
elif page == "About":
    about.show()