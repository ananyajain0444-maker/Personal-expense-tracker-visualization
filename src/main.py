from analysis import load_data, perform_analysis
from visualization import create_charts

def main():
    print("\n🚀 Starting Personal Expense Tracker...\n")

    df = load_data("data/expenses.csv")

    results = perform_analysis(df)

    create_charts(df)

    print("\n✅ Analysis Completed Successfully!")
    print("\n📊 Summary:")
    print(results)

if __name__ == "__main__":
    main()