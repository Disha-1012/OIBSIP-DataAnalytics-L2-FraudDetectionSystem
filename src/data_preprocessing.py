import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

# Load Dataset
df = pd.read_csv("data/raw/creditcard.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Separate Features and Target
X = df.drop("Class",axis=1)

y = df["Class"]

# Scale Amount and Time
scaler = StandardScaler()

X["Amount"] = scaler.fit_transform(X[["Amount"]])

X["Time"] = scaler.fit_transform(X[["Time"]])

# Train Test Split

X_train,X_test,y_train,y_test = train_test_split(

X,
y,
test_size=0.2,
random_state=42,
stratify=y

)

print("Training Shape :",X_train.shape)

print("Testing Shape :",X_test.shape)