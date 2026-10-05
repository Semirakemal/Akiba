#currency exchange desk
USD_Amount = int(input("Enter the amount in USD: "))

Exchange_rate  = 150

ETB_Amount = USD_Amount * Exchange_rate
line = "=================================="
print(f"{line} \n \t CURRENCY EXCHANGES \n {line}")
print(f"USD_Amount: {USD_Amount}")

print(f"Exchange_rate: 1 USD = {Exchange_rate}")
print(f"ETB_Amount: {ETB_Amount}")
print(line)
