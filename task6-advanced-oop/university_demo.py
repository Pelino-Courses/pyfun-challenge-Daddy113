# university_demo.py
from student import Student
from course import Course
from teaching_assistant import TeachingAssistant

def main():
    students = []
    courses = []

    def find_student(name: str) -> Student:
        name = name.lower().strip()
        return next((s for s in students if f"{s.first_name} {s.last_name}".lower().strip() == name), None)

    def find_course(code: str) -> Course:
        return next((c for c in courses if c.code.lower().strip() == code.lower().strip()), None)

    while True:
        print("\n--- University System Menu ---")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Show Student Courses")
        print("5. Show Course Enrollments")
        print("6. Combine Student Course without duplicate")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            first = input("First name: ")
            last = input("Last name: ")
            students.append(Student(first, last))
            print(f"Student {first} {last} added.")

        elif choice == '2':
            name = input("Course name: ")
            code = input("Course code: ")
            course = Course(name, code)
            courses.append(course)
            print(f"Course {course} added.")

        elif choice == '3':
            student_name = input("Enter student full name (e.g. Alice Smith): ")
            course_code = input("Enter course code: ")
            student = find_student(student_name)
            course = find_course(course_code)
            if student and course:
                course.enroll(student)
                print(f"{student} enrolled in {course}")
            else:
                print("Student or course not found.")

        elif choice == '4':
            student_name = input("Enter student full name: ")
            student = find_student(student_name)
            if student:
                print(f"{student}'s courses:")
                for course in student.get_courses():
                    print(f" - {course}")
            else:
                print("Student not found.")

        elif choice == '5':
            course_code = input("Enter course code: ")
            course = find_course(course_code)
            if course:
                print(f"Students in {course}:")
                for student in course.get_students():
                    print(f" - {student}")
            else:
                print("Course not found.")

        elif choice == '6':
            name1 = input("First student full name: ")
            name2 = input("Second student full name: ")
            s1 = find_student(name1)
            s2 = find_student(name2)
            if s1 and s2:
                combined = s1 + s2
                print(f"Combined course load of {s1} and {s2}:")
                for c in combined:
                    print(f" - {c}")
            else:
                print("One or both students not found.")

        elif choice == '7':
            print("Exiting system.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
