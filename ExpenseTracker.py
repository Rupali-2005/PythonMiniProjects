def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})


def print_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Amount: {expense['amount']:.2f} | Category: {expense['category']}")


def total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)


def filter_expenses_by_category(expenses, category):
    return [expense for expense in expenses if expense['category'].lower() == category.lower()]


def main():
    expenses = []
    while True:
        print("\n========== Expense Tracker ==========")
        print("1. Add an expense")
        print("2. List all expenses")
        print("3. Show total expenses")
        print("4. Filter expenses by category")
        print("5. Exit")
        print("=====================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            try:
                amount = float(input("Enter amount: ").strip())
                category = input("Enter category: ").strip()
                add_expense(expenses, amount, category)
                print("Expense added successfully.")
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == '2':
            print("\nAll Expenses:")
            print_expenses(expenses)

        elif choice == '3':
            print(f"\nTotal Expenses: {total_expenses(expenses):.2f}")

        elif choice == '4':
            category = input("Enter category to filter: ").strip()
            filtered = filter_expenses_by_category(expenses, category)
            if filtered:
                print(f"\nExpenses in category '{category}':")
                print_expenses(filtered)
            else:
                print(f"No expenses found in category '{category}'.")

        elif choice == '5':
            print("Thank you for using Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()
