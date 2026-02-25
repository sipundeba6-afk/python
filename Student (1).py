students = {}

def is_valid_marks(marks):
    if marks.replace('.', '', 1).isdigit():
        return True
    return False

def add_student():
    name = input("👤 Enter student name: ").strip()

    if name in students:
        print("⚠️ Student already exists!\n")
        return

    marks = input("📝 Enter marks: ")

    if is_valid_marks(marks):
        students[name] = float(marks)
        print("✅ Student added successfully!\n")
    else:
        print("❌ Invalid marks! Enter numbers only.\n")

def view_students():
    if not students:
        print("📭 No student records found!\n")
        return

    print("\n📚 Student Records:")
    print("----------------------------")
    for name, marks in students.items():
        print(f"👤 {name} ➝ 📝 {marks}")
    print()

def search_student():
    name = input("🔎 Enter student name to search: ").strip()

    if name in students:
        print(f"✅ Found: 👤 {name} ➝ 📝 {students[name]}\n")
    else:
        print("❌ Student not found!\n")

def update_student():
    name = input("✏️ Enter student name to update: ").strip()

    if name in students:
        marks = input("📝 Enter new marks: ")

        if is_valid_marks(marks):
            students[name] = float(marks)
            print("✅ Marks updated successfully!\n")
        else:
            print("❌ Invalid marks! Enter numbers only.\n")
    else:
        print("❌ Student not found!\n")

def delete_student():
    name = input("🗑️ Enter student name to delete: ").strip()

    if name in students:
        del students[name]
        print("✅ Student deleted successfully!\n")
    else:
        print("❌ Student not found!\n")

def calculate_average():
    if not students:
        print("📭 No student records found!\n")
        return

    avg = sum(students.values()) / len(students)
    print(f"📊 Class Average Marks: {avg:.2f}\n")

def show_topper():
    if not students:
        print("📭 No student records found!\n")
        return

    topper = max(students, key=students.get)
    print(f"🏆 Topper: 👑 {topper} ➝ 📝 {students[topper]}\n")

def show_grades():
    if not students:
        print("📭 No student records found!\n")
        return

    print("\n🎖️ Grade Report:")
    print("----------------------------")

    for name, marks in students.items():
        if marks >= 90:
            grade = "A+ 🌟"
        elif marks >= 75:
            grade = "A 🎉"
        elif marks >= 60:
            grade = "B 👍"
        elif marks >= 40:
            grade = "C 🙂"
        else:
            grade = "F ❌"

        print(f"👤 {name} ➝ 📝 {marks} ➝ 🎓 {grade}")
    print()

def main():
    while True:
        print("=================================")
        print("🎓 STUDENT GRADE BOOK SYSTEM 🎓")
        print("=================================")
        print("1️⃣ Add Student")
        print("2️⃣ View All Students")
        print("3️⃣ Search Student")
        print("4️⃣ Update Marks")
        print("5️⃣ Delete Student")
        print("6️⃣ Calculate Average")
        print("7️⃣ Show Topper")
        print("8️⃣ Show Grade Report")
        print("9️⃣ Exit")
        print("=================================")

        choice = input("👉 Enter your choice (1-9): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            show_topper()
        elif choice == "8":
            show_grades()
        elif choice == "9":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

main()