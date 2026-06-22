students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = int(input("Enter marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("\nStudent Records:")
        for student in students:
            print(f"Name: {student['name']}, Roll: {student['roll']}, Marks: {student['marks']}")

def search_student():
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student Found!")
            print(f"Name: {student['name']}")
            print(f"Roll: {student['roll']}")
            print(f"Marks: {student['marks']}")
            return

    print("Student not found.")

def delete_student():
    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")

def update_marks():
    roll = input("Enter roll number: ")

    for student in students:
        if student["roll"] == roll:
            new_marks = int(input("Enter new marks: "))
            student["marks"] = new_marks
            print("Marks updated successfully!")
            return

    print("Student not found.")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Marks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_marks()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")