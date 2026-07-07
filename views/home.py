import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def show():

    df = pd.read_csv("data/raw/creditcard.csv")

    fraud = int(df["Class"].sum())
    normal = len(df) - fraud

    st.title("Fraud Detection Dashboard")

    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Transactions",
        f"{len(df):,}"
    )

    c2.metric(
        "Fraud",
        fraud
    )

    c3.metric(
        "Legitimate",
        normal
    )

    c4.metric(
        "Fraud %",
        f"{fraud/len(df)*100:.3f}%"
    )

    st.markdown("---")

    left, right = st.columns([2, 1])

    with left:

        st.subheader("Dataset Preview")

        st.dataframe(df.head())

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
        [normal, fraud],
        labels=["Legitimate", "Fraud"],
        autopct="%1.2f%%",
        startangle=90
    )

    st.pyplot(fig)