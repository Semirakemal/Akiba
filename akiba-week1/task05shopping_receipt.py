# Shoping Receipt
c_name = input("enter your name: ")
p_name = input("enter product name: ")
price = int(input(f"enter price of {p_name}: "))
quantity = int(input (f"how many {p_name} do you want? "))

total_price = price * quantity

line = "=================================="

line2 = "-----------------------"

print(f"{line}\n\t RECEIPT\n{line}")
print(f"customer: {c_name}")
print(f"product\t price\t quntity \n{line2}\n{p_name}\t{price} ETB\t{quantity}")

print("Total = ", total_price )

print("Thankyou for shoping")
print(line)