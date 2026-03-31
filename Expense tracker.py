import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"


# Create file if not exists
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


# Add expense
def add_expense():
    category = input("Enter category (Food/Travel/Entertainment/etc): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("✅ Expense added successfully!")


# View expenses
def view_expenses():
    print("\n--- All Expenses ---")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


# Category summary
def category_summary():
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            summary[category] = summary.get(category, 0) + amount

    print("\n📊 Category-wise Summary:")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")


# Generate pie chart and save copy
def generate_pie_chart():
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            summary[category] = summary.get(category, 0) + amount

    if not summary:
        print("⚠️ No data to display!")
        return

    categories = list(summary.keys())
    amounts = list(summary.values())

    # Highlight largest category
    max_value = max(amounts)
    explode = [0.1 if amt == max_value else 0 for amt in amounts]

    plt.figure()
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', explode=explode)
    plt.title("Expense Distribution")

    # Save chart as image
    filename = f"expense_chart_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plt.savefig(filename)

    print(f"📁 Pie chart saved as: {filename}")

    plt.show()


# Main menu
def main():
    init_file()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Generate Pie Chart")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            generate_pie_chart()
        elif choice == "5":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice, try again.")


main()