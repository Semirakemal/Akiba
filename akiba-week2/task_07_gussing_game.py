count = 0
secret_no = 1

while count < 5 :
    count += 1
    correct_no = int(input("enter the secret number: "))
    if correct_no == secret_no:
        print("congratulations, you tried", count)
        break
    else:
        print("fail, you tried", count)
if count == 5 and correct_no != secret_no:
    print("Game over")
           