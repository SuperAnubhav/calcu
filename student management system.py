# Student Management System
print('\t\tSTUDENT MANAGEMENT SYSTEM' )
print()

students = []

# Function to add student
def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    grade = input("Enter grade: ")
    
    student = {
        'name': name,
        'roll_no': roll_no,
        'grade': grade
    }
    
    students.append(student)
    print(f"Student {name} added successfully!\n")

# Function to view all students
def view_students():
    if not students:
        print("No students found.\n")
    else:
        print("Student List:")
        for student in students:
            print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Grade: {student['grade']}")
        print()

# Function to search student by roll number
def search_student():
    roll_no = input("Enter roll number to search: ")
    for student in students:
        if student['roll_no'] == roll_no:
            print(f"Student Found: Name: {student['name']}, Roll No: {student['roll_no']}, Grade: {student['grade']}")
            return
    print("Student not found.\n")

# Function to delete student by roll number
def delete_student():
    roll_no = input("Enter roll number to delete: ")
    for student in students:
        if student['roll_no'] == roll_no:
            students.remove(student)
            print(f"Student with roll number {roll_no} deleted successfully!")
            return
    print("Student not found.\n")

# Main program loop
def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        print()

        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()