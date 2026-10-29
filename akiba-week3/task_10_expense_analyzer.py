
def add_expense(expenses, description, category, amount):
    """Add an expense after validating its details."""
    description = description.strip()
    category = category.strip()

    if not description:
        print("Error: Description cannot be empty.")
        return False

    if not category:
        print("Error: Category cannot be empty.")
        return False

    if amount <= 0:
        print("Error: Amount must be greater than zero.")
        return False

    expense = {
        "description": description,
        "category": category.title(),
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully.")
    return True


def calculate_total_expenses(expenses):
    """Calculate the total amount spent."""
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def spending_by_category(expenses):
    """Calculate the total spending for each category."""
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals


def find_largest_expense(expenses):
    """Return the expense with the largest amount."""
    if len(expenses) == 0:
        return None

    largest = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense

    return largest


def expenses_above_threshold(expenses, threshold=200):
    """Return expenses whose amount exceeds the threshold."""
    result = []

    for expense in expenses:
        if expense["amount"] > threshold:
            result.append(expense)

    return result


def category_percentages(expenses):
    """Calculate each category's percentage of total spending."""
    total = calculate_total_expenses(expenses)
    category_totals = spending_by_category(expenses)
    percentages = {}

    if total == 0:
        return percentages

    for category, amount in category_totals.items():
        percentages[category] = (amount / total) * 100

    return percentages


def highest_spending_category(expenses):
    """Return the category with the highest total spending."""
    category_totals = spending_by_category(expenses)

    if len(category_totals) == 0:
        return None

    highest_category = None
    highest_amount = -1

    for category, amount in category_totals.items():
        if amount > highest_amount:
            highest_amount = amount
            highest_category = category

    return highest_category, highest_amount


def generate_spending_report(expenses, threshold=200):
    """Display a complete spending report."""
    print("\n" + "=" * 45)
    print("           EXPENSE ANALYSIS REPORT")
    print("=" * 45)

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    total = calculate_total_expenses(expenses)
    category_totals = spending_by_category(expenses)
    percentages = category_percentages(expenses)
    largest = find_largest_expense(expenses)
    above_threshold = expenses_above_threshold(expenses, threshold)
    highest_category = highest_spending_category(expenses)

    print(f"Number of expenses: {len(expenses)}")
    print(f"Total spending: {total:.2f} Birr")

    print("\nSPENDING BY CATEGORY")
    print("-" * 45)

    for category, amount in category_totals.items():
        percentage = percentages[category]
        print(
            f"{category}: {amount:.2f} Birr "
            f"({percentage:.2f}%)"
        )

    print("\nLARGEST EXPENSE")
    print("-" * 45)
    print(f"Description: {largest['description']}")
    print(f"Category: {largest['category']}")
    print(f"Amount: {largest['amount']:.2f} Birr")

    print("\nHIGHEST-SPENDING CATEGORY")
    print("-" * 45)
    category, amount = highest_category
    print(f"{category}: {amount:.2f} Birr")

    print(f"\nEXPENSES ABOVE {threshold:.2f} BIRR")
    print("-" * 45)

    if len(above_threshold) == 0:
        print("No expenses exceed this threshold.")
    else:
        for expense in above_threshold:
            print(
                f"{expense['description']} | "
                f"{expense['category']} | "
                f"{expense['amount']:.2f} Birr"
            )

    print("\nALL EXPENSES")
    print("-" * 45)

    for expense in expenses:
        print(
            f"{expense['description']} | "
            f"{expense['category']} | "
            f"{expense['amount']:.2f} Birr"
        )

    print("=" * 45)


def main():
    expenses = [
        {"description": "Lunch", "category": "Food", "amount": 180},
        {"description": "Taxi", "category": "Transport", "amount": 120},
        {"description": "Groceries", "category": "Food", "amount": 450},
        {"description": "Internet", "category": "Bills", "amount": 300}
    ]

    while True:
        print("\nFUNCTION-BASED EXPENSE ANALYZER")
        print("1. Add expense")
        print("2. Display spending report")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            description = input("Expense description: ")
            category = input("Expense category: ")

            try:
                amount = float(input("Expense amount in Birr: "))
                add_expense(expenses, description, category, amount)
            except ValueError:
                print("Error: Please enter a valid numeric amount.")

        elif choice == "2":
            try:
                threshold_input = input(
                    "Enter threshold in Birr (default 200): "
                ).strip()

                if threshold_input == "":
                    threshold = 200
                else:
                    threshold = float(threshold_input)

                if threshold < 0:
                    print("Threshold cannot be negative.")
                else:
                    generate_spending_report(expenses, threshold)

            except ValueError:
                print("Error: Please enter a valid threshold.")

        elif choice == "3":
            print("Thank you for using the Expense Analyzer.")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
