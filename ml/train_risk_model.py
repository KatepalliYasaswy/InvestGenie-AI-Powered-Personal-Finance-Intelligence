import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

from risk_prediction import create_risk_labels
import os

os.makedirs("models", exist_ok=True)
df = pd.read_csv("C://Users/ASUS/Videos/ml rp-1/data/transactions.csv")

df = create_risk_labels(df)

features = [
    "Amount",
    "Income",
    "Savings",
    "Spending_Ratio"
]

X = df[features]

le = LabelEncoder()

y = le.fit_transform(
    df["Risk_Level"]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(
    X_train,
    y_train
)

pickle.dump(
    model,
    open(
        "models/risk_model.pkl",
        "wb"
    )
)

pickle.dump(
    le,
    open(
        "models/label_encoder.pkl",
        "wb"
    )
)

print("Model Saved")