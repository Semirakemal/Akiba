class Student:
    def __init__(self,name,age,department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(f"my name is {self.name}")
        print(f"am {self.age} years old")
        print(f"i study {self.department}")

student1=Student("semira",22,"IT")
student2=Student("Mehbuba",23,"MSE")
student3=Student("Sarah",33,"BME")

student1.display_info()
print()
student2.display_info()
print()
student3.display_info()





