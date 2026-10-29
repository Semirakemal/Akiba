
def add_product(inventory, name, price, stock):
    """Add a new product after validating its details."""
    name = name.strip()

    if not name:
        print("Error: Product name cannot be empty.")
        return False

    if name in inventory:
        print("Error: Product already exists.")
        return False

    if price < 0:
        print("Error: Price cannot be negative.")
        return False

    if stock < 0:
        print("Error: Stock cannot be negative.")
        return False

    inventory[name] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    print(f"Product '{name}' added successfully.")
    return True


def search_product(inventory, name):
    """Find and return a product, or None if not found."""
    name = name.strip()

    if name in inventory:
        return inventory[name]

    return None


def update_price(inventory, name, new_price):
    """Update the price of an existing product."""
    product = search_product(inventory, name)

    if product is None:
        print("Error: Product not found.")
        return False

    if new_price < 0:
        print("Error: Price cannot be negative.")
        return False

    product["price"] = new_price
    print(f"Price of '{name}' updated successfully.")
    return True


def increase_stock(inventory, name, quantity):
    """Increase the stock of an existing product."""
    product = search_product(inventory, name)

    if product is None:
        print("Error: Product not found.")
        return False

    if quantity <= 0:
        print("Error: Quantity must be greater than zero.")
        return False

    product["stock"] += quantity
    print(f"Stock of '{name}' increased by {quantity}.")
    return True


def sell_product(inventory, name, quantity):
    """Sell a product without exceeding available stock."""
    product = search_product(inventory, name)

    if product is None:
        print("Error: Product not found.")
        return False

    if quantity <= 0:
        print("Error: Sale quantity must be greater than zero.")
        return False

    if quantity > product["stock"]:
        print(
            "Error: Insufficient stock.",
            f"Available quantity: {product['stock']}"
        )
        return False

    product["stock"] -= quantity

    sale_total = product["price"] * quantity

    print(f"Sold {quantity} unit(s) of '{name}'.")
    print(f"Sale total: {sale_total:.2f} Birr")
    print(f"Remaining stock: {product['stock']}")

    return True


def calculate_inventory_value(inventory):
    """Calculate the total value of all products in stock."""
    total_value = 0

    for product in inventory.values():
        total_value += product["price"] * product["stock"]

    return total_value


def low_stock_report(inventory, threshold=5):
    """Return products whose stock is below the given threshold."""
    if threshold < 0:
        print("Error: Threshold cannot be negative.")
        return []

    low_stock_products = []

    for product in inventory.values():
        if product["stock"] < threshold:
            low_stock_products.append(product)

    return low_stock_products


def display_inventory(inventory):
    """Display all products and their details."""
    print("\nINVENTORY")
    print("-" * 55)

    if not inventory:
        print("Inventory is empty.")
        return

    for product in inventory.values():
        print(
            f"Name: {product['name']} | "
            f"Price: {product['price']:.2f} Birr | "
            f"Stock: {product['stock']}"
        )


def display_low_stock_report(inventory, threshold=5):
    """Display products below the configured stock threshold."""
    products = low_stock_report(inventory, threshold)

    print(f"\nLOW-STOCK REPORT (below {threshold} units)")
    print("-" * 40)

    if not products:
        print("No low-stock products.")
        return

    for product in products:
        print(
            f"{product['name']} - "
            f"{product['stock']} unit(s) remaining"
        )


def get_number(prompt, allow_zero=True):
    """Read a non-negative or positive number."""
    try:
        number = float(input(prompt))

        if number < 0 or (not allow_zero and number == 0):
            print("Invalid number.")
            return None

        return number

    except ValueError:
        print("Please enter a valid number.")
        return None


def get_quantity(prompt, allow_zero=True):
    """Read a whole-number quantity."""
    try:
        quantity = int(input(prompt))

        if quantity < 0 or (not allow_zero and quantity == 0):
            print("Invalid quantity.")
            return None

        return quantity

    except ValueError:
        print("Please enter a whole-number quantity.")
        return None


def main():
    inventory = {
        "Rice": {
            "name": "Rice",
            "price": 120.00,
            "stock": 10
        },
        "Sugar": {
            "name": "Sugar",
            "price": 90.00,
            "stock": 3
        },
        "Oil": {
            "name": "Oil",
            "price": 180.00,
            "stock": 7
        }
    }

    while True:
        print("\nINVENTORY STOCK CONTROLLER")
        print("=" * 35)
        print("1. Add product")
        print("2. Search product")
        print("3. Update product price")
        print("4. Increase stock")
        print("5. Sell product")
        print("6. Display inventory")
        print("7. Calculate inventory value")
        print("8. Low-stock report")
        print("9. Exit")

        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            name = input("Product name: ")
            price = get_number("Product price: ")
            stock = get_quantity("Initial stock: ")

            if price is not None and stock is not None:
                add_product(inventory, name, price, stock)

        elif choice == "2":
            name = input("Enter product name: ")
            product = search_product(inventory, name)

            if product is None:
                print("Product not found.")
            else:
                print("Product details:", product)

        elif choice == "3":
            name = input("Enter product name: ")
            new_price = get_number("Enter new price: ")

            if new_price is not None:
                update_price(inventory, name, new_price)

        elif choice == "4":
            name = input("Enter product name: ")
            quantity = get_quantity(
                "Quantity to add: ",
                allow_zero=False
            )

            if quantity is not None:
                increase_stock(inventory, name, quantity)

        elif choice == "5":
            name = input("Enter product name: ")
            quantity = get_quantity(
                "Quantity to sell: ",
                allow_zero=False
            )

            if quantity is not None:
                sell_product(inventory, name, quantity)

        elif choice == "6":
            display_inventory(inventory)

        elif choice == "7":
            total = calculate_inventory_value(inventory)
            print(f"Total inventory value: {total:.2f} Birr")

        elif choice == "8":
            threshold = get_quantity(
                "Enter low-stock threshold (default 5): "
            )

            if threshold is not None:
                display_low_stock_report(inventory, threshold)

        elif choice == "9":
            print("Thank you for using the Inventory Stock Controller.")
            break

        else:
            print("Invalid choice. Please select 1 to 9.")


if __name__ == "__main__":
    main()
