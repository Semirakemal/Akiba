#Employee Payslip
E_name = input("Enter Employ name: ")
B_salary = int(input("Enter salary: "))
T_allowance = int(input("Enter transport allowance: "))
F_allowance = int(input("Enter food alllowance: "))

G_salary = B_salary + T_allowance + F_allowance

line = "=================================="

line2 = "-----------------------"

print(f"{line}\n\t EMPLOYEE PAYSLIP\n{line}")

print(f"Employee: {E_name}")
print(f"Basic salary: {B_salary} ETB")
print(f"Transport Allowance: {T_allowance}")
print(f"Food Allownace: {F_allowance}")
print(line2 )
print("GROSS SALARY:", G_salary ,"ETB")
print(line)

