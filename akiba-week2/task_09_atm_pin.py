count = 0
pin = 1234


while count < 3:
    count += 1
    attemps_remaining = 3 - count
    correct_pin = int(input("enter the correct pin: "))
    if correct_pin == pin:
        print("you are log in successfully")
    else:
        print("incorrect pin, Attemps remaining: ", attemps_remaining)
if attemps_remaining == 0 and correct_pin != pin:
    print("looked")
