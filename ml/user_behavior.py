import pandas as pd

def classify_user(df):

    total_expense = df["Amount"].sum()

    avg_expense = df["Amount"].mean()

    if total_expense < 5000:
        return "Saver"

    elif total_expense < 15000:
        return "Moderate Spender"

    else:
        return "High Spender"


def get_behavior_metrics(df):

    total_expense = df["Amount"].sum()

    avg_expense = round(
        df["Amount"].mean(),
        2
    )

    frequent_category = (
        df.groupby("Category")["Amount"]
        .sum()
        .idxmax()
    )

    return {
        "total": total_expense,
        "average": avg_expense,
        "category": frequent_category
    }