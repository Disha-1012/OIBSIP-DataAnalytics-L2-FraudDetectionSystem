import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from imblearn.over_sampling import SMOTE

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/raw/creditcard.csv")

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# -----------------------------
# Separate Features and Target
# -----------------------------
X = df.drop("Class", axis=1)
y = df["Class"]

# -----------------------------
# Scale Time and Amount
# -----------------------------
scaler = StandardScaler()

X["Amount"] = scaler.fit_transform(X[["Amount"]])
X["Time"] = scaler.fit_transform(X[["Time"]])

# -----------------------------
# Train Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Before SMOTE")
print(y_train.value_counts())

# -----------------------------
# Apply SMOTE ONLY on training data
# -----------------------------
smote = SMOTE(random_state=42)

X_train_smote, y_train_smote = smote.fit_resample(
    X_train,
    y_train
)

print("\nAfter SMOTE")
print(y_train_smote.value_counts())