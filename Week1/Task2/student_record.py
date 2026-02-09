# student_records.py

students = []


def add_student(name, marks):
    students.append({"name": name, "marks": marks})
    print("Student added.")


def update_student(name, new_marks):
    for student in students:
        if student["name"] == name:
            student["marks"] = new_marks
            print("Record updated.")
            return
    print("Student not found.")


def display_students():
    if not students:
        print("No records available.")
    for student in students:
        print(f"Name: {student['name']}, Marks: {student['marks']}")


def main():
    while True:
        print("\n1. Add\n2. Update\n3. Display\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            marks = float(input("Marks: "))
            add_student(name, marks)
        elif choice == "2":
            name = input("Name to update: ")
            marks = float(input("New marks: "))
            update_student(name, marks)
        elif choice == "3":
            display_students()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
