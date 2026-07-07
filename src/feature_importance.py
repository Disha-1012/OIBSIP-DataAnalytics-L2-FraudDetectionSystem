import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load model
model = joblib.load("saved_models/best_model.pkl")

# Load dataset
df = pd.read_csv("data/raw/creditcard.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Features
X = df.drop("Class", axis=1)

# Feature Importance
importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("\nTop 15 Important Features:\n")
print(importance.head(15))

# Plot
plt.figure(figsize=(10,6))

importance.head(15).plot(kind="bar")

plt.title("Top 15 Important Features")

plt.xlabel("Features")

plt.ylabel("Importance")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("saved_models/feature_importance.png")

plt.show()