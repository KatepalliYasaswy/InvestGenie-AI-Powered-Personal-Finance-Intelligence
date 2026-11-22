

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("C://Users/ASUS/Videos/ml rp-1/data/transactions.csv")

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------

user_df = df.groupby("User_ID").agg({
    "Amount": ["sum", "mean", "count"],
    "Income": "mean",
    "Savings": "mean"
})

user_df.columns = [
    "total_spent",
    "avg_spent",
    "transaction_count",
    "income",
    "savings"
]

user_df = user_df.reset_index()

# Ratios
user_df["savings_rate"] = user_df["savings"] / user_df["income"]
user_df["expense_ratio"] = user_df["total_spent"] / user_df["income"]
user_df["income_utilization"] = user_df["total_spent"] / user_df["income"]

# Target (synthetic but realistic scoring logic)
user_df["health_score"] = (
    (user_df["savings_rate"] * 50)
    + ((1 - user_df["expense_ratio"]) * 30)
    + ((1 - user_df["income_utilization"]) * 20)
) * 100

user_df["health_score"] = np.clip(user_df["health_score"], 0, 100)

# -----------------------------
# MODEL
# -----------------------------
features = [
    "total_spent",
    "avg_spent",
    "transaction_count",
    "income",
    "savings",
    "savings_rate",
    "expense_ratio",
    "income_utilization"
]

X = user_df[features]
y = user_df["health_score"]

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X, y)

joblib.dump(model, "financial_health_model.pkl")

print("Model trained successfully!")