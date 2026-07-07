import joblib

model = joblib.load("saved_models/best_model.pkl")

amount_scaler = joblib.load(
    "saved_models/amount_scaler.pkl"
)

time_scaler = joblib.load(
    "saved_models/time_scaler.pkl"
)