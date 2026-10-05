#BMI health information
name = input("enter your name: ")
weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))

BMI = weight / (height * height)

line = "=================================="
print(f"{line} \n \t BMI REPORT \n {line}")

print(f"Name: {name}")
print(f"weight: {weight} kg")
print(f"height: {height} m")
print(f"BMI: {BMI}")
print(line)
