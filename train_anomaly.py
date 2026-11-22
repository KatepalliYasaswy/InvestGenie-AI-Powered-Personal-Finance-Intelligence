import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/transactions.csv")

df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# STANDARDIZE PAYMENT TYPES
# -----------------------------
df["Payment_Mode"] = df["Payment_Mode"].replace({
    "creditcard": "Credit Card",
    "CreditCard": "Credit Card",
    "debitcard": "Debit Card",
    "banktransfer": "Bank Transfer",
    "UPI": "UPI",
    "Cash": "Cash"
})

# -----------------------------
# FEATURES
# -----------------------------
df["Day"] = df["Date"].dt.day
df["Month"] = df["Date"].dt.month

# -----------------------------
# ENCODING
# -----------------------------
cat_enc = LabelEncoder()
pay_enc = LabelEncoder()

df["Category_enc"] = cat_enc.fit_transform(df["Category"])
df["Payment_enc"] = pay_enc.fit_transform(df["Payment_Mode"])

features = [
    "Amount",
    "Income",
    "Category_enc",
    "Payment_enc",
    "Day",
    "Month"
]

X = df[features]

# -----------------------------
# MODEL
# -----------------------------
model = IsolationForest(
    n_estimators=200,
    contamination=0.05,
    random_state=42
)

model.fit(X)

# -----------------------------
# SAVE
# -----------------------------
joblib.dump(model, "models/anomaly_model.pkl")
joblib.dump(cat_enc, "models/category_encoder.pkl")
joblib.dump(pay_enc, "models/payment_encoder.pkl")

print("Model trained with full payment types")
print(pay_enc.classes_)