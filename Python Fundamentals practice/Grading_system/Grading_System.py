
# Grading System Program
# This program allows users to search for students by ID, update their grades,
# and view all students with their numeric and letter grades.

# Dictionary list storing student information: name, surname, ID, and grade
Students_grades = [
    {"name": "John", "Surname": "Doe", "Student_ID": 12345, "Grade": 85},
    {"name": "Jane", "Surname": "Smith", "Student_ID": 67890, "Grade": 92},
    {"name": "Alice", "Surname": "Johnson", "Student_ID": 54321, "Grade": 78},
    {"name": "Bob", "Surname": "Brown", "Student_ID": 98765, "Grade": 88},
    {"name": "Charlie", "Surname": "Davis", "Student_ID": 24680, "Grade": 95},
    {"name": "Eve", "Surname": "Miller", "Student_ID": 13579, "Grade": 82},
    {"name": "Frank", "Surname": "Wilson", "Student_ID": 11223, "Grade": 90},
    {"name": "Grace", "Surname": "Taylor", "Student_ID": 44556, "Grade": 80},
    {"name": "Hank", "Surname": "Anderson", "Student_ID": 77889, "Grade": 87},
    {"name": "Ivy", "Surname": "Thomas", "Student_ID": 99887, "Grade": 91}
]

# Function to convert numeric grades (0-100) to letter grades (1-7)
def grading_system(grade):
    if grade >= 80:
        return "7"
    elif grade >= 70:
        return "6"
    elif grade >= 60:
        return "5"
    elif grade >= 50:
        return "4"
    elif grade >= 40:
        return "3"
    elif grade >= 30:
        return "2"
    else:
        return "1"

# Function to search for a student by ID and optionally update their grade
def student_search(student_ID):
    for student in Students_grades:
        if student["Student_ID"] == student_ID:
            print(f"Student found: {student['name']} {student['Surname']}, Grade: {student['Grade']}")
            change_grade = input("Do you want to change the grade? (y/n): ").lower()
            if change_grade == "y":
                new_grade = int(input("Enter the new grade: "))
                student["Grade"] = new_grade
                print(f"Grade updated for {student['name']} {student['Surname']}: {student['Grade']}")
            return True
    return False

# Main loop: Allows users to search for students and update grades
while True:
    student_ID = int(input("Enter the Student ID: "))
    found = student_search(student_ID)
    if not found:
        print("Student not found.")
    another_search = input("Do you want to search for another student? (y/n): ").lower()
    if another_search != "y": 
        break

# Display all students with their numeric and letter grades
for student in Students_grades:
    student["Letter_Grade"] = grading_system(student["Grade"])
    print(f"{student['name']} {student['Surname']} - Grade: {student['Grade']} - Letter Grade: {student['Letter_Grade']}")
    

    
