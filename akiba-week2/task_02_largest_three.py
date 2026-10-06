a = int(input("enput the first number: "))
b = int(input("enput the second number: "))
c = int(input("enput the thrird number: "))


if a == b == c:           # if all number are equal
    print(f"{a} equal to {b} equal to {c}")
elif a == b and a != c:           #  a and b are equal but c can be different
    if a > c:
        print(f" {a} and {b} are equal and {c} is smallest")
    else:
        print(f"{a} equal to {b} and {c} is largest")
elif a == c and a != b:            #  a and c are equal but b can be different
    if a > b:
        print(f" {a} and {c} are equal and {b} is smallest")
    else:
        print(f"{a} equal to {c} and {b} is largest")
elif b == c and b != a:            #  b and c are equal but a can be different
    if b > c:
        print(f" {b} and {c} are equal and {a} is smallest")
    else:
        print(f"{b} equal to {c} and {a} is largest")
else:                         #  if all three numbers are different
    if a > b and a > c:
        print(f"{a} is  largest number")
    elif b > a and b > c:
        print(f" {b} is largest number")
    else:
        print(f"{c} is largest number")