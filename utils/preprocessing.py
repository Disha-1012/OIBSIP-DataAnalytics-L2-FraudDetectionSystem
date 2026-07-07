import pandas as pd

from utils.load_model import (
    amount_scaler,
    time_scaler
)


def preprocess(df):

    df = df.copy()

    df["Time"] = time_scaler.transform(
        df[["Time"]]
    )

    df["Amount"] = amount_scaler.transform(
        df[["Amount"]]
    )

    return df