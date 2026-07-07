import matplotlib.pyplot as plt
import seaborn as sns


def class_distribution(df):

    fig, ax = plt.subplots(figsize=(6,4))

    df["Class"].value_counts().plot(
        kind="bar",
        ax=ax,
        color=["steelblue","red"]
    )

    ax.set_xticklabels(["Legitimate","Fraud"])

    ax.set_title("Class Distribution")

    return fig


def amount_distribution(df):

    fig, ax = plt.subplots(figsize=(8,4))

    ax.hist(df["Amount"], bins=50)

    ax.set_title("Transaction Amount Distribution")

    ax.set_xlabel("Amount")

    ax.set_ylabel("Count")

    return fig


def correlation_heatmap(df):

    fig, ax = plt.subplots(figsize=(12,8))

    sns.heatmap(
        df.corr(),
        cmap="coolwarm",
        ax=ax
    )

    return fig