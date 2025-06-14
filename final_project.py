class Teacher:
    def __init__(self, tid, name, subject):
        self.id = tid
        self.name = name
        self.subject = subject
        self.students = []

class Student:
    def __init__(self, sid, name, grade):
        self.id = sid
        self.name = name
        self.grade = grade

teachers = {}
students = {}

def add_teacher():
    tid = input("Teacher ID: ")
    name = input("Name: ")
    subject = input("Subject: ")
    teachers[tid] = Teacher(tid, name, subject)
    print("Teacher added.")

def add_student():
    sid = input("Student ID: ")
    name = input("Name: ")
    grade = input("Grade: ")
    students[sid] = Student(sid, name, grade)
    print("Student added.")

def assign_student():
    tid = input("Teacher ID: ")
    sid = input("Student ID: ")
    if tid in teachers and sid in students:
        teachers[tid].students.append(sid)
        print("Student assigned.")
    else:
        print("Invalid IDs.")

def view_teachers():
    for t in teachers.values():
        print(f"ID: {t.id}, Name: {t.name}, Subject: {t.subject}, Students: {t.students}")

def view_students():
    for s in students.values():
        print(f"ID: {s.id}, Name: {s.name}, Grade: {s.grade}")

while True:
    print("\n1. Add Teacher\n2. Add Student\n3. Assign Student\n4. View Teachers\n5. View Students\n6. Exit")
    ch = input("Choice: ")
    if ch == "1": add_teacher()
    elif ch == "2": add_student()
    elif ch == "3": assign_student()
    elif ch == "4": view_teachers()
    elif ch == "5": view_students()
    elif ch == "6": break
    else: print("Invalid choice.")
