class Student:
     school_name = " Akiba Acadamy"

     def __init__(self, name, score, department):
          self.name = name
          self.score = score
          self.department = department

     def display(self):
          print(f"Name: {self.name}")
          print(f"Score: {self.score}")
          print(f"Department: {self.department}")

student1 = Student("semira", 3 , "IT")
student2 = Student("saediya", 1 , "IT")
student3 = Student("Ebise", 2 , "MSE")

student1.school_name = "jimma Accadamy"

student1.display()
print(student1.school_name)
print()

student2.display()
print(student2.school_name)
print()

student3.display()
print(student3.school_name)



