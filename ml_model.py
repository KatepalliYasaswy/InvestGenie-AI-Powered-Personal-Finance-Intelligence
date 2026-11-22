import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

import joblib

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/transactions.csv")

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------
df["Date"] = pd.to_datetime(df["Date"])

df["Day"] = df["Date"].dt.day
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

# -----------------------------
# ENCODING CATEGORICAL DATA
# -----------------------------
cat_enc = LabelEncoder()
pay_enc = LabelEncoder()

df["Category_enc"] = cat_enc.fit_transform(df["Category"])
df["Payment_enc"] = pay_enc.fit_transform(df["Payment_Mode"])

# -----------------------------
# FEATURES & TARGET
# -----------------------------
features = ["Income", "Category_enc", "Payment_enc", "Day", "Month"]
X = df[features]
y = df["Amount"]

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# MODEL
# -----------------------------
model = RandomForestRegressor(
    n_estimators=80,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    max_features="sqrt",
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# -----------------------------
# EVALUATION
# -----------------------------
pred = model.predict(X_test)

mae = mean_absolute_error(y_test, pred)
print("Model MAE:", mae)

# -----------------------------
# SAVE MODEL + ENCODERS
# -----------------------------
joblib.dump(
    model,
    "models/spending_model.pkl",
    compress=3
)
joblib.dump(cat_enc, "models/category_encoder.pkl")
joblib.dump(pay_enc, "models/payment_encoder.pkl")

print("Model Saved Successfully!")