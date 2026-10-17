largest = None
smallest = None
total = 0
even = 0
odd = 0

for i in range(10):
    num = int(input("Enter a number: "))

    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num
    total += num 
    if num % 2 == 0:
       even += 1
    else:
        odd += 1

average = total / 10

print("largest: ", largest)
print("smallest: ", smallest)
print("total: ", total)
print("Even: ", even)
print("odd: ", odd)