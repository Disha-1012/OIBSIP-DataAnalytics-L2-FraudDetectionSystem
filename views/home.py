import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def show():

    # Dataset Statistics (Hardcoded)
    TOTAL_TRANSACTIONS = 284807
    FRAUD_TRANSACTIONS = 492
    LEGITIMATE_TRANSACTIONS = 284315
    TOTAL_FEATURES = 31
    FRAUD_PERCENTAGE = (FRAUD_TRANSACTIONS / TOTAL_TRANSACTIONS) * 100

    st.title("Fraud Detection Dashboard")

    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Transactions",
        f"{TOTAL_TRANSACTIONS:,}"
    )

    c2.metric(
        "Fraud",
        f"{FRAUD_TRANSACTIONS:,}"
    )

    c3.metric(
        "Legitimate",
        f"{LEGITIMATE_TRANSACTIONS:,}"
    )

    c4.metric(
        "Fraud %",
        f"{FRAUD_PERCENTAGE:.3f}%"
    )

    st.markdown("---")

    left, right = st.columns([2, 1])

    with left:

        st.subheader("Dataset Preview")

        st.info(
            """
            Dataset is used only during model training.

            The deployed application does not include the original dataset to keep the repository lightweight.

            Dataset Summary:

            • Total Transactions: 284,807

            • Legitimate: 284,315

            • Fraud: 492

            • Features: 31
            """
        )

    with right:

        st.subheader("Dataset Information")

        st.info(
        """
        ✔ Credit Card Dataset

        ✔ 31 Features

        ✔ PCA Transformed

        ✔ Binary Classification

        ✔ Highly Imbalanced Dataset
        """
        )

    st.markdown("---")

    st.subheader("Project Workflow")

    st.success("""
    1. Load Dataset

    2. Data Preprocessing

    3. Feature Scaling

    4. Extra Trees Classification

    5. Fraud Detection

    6. Download Prediction Results
    """)

    st.markdown("---")

    st.subheader("Fraud vs Legitimate Transactions")

    fig, ax = plt.subplots(figsize=(5, 5))

    ax.pie(
        [LEGITIMATE_TRANSACTIONS, FRAUD_TRANSACTIONS],
        labels=["Legitimate", "Fraud"],
        autopct="%1.2f%%",
        startangle=90
    )

    st.pyplot(fig)