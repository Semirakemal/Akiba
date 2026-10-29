def validate_score(score):
    return 0 <= score <= 100

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_average(students):
        total = 0
        count = 0

        for student in students:
            total += student["score"]
            count += 1

        if count == 0:
            return 0
        return total / count
    
def find_highest_score(students):
        if len(students) == 0:
            return None
        highest = students[0]["score"]

        for student in students:
            if student["score"] > highest:
                highest = student["score"]
        return highest

def find_lowest_score(students):
        if len(students) == 0:
            return None 
        lowest = students[0] ["score"]

        for student in students:
            if student["score"] < lowest:
                lowest = student["score"]

        return lowest


def count_passed_failed(students):
     passed = 0
     failed = 0

     for student in students:
          if student["score"] >= 50:
               passed += 1
          else:
               failed += 1
     return passed, failed

def students_above_average(students):

     average = calculate_average(students)
     result = []

     for student in students:
          if student["score"] > average:
               result.append(student)
     return result

def generate_report(students):

     valid_students = []

     print("STUDENT PERFORMANCE REPORT")

     print("=" * 35)

     for student in students:
          if validate_score(student["score"]):
               valid_students.append(student)
          else:
               print(
                    "Invalid score:",
                     student["name"],
                     "-",
                     student["score"]
               )

                       
               
     if len(valid_students) == 0:
        print("no valid student records avialable.")
        return
     print("\nINdividual REsults")
     print("-" * 35)

     for student in valid_students:
        name = student["name"]
        score = student["score"]
        grade = calculate_grade(score)
        
        if score >= 50:
            status = "passed"
        else:
            status = "failed" 
        print(
             name,
               "| score: ", score,
               "| grade: ", grade,
               "| status: ", status
                    ) 
     average = calculate_average(valid_students)
     highest = find_highest_score(valid_students)
     lowest = find_lowest_score(valid_students)
     passed = failed = count_passed_failed(valid_students)

     print("\nclass statistics")
     print("-" * 35)
     print("Number of students:", len(valid_students))
     print("Average score:", round(average, 2))
     print("Highest score:", highest)
     print("LOwest score:", lowest)
     print("Passed students", passed)
     print("Failed students", failed)

     above_average = students_above_average(valid_students)

     print("\nStudents Above Class Average")
     print("-" * 35)

     if len(above_average) == 0:
          print("No students scored above the average")
     else:
          for student in above_average:
              print(
                   student["name"],
                   "-",
                   student["score"]
              )

students = [
     {"name": "sara", "score": 85},
     {"name": "Ahmed", "score": 42},
     {"name": "musa", "score": 93},
     {"name": "hana", "score": 67}
]

generate_report(students)
               