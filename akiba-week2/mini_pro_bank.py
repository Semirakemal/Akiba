avilabele_amount = 1000
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

    print(" ====== AKIBA BANK ======= \n 1.Check Balance \n 2.Deposite Money \n 3.Withdraw Money \n 4.Exit")
    option = int(input("choose an option: "))
    
    if option == 1:
           print("your current balance is :" , avilabele_amount)
    elif option == 2:
           deposite = int(input("how much money you want to deposite ? "))
           uppdate_balance = avilabele_amount + deposite
           print("Deposite successfull \n your new balance is {uppdate_balance}")
           if deposite == 0 and deposite <= 0:
              print("enter valid amount")
    elif option == 3:
           withdraw = int(input("how much you want to withdraw? "))
           if withdraw == 0 and withdraw <= 0:
              print("enter valid amount")
           else:
               if withdraw > avilabele_amount:
                   print("inseficent balance!")
               else:
                   update = avilabele_amount - withdraw
                   print("your new balance is : {update} birr")
    else:
           print("Thank you for using Akiba Bank! \n Goodbye!")
    
    
    
        

