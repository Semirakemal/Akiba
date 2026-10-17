account = 1000
secret_pin = 1234
count = 0



while count < 3:
    count += 1
    attemps = 3 - count
    pin = int(input("Enter your pin: "))

    if secret_pin == pin:
        print("pin correct \n Welcome to Akiba Bank")
        break
        
    
    else:
        print("incorrect pin. \n Attempts reamining: ", attemps)

if attemps == 0 and secret_pin != pin:
    print("your account is looked")

if secret_pin == pin:
    checkBalance = 1
    Deposite_Money = 2
    Withdraw_Money = 3
    print(" ====== AKIBA BANK ======= \n 1.Check Balance \n 2. Deposite Money \n 3.Withdraw Money \n 4.Exit")

    option = input("choose an option: ")

    if option == 1:
        print("your current balance is :" , account)
        

