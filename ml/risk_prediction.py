import pandas as pd

def create_risk_labels(df):

    df["Spending_Ratio"] = (
        df["Amount"] / df["Income"]
    )

    risk = []

    for ratio in df["Spending_Ratio"]:

        if ratio < 0.10:
            risk.append("Low")

        elif ratio < 0.30:
            risk.append("Medium")

        else:
            risk.append("High")

    df["Risk_Level"] = risk

    return df