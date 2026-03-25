import json
import os

FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add expense
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("✅ Expense added!")

# View expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print("\n📋 All Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['name']} - ₹{exp['amount']} ({exp['category']})")

# Show total
def show_total():
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total खर्च: ₹{total}")

# Main menu loop
def main():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Run app
if __name__ == "__main__":
    main()