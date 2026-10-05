#exam result report
st_name = input("enter student name: ")
python_score = int(input("enter python score: "))
English_score = int(input("Enter English score: "))
Mathematics_score = int(input("Enter Mathematics score: "))

Total = python_score + English_score + Mathematics_score

Average = Total/3
line = "=================================="
line2 = "--------------------"

print(f"{line} \n \t STUDENT RESULT \n {line}")
print(f"student: {st_name}")
print(f"python: {python_score}")
print(f"English: {English_score}")
print(f"Mathematics: {Mathematics_score}")
print(line2)
print(f"Average score : {Average}")

print(line)
