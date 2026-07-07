import streamlit as st
import pandas as pd

from utils.load_model import (
    model,
    amount_scaler,
    time_scaler
)

from utils.preprocessing import preprocess


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

        /* ================= Download Button ================= */
        .stDownloadButton>button {
            background: linear-gradient(90deg, #2563EB, #1E40AF);
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-size: 16px;
            font-weight: 600;
            border: none;
            transition: all 0.25s ease-in-out;
            box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25);
        }

        .stDownloadButton>button:hover {
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

        /* ================= Info / Success / Error Boxes ================= */
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

        /* ================= Tabs ================= */
        button[data-baseweb="tab"] {
            font-weight: 600;
            color: #374151;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            color: #2563EB;
        }

        div[data-baseweb="tab-highlight"] {
            background-color: #2563EB;
        }

        /* ================= Number Input / File Uploader ================= */
        div[data-testid="stNumberInput"] input {
            border-radius: 8px;
        }

        div[data-testid="stFileUploaderDropzone"] {
            border-radius: 12px;
            border: 1.5px dashed #93c5fd;
            background-color: #f8fafc;
        }

        /* ================= Progress Bar ================= */
        div[data-testid="stProgress"] > div > div {
            background-color: #2563EB;
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

    st.title("Fraud Prediction")

    # Main Tabs
    manual_tab, upload_tab = st.tabs(
        [
            "📝 Manual Prediction",
            "📂 CSV Upload"
        ]
    )

    # =====================================================
    # MANUAL PREDICTION
    # =====================================================

    with manual_tab:

        st.write(
            "Enter the transaction details below."
        )

        tab1, tab2, tab3 = st.tabs(
            [
                "Transaction",
                "V1 - V14",
                "V15 - V28"
            ]
        )

        # Transaction Details

        with tab1:

            time = st.number_input(
                "Time",
                value=0.0
            )

            amount = st.number_input(
                "Amount",
                value=0.0
            )

        values = {}

        # V1-V14

        with tab2:

            col1, col2 = st.columns(2)

            for i in range(1, 15):

                if i % 2 == 0:

                    values[f"V{i}"] = col2.number_input(
                        f"V{i}",
                        value=0.0,
                        key=f"manual_V{i}"
                    )

                else:

                    values[f"V{i}"] = col1.number_input(
                        f"V{i}",
                        value=0.0,
                        key=f"manual_V{i}"
                    )

        # V15-V28

        with tab3:

            col1, col2 = st.columns(2)

            for i in range(15, 29):

                if i % 2 == 0:

                    values[f"V{i}"] = col2.number_input(
                        f"V{i}",
                        value=0.0,
                        key=f"manual_V{i}"
                    )

                else:

                    values[f"V{i}"] = col1.number_input(
                        f"V{i}",
                        value=0.0,
                        key=f"manual_V{i}"
                    )

        st.markdown("---")

        if st.button("🔍 Predict Transaction"):

            sample = {
                "Time": time,
                **values,
                "Amount": amount
            }

            df = pd.DataFrame([sample])

            df = preprocess(df)

            prediction = model.predict(df)[0]

            probability = model.predict_proba(df)[0]

            st.markdown("---")

            st.subheader("Prediction Result")

            if prediction == 0:

                st.success("✅ Legitimate Transaction")

            else:

                st.error("🚨 Fraudulent Transaction")

            st.subheader("Prediction Probability")

            st.write(
                f"Legitimate : {probability[0]*100:.2f}%"
            )

            st.write(
                f"Fraud : {probability[1]*100:.2f}%"
            )

            st.progress(float(probability[1]))

    # =====================================================
    # CSV UPLOAD
    # =====================================================

    with upload_tab:

        st.subheader("📂 Batch Fraud Detection")

        st.write(
            "Upload a CSV file containing multiple transactions."
        )

        uploaded_file = st.file_uploader(
            "Choose a CSV file",
            type=["csv"]
        )

        if uploaded_file is not None:

            df = pd.read_csv(uploaded_file)

            st.success("File uploaded successfully!")

            st.subheader("Dataset Preview")

            st.dataframe(df.head())

            required_columns = [
                "Time",
                "V1", "V2", "V3", "V4", "V5",
                "V6", "V7", "V8", "V9", "V10",
                "V11", "V12", "V13", "V14",
                "V15", "V16", "V17", "V18",
                "V19", "V20", "V21", "V22",
                "V23", "V24", "V25", "V26",
                "V27", "V28",
                "Amount"
            ]

            missing = [
                col
                for col in required_columns
                if col not in df.columns
            ]

            if missing:

                st.error(
                    f"Missing columns:\n{missing}"
                )

            else:

                # Remove target column if it exists
                prediction_df = df.copy()

                if "Class" in prediction_df.columns:
                    prediction_df = prediction_df.drop(columns=["Class"])

                processed = preprocess(prediction_df)
                
                predictions = model.predict(processed)

                probabilities = model.predict_proba(processed)
                result_df = df.copy()

                result_df["Prediction"] = predictions

                result_df["Fraud Probability (%)"] = (
                    probabilities[:, 1] * 100
                ).round(2)

                result_df["Prediction"] = result_df[
                    "Prediction"
                ].replace(
                    {
                        0: "Legitimate",
                        1: "Fraud"
                    }
                )

                if "Class" in result_df.columns:

                    actual = result_df["Class"].replace(
                        {
                            0: "Legitimate",
                            1: "Fraud"
                        }
                    )

                    result_df["Actual"] = actual

                    result_df["Correct"] = (
                        result_df["Prediction"] == result_df["Actual"]
                    )

                st.subheader("Prediction Results")

                st.dataframe(result_df)

                fraud_count = (
                    result_df["Prediction"] == "Fraud"
                ).sum()

                legit_count = (
                    result_df["Prediction"] == "Legitimate"
                ).sum()

                col1, col2 = st.columns(2)

                col1.metric(
                    "Fraud Transactions",
                    fraud_count
                )

                col2.metric(
                    "Legitimate Transactions",
                    legit_count
                )

                csv = result_df.to_csv(
                    index=False
                ).encode("utf-8")

                st.download_button(
                    "⬇ Download Prediction Results",
                    csv,
                    "fraud_predictions.csv",
                    "text/csv"
                )