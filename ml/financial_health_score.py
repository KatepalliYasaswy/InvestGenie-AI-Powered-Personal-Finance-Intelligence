import pandas as pd

def calculate_health_score(df, behavior_label, anomaly_count=0):

    total_income = df["Income"].sum()
    total_spending = df["Amount"].sum()
    total_savings = df["Savings"].sum()

    # -------------------
    # Savings Rate
    # -------------------
    savings_rate = (
        total_savings / total_income
        if total_income > 0 else 0
    )

    # -------------------
    # Spending Ratio
    # -------------------
    spending_ratio = (
        total_spending / total_income
        if total_income > 0 else 1
    )

    # -------------------
    # Payment Diversity
    # -------------------
    payment_diversity = (
        df["Payment_Mode"].nunique() / 5
    )

    # -------------------
    # Behavior Score
    # -------------------
    behavior_scores = {
        "Frugal Saver": 100,
        "Balanced User": 80,
        "Impulsive Spender": 50,
        "Luxury Lifestyle User": 30
    }

    behavior_score = behavior_scores.get(
        behavior_label,
        50
    )

    # -------------------
    # Anomaly Penalty
    # -------------------
    anomaly_penalty = anomaly_count * 5

    # -------------------
    # Weighted Score
    # -------------------
    score = (
        savings_rate * 30 +
        (1 - min(spending_ratio, 1)) * 25 +
        payment_diversity * 10 +
        (behavior_score / 100) * 15 +
        (1 - min(anomaly_count / 10, 1)) * 20
    )

    score = max(0, min(100, score))

    # -------------------
    # Health Status
    # -------------------
    if score >= 85:
        status = "Excellent"
    elif score >= 70:
        status = "Good"
    elif score >= 55:
        status = "Moderate"
    else:
        status = "Risky"

    return round(score, 2), status