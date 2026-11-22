import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def perform_behavior_clustering(df):

    total_expense = df["Amount"].sum()

    food = df[df["Category"] == "Food"]["Amount"].sum()
    shopping = df[df["Category"] == "Shopping"]["Amount"].sum()
    entertainment = df[df["Category"] == "Entertainment"]["Amount"].sum()
    transport = df[df["Category"] == "Transport"]["Amount"].sum()

    transaction_count = len(df)

    avg_amount = df["Amount"].mean()

    current_user = pd.DataFrame({
        "total_expense": [total_expense],
        "food": [food],
        "shopping": [shopping],
        "entertainment": [entertainment],
        "transport": [transport],
        "transactions": [transaction_count],
        "avg_amount": [avg_amount]
    })

    sample_users = pd.DataFrame({
        "total_expense": [5000,8000,12000,18000,25000,35000],
        "food": [1000,2000,3000,5000,6000,9000],
        "shopping": [500,1000,2500,4500,7000,10000],
        "entertainment": [300,800,1500,2500,3500,5000],
        "transport": [500,700,1200,1500,2500,3500],
        "transactions": [20,30,40,50,70,90],
        "avg_amount": [250,280,320,360,420,500]
    })

    dataset = pd.concat(
        [sample_users, current_user],
        ignore_index=True
    )

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(dataset)

    kmeans = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10
    )

    dataset["cluster"] = kmeans.fit_predict(
        scaled_data
    )

    user_cluster = dataset.iloc[-1]["cluster"]

    cluster_names = {
        0: "Frugal Saver",
        1: "Balanced User",
        2: "Impulsive Spender",
        3: "Luxury Lifestyle User"
    }

    return (
        int(user_cluster),
        cluster_names[user_cluster],
        dataset,
        scaled_data
    )