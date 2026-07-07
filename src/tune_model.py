import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import ExtraTreesClassifier

from sklearn.model_selection import RandomizedSearchCV

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

from imblearn.over_sampling import SMOTE

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("data/raw/creditcard.csv")

df.drop_duplicates(inplace=True)

# ==========================
# Features
# ==========================

X = df.drop("Class", axis=1)
y = df["Class"]

# ==========================
# Scaling
# ==========================

scaler = StandardScaler()

X["Amount"] = scaler.fit_transform(X[["Amount"]])
X["Time"] = scaler.fit_transform(X[["Time"]])

# ==========================
# Train Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    stratify=y,
    test_size=0.2,
    random_state=42
)

# ==========================
# SMOTE
# ==========================

smote = SMOTE(random_state=42)

X_train, y_train = smote.fit_resample(
    X_train,
    y_train
)

# ==========================
# Extra Trees
# ==========================

model = ExtraTreesClassifier(random_state=42)

# ==========================
# Parameters
# ==========================

params = {

    "n_estimators":[100,200,300,500],

    "max_depth":[10,20,30,None],

    "min_samples_split":[2,5,10],

    "min_samples_leaf":[1,2,4],

    "max_features":["sqrt","log2",None]

}

# ==========================
# Random Search
# ==========================

search = RandomizedSearchCV(

    estimator=model,

    param_distributions=params,

    n_iter=20,

    cv=5,

    scoring="f1",

    random_state=42,

    n_jobs=-1

)

search.fit(X_train,y_train)

print("\nBest Parameters\n")

print(search.best_params_)

best_model = search.best_estimator_

# ==========================
# Prediction
# ==========================

y_pred = best_model.predict(X_test)

print("\nAccuracy :",accuracy_score(y_test,y_pred))

print("Precision:",precision_score(y_test,y_pred))

print("Recall :",recall_score(y_test,y_pred))

print("F1 :",f1_score(y_test,y_pred))

print("ROC AUC :",roc_auc_score(y_test,y_pred))

print("\nConfusion Matrix")

print(confusion_matrix(y_test,y_pred))

print("\nClassification Report")

print(classification_report(y_test,y_pred))

# ==========================
# Save Model
# ==========================

joblib.dump(best_model,"saved_models/fraud_model.pkl")

joblib.dump(scaler,"saved_models/scaler.pkl")

print("\nModel Saved Successfully")