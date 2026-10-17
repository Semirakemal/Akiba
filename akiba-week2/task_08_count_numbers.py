n = int(input("enter the number: "))
total = 0
even = 0
odd = 0

i = 1
while i <= n:
   total += i
   i += 1

   if i % 2 == 0:
      even += 1
   if i % 2 == 1:
      odd += 1
      
   
print("odd", odd)
print("even =", even )   
print(total)