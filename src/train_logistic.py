import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

from imblearn.over_sampling import SMOTE

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/raw/creditcard.csv")

df.drop_duplicates(inplace=True)

# -----------------------------
# Features and Target
# -----------------------------
X = df.drop("Class", axis=1)
y = df["Class"]

# -----------------------------
# Scale Features
# -----------------------------
scaler = StandardScaler()

X["Amount"] = scaler.fit_transform(X[["Amount"]])
X["Time"] = scaler.fit_transform(X[["Time"]])

# -----------------------------
# Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------
# Apply SMOTE
# -----------------------------
smote = SMOTE(random_state=42)

X_train, y_train = smote.fit_resample(
    X_train,
    y_train
)

# -----------------------------
# Train Model
# -----------------------------
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------
print("\nAccuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))

print("\nConfusion Matrix")

print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")

print(classification_report(y_test, y_pred))

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, "saved_models/logistic_model.pkl")
joblib.dump(scaler, "saved_models/scaler.pkl")

print("\nModel Saved Successfully!")