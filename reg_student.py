from main import Student

try:
    student_name = input("Enter your name \n")
    student_id = input("Enter your id \n")
    student_class = input("Enter your class \n")

    Student.create(student_name = student_name, student_id = student_id, student_class = student_class)
    print("Student Created Successfully")


except:
    print("Failed to Admit student Use a Different id")


