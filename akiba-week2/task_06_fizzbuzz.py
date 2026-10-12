start_no = int(input("enter starting  number: "))
stop_no = int(input("enter stoping number: "))

for i in range(start_no,stop_no,1):
   
   if i % 3 == 0 and i % 5 == 0:
       print("FIZZBUZZ")
   elif i % 5 == 0:
       print("BUZZ")
   elif i % 3 == 0:
       print("FIZZ")
   else:
       print(i)
