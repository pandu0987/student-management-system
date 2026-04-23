students = []

# Load data
try:
    with open("students.txt", "r") as file:
        for line in file:
            students.append(line.strip())
except FileNotFoundError:
    pass

# Save function
def save_data():
    with open("students.txt", "w") as file:
        for s in students:
            file.write(s + "\n")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        save_data()
        print("Student added!")

    elif choice == "2":
        print("Students List:")
        for i in students:
            print(i)

    elif choice == "3":
        old = input("Enter name to update: ")
        new = input("Enter new name: ")

        if old in students:
            index = students.index(old)
            students[index] = new
            save_data()
            print("Updated successfully!")
        else:
            print("Student not found")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in students:
            students.remove(name)
            save_data()
            print("Deleted successfully!")
        else:
            print("Student not found")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")