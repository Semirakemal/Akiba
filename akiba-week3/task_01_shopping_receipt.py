def calculate_subtotal(items):
    subtotal = 0
    for item in items:
        subtotal += item["price"] * item["quantity"]
    return subtotal

def calculate_discount(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.1
    elif subtotal >= 1000:
        return subtotal * 0.05
    else:
        return 0
    
def calculate_tax(amount,tax_rate):
    return amount * tax_rate/100
    

def generete_recipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)

    discounted_amount = subtotal - discount
    tax = calculate_tax(discounted_amount, tax_rate)

    final_amount = discounted_amount + tax

    return {
        "subtotal": subtotal ,
        "discount": discount,
        "tax": tax,
        "final_amount": final_amount
                }

items = []
number_of_items = int(input("how many products you need ? "))
for i in range(number_of_items):
    print(f"\n product {i + 1}")

    name = input("product name: ")
    price = float(input("price: "))
    quantity = int(input("quantity"))

    if price < 0 or quantity < 0:
        print("Error: price and quantity can not be negative ")
        raise SystemExit
    items.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

tax_rate = float(input("\n Enter tax rate(%): "))

if tax_rate < 0 or tax_rate > 100:
    print("Error: tax rate must be between 0 and 100")

    raise SystemError

receipt = generete_recipt(items, tax_rate)

print("\n ============= RECEIPT =============")

for item in items:
    cost = item["price"] * item["quantity"]

    print(f'{item["name"]}: {item["quantity"]} x ' f'{item["price"]:.2f} = {cost:.2f} Birr')

print("___________________________________________")
print(f'subtotal: {receipt["subtotal"]:.2f} Birr')
print(f'Discount: {receipt["discount"]:.2f} Birr')
print(f'Tax: {receipt["tax"]:.2f} Birr')
print(f'Final amount: {receipt["final_amount"]:.2f} Birr')
print("============================================")