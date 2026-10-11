word = input("enter the word ")

reverse = ""

for words in word :
  word = reverse + words
  if word == reverse:
    print("palindrome")
  else:
    print("not palindrome")