def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    expenses.append({"description": description, "amount": amount})
    print("Expense added successfully.")

def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - ${expense['amount']:.2f}")

def show_total():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: ${total:.2f}")

def show_average():
    if not expenses:
        print("No expenses to calculate average.")
        return
    total = sum(expense['amount'] for expense in expenses)
    average = total / len(expenses)
    print(f"Average expense: ${average:.2f}")

def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']}")
    choice = input("Expense number to delete: ")
    if not choice.isdigit():
        print("Invalid expense number.")
        return
    index = int(choice) - 1
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Deleted: {removed['description']}")
    else:
        print("Invalid expense number.")

expenses = []

def main():
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Show average")
        print("5. Delete an expense")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            show_average()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()