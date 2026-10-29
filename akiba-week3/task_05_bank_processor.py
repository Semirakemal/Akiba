
def record_transaction(history, transaction_type, amount, balance):
    """Record a successful transaction."""
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": balance
    }

    history.append(transaction)


def deposit_money(balance, amount, history):
    """Deposit money into the account."""
    if amount <= 0:
        print("Error: Deposit amount must be greater than zero.")
        return balance

    balance += amount

    record_transaction(
        history, "deposit", amount, balance
    )

    print(f"Successfully deposited {amount:.2f} Birr.")
    return balance


def withdraw_money(
    balance, amount, history, withdrawn_today, daily_limit
):
    """Withdraw money while enforcing balance and daily limits."""
    if amount <= 0:
        print("Error: Withdrawal amount must be greater than zero.")
        return balance, withdrawn_today

    if amount > balance:
        print("Error: Insufficient balance.")
        return balance, withdrawn_today

    remaining_limit = daily_limit - withdrawn_today

    if amount > remaining_limit:
        print(
            "Error: Daily withdrawal limit exceeded.",
            f"Remaining limit: {remaining_limit:.2f} Birr."
        )
        return balance, withdrawn_today

    balance -= amount
    withdrawn_today += amount

    record_transaction(
        history, "withdrawal", amount, balance
    )

    print(f"Successfully withdrew {amount:.2f} Birr.")
    return balance, withdrawn_today


def check_balance(balance):
    """Display the current balance."""
    print(f"Current balance: {balance:.2f} Birr.")
    return balance


def generate_transaction_summary(history, opening_balance, balance):
    """Display totals, final balance, and transaction history."""
    total_deposited = 0
    total_withdrawn = 0

    for transaction in history:
        if transaction["type"] == "deposit":
            total_deposited += transaction["amount"]
        elif transaction["type"] == "withdrawal":
            total_withdrawn += transaction["amount"]

    print("\n" + "=" * 45)
    print("         TRANSACTION SUMMARY")
    print("=" * 45)

    print(f"Opening balance:  {opening_balance:.2f} Birr")
    print(f"Total deposited:  {total_deposited:.2f} Birr")
    print(f"Total withdrawn:  {total_withdrawn:.2f} Birr")
    print(f"Final balance:    {balance:.2f} Birr")

    print("\nTRANSACTION HISTORY")
    print("-" * 45)

    if len(history) == 0:
        print("No successful transactions.")
    else:
        for index, transaction in enumerate(history, start=1):
            print(f"\nTransaction {index}")
            print(f"Type: {transaction['type']}")
            print(f"Amount: {transaction['amount']:.2f} Birr")
            print(
                "Balance after: "
                f"{transaction['balance_after']:.2f} Birr"
            )

    print("\n" + "=" * 45)


def get_positive_or_zero_amount(prompt):
    """Read a numeric amount; reject non-numeric input."""
    try:
        amount = float(input(prompt))

        if not amount > 0:
            print("Enter an amount greater than zero.")
            return None

        return amount

    except ValueError:
        print("Invalid input. Enter a numeric amount.")
        return None


def main():
    print("BANK TRANSACTION PROCESSOR")
    print("=" * 35)

    # Configurable account settings
    opening_balance = 1000.00
    daily_withdrawal_limit = 2000.00

    balance = opening_balance
    history = []
    withdrawn_today = 0.00

    while True:
        print("\n1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Transaction summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            amount = get_positive_or_zero_amount(
                "Enter deposit amount: "
            )

            if amount is not None:
                balance = deposit_money(balance, amount, history)

        elif choice == "2":
            amount = get_positive_or_zero_amount(
                "Enter withdrawal amount: "
            )

            if amount is not None:
                balance, withdrawn_today = withdraw_money(
                    balance,
                    amount,
                    history,
                    withdrawn_today,
                    daily_withdrawal_limit
                )

        elif choice == "3":
            check_balance(balance)

        elif choice == "4":
            generate_transaction_summary(
                history, opening_balance, balance
            )
            print(
                "Daily withdrawal limit remaining: "
                f"{daily_withdrawal_limit - withdrawn_today:.2f} Birr"
            )

        elif choice == "5":
            generate_transaction_summary(
                history, opening_balance, balance
            )
            print("Thank you for using the banking program.")
            break

        else:
            print("Invalid option. Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
