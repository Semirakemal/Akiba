n = int(input("enter the number: "))
total = 0
even = 0
odd = 0

i = 1
while i <= n:
    total += i
    if i % 2 == 0:
       print("even =", even )
       even += 1

    else:
      odd += 1
      print("odd", odd)
    i += 1
   

print(total)