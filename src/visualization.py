import pandas as pd
import matplotlib.pyplot as plt

def create_charts(df):

    # Category Chart
    plt.figure()
    df.groupby("Category")["Amount"].sum().plot(kind="bar")
    plt.title("Category-wise Spending")
    plt.tight_layout()
    plt.savefig("images/category_chart.png")
    plt.close()

    # Monthly Trend
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")

    plt.figure()
    df.groupby("Month")["Amount"].sum().plot(marker="o")
    plt.title("Monthly Spending Trend")
    plt.tight_layout()
    plt.savefig("images/monthly_trend.png")
    plt.close()

    # Payment Pie Chart
    plt.figure()
    df.groupby("Payment Method")["Amount"].sum().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Payment Method Distribution")
    plt.ylabel("")
    plt.savefig("images/payment_pie.png")
    plt.close()

    # Daily Trend
    plt.figure()
    df.groupby("Date")["Amount"].sum().plot()
    plt.title("Daily Spending Trend")
    plt.tight_layout()
    plt.savefig("images/daily_trend.png")
    plt.close()

    print("📊 Charts Generated Successfully!")