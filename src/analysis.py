import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])
    return df


def perform_analysis(df):
    total_spend = df["Amount"].sum()

    category_sum = df.groupby("Category")["Amount"].sum()

    monthly = df.copy()
    monthly["Month"] = monthly["Date"].dt.to_period("M")
    monthly_sum = monthly.groupby("Month")["Amount"].sum()

    payment_sum = df.groupby("Payment Method")["Amount"].sum()

    highest_category = category_sum.idxmax()

    avg_daily = df.groupby("Date")["Amount"].sum().mean()

    return {
        "Total Spending": total_spend,
        "Highest Category": highest_category,
        "Average Daily Spending": avg_daily
    }