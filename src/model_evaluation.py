import joblib
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    RocCurveDisplay
)

import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/raw/creditcard.csv")

X = df.drop("Class", axis=1)

y = df["Class"]

amount_scaler = StandardScaler()
time_scaler = StandardScaler()

X["Amount"] = amount_scaler.fit_transform(X[["Amount"]])
X["Time"] = time_scaler.fit_transform(X[["Time"]])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = joblib.load(
    "saved_models/best_model.pkl"
)

pred = model.predict(X_test)

cm = confusion_matrix(
    y_test,
    pred
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm
)

disp.plot()

plt.savefig(
    "saved_models/confusion_matrix.png"
)

plt.close()

RocCurveDisplay.from_estimator(
    model,
    X_test,
    y_test
)

plt.savefig(
    "saved_models/roc_curve.png"
)

plt.close()

print("Saved Successfully")