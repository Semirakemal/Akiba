word = input("enter the word ")

reverse = ""

for i in range(len(word) -1,-1,-1) :
  reverse += word[i]

if word == reverse:
    print("palindrome")
else:
    print("not palindrome")