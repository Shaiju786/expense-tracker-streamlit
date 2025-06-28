import csv
from collections import defaultdict

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc.): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    
    print("Expense added!\n")

def view_summary():
    total = 0
    category_totals = defaultdict(float)

    with open('expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row['amount'])
            total += amount
            category_totals[row['category']] += amount

    print(f"Total expenses: ${total:.2f}")
    print("Expenses by category:")
    for cat, amt in category_totals.items():
        print(f"  {cat}: ${amt:.2f}")
    print()

def main():
    while True:
        print("Choose an option:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
