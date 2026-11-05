class Student:
    def __init__(self,name,student_id,department):
        self.name = name
        self.student_id = student_id
        self.department = department
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Department: {self.department}")

    def introduce(self):
        print(f"my name is {self.name}. i learn in jimma university. and my {self.student_id}. and am learning {self.department} ")

student1 = Student("semira","Ru0918","IT")
student2 = Student("Mehbuba","Ru0638","MSE")
student3 = Student("saediya","Ru0812","IT")

student1.display_info()
student1.introduce()
print()

student2.display_info()
student2.introduce()
print()

student3.display_info()
student3.introduce()

        