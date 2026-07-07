import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier
)

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

from imblearn.over_sampling import SMOTE

# ============================
# Load Dataset
# ============================

df = pd.read_csv("data/raw/creditcard.csv")

df.drop_duplicates(inplace=True)

# ============================
# Split Features
# ============================

X = df.drop("Class", axis=1)
y = df["Class"]

# ============================
# Scaling
# ============================

amount_scaler = StandardScaler()
time_scaler = StandardScaler()

X["Amount"] = amount_scaler.fit_transform(X[["Amount"]])
X["Time"] = time_scaler.fit_transform(X[["Time"]])

# ============================
# Train Test Split
# ============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42
)

# ============================
# SMOTE
# ============================

smote = SMOTE(random_state=42)

X_train, y_train = smote.fit_resample(
    X_train,
    y_train
)

# ============================
# Models
# ============================

models = {

    "Logistic Regression":
        LogisticRegression(max_iter=1000),

    "Decision Tree":
        DecisionTreeClassifier(random_state=42),

    "Random Forest":
        RandomForestClassifier(random_state=42),

    "Extra Trees":
        ExtraTreesClassifier(
            n_estimators=100,
            max_depth=20,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1
        ),

    "Gradient Boosting":
        GradientBoostingClassifier(random_state=42),

    "AdaBoost":
        AdaBoostClassifier(random_state=42),

    "XGBoost":
        XGBClassifier(
            random_state=42,
            eval_metric="logloss"
        ),

    "LightGBM":
        LGBMClassifier(random_state=42),

    "CatBoost":
        CatBoostClassifier(
            verbose=0,
            random_state=42
        )
}

# ============================
# Compare Models
# ============================

results = []

best_model = None
best_f1 = 0

for name, model in models.items():

    print("=" * 60)
    print(name)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(y_test, y_pred)

    recall = recall_score(y_test, y_pred)

    f1 = f1_score(y_test, y_pred)

    roc = roc_auc_score(y_test, y_pred)

    print("Accuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1)
    print("ROC AUC  :", roc)

    results.append([
        name,
        accuracy,
        precision,
        recall,
        f1,
        roc
    ])

    if f1 > best_f1:
        best_f1 = f1
        best_model = model

# ============================
# Result Table
# ============================

results_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1",
        "ROC AUC"
    ]
)

print("\n")
print(results_df)

# ============================
# Save Best Model
# ============================

joblib.dump(
    best_model,
    "saved_models/best_model.pkl",
    compress=3)
joblib.dump(amount_scaler, "saved_models/amount_scaler.pkl")
joblib.dump(time_scaler, "saved_models/time_scaler.pkl")

print("\nBest Model Saved Successfully!")