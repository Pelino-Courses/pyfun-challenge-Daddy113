from student import Student
from course import  Course
from instructor import Instructor
from teaching_assistant import TeachingAssistant


def main():
    students=[]
    courses=[]
    instructors=[]
    assistants=[]

    def find_student(name:str)->Student:
        name=name.lower().strip()
        return next((s for s in students if f"{s.first_name} {s.last_name}".lower().strip()==name),None)
    

    def find_course(code:str)->Course:
        return next((c for c in courses if c.code.lower().strip()==code.lower().strip()),None)


    def find_instructor(name:str)->Instructor:
        name=name.lower().strip()
        return next((i for i in instructors if f"{i.first_name} {i.last_name}".lower().strip()==name),None)

    def find_assistant(name: str)->TeachingAssistant:
        name=name.lower().strip()
        return next((a for a in assistants if f"{a.first_name} {a.last_name}".lower().strip()==name),None)

    while True:

        print("              University System ")
        print("1.Add Student")
        print("2.Add Course")
        print("3.Enroll Student in Course")
        print("4.Show Student Courses")
        print("5.Show Course Enrollments")
        print("6.Combine Student Course without duplicate")
        print("7.Add Instructor to Course")
        print("8.Remove Instructor from Course")
        print("9.Add Teaching Assistant to Course")
        print("10.Remove Teaching Assistant from Course")
        print("11.Unenroll Student from Course")
        print("12.Exit")
        print("13.Add Instructor")
        print("14.Add Teaching Assistant")

        choice=input("Choose an option you want: ").strip()

        if choice=="1":
            first=input("The First name: ")
            last=input("The Last name: ")
            student_id=input("The Student ID: ")
            students.append(Student(first,last,student_id))
            print(f"The Student {first} {last} added with ID {student_id}.")

        elif choice=="2":
            name=input("The Course name: ")
            code=input("The code of the course: ")
            course=Course(name,code)
            courses.append(course)
            print(f"Course {course} added.")

        elif choice=="3":
            student_name=input("Enter The full name of The student (e.g. Alice Stella): ")
            course_code=input("Enter code of the course: ")
            student=find_student(student_name)
            course=find_course(course_code)

            if student and course:
                student.enroll_in_course(course)
                print(f"{student} enrolled in {course}")
            else:
                print("The Student or course not found.")

        elif choice=="4":
            student_name=input("Enter The full name of the student: ")
            student=find_student(student_name)
            if student:
                print(f"{student}'s courses:")
                for course in student.get_courses():
                    print(f"-{course}")
            else:
                print("The Student not found.")

        elif choice=="5":
            course_code=input("Enter the code of the course: ")
            course=find_course(course_code)
            if course:
                print(f"Students in {course}:")
                for student in course.get_students():
                    print(f"-{student}")
            else:
                print("The Course not found.")

        elif choice=="7":
            course_code=input("Enter the code of the course: ")
            instructor_name=input("Enter Thefull name of instructor: ")
            course=find_course(course_code)
            instructor=find_instructor(instructor_name)

            if course and instructor:
                instructor.assign_course(course)
                print(f"Instructor {instructor} assigned to {course}")
            else:
                print("The Course or instructor not found.")

        elif choice=="8":
            course_code=input("Enter The code of the course: ")
            instructor_name=input("Enter The full name of instructor : ")
            course=find_course(course_code)
            instructor=find_instructor(instructor_name)
            if course and instructor:
                instructor.remove_course(course)
                print(f"Instructor {instructor} removed from {course}")
            else:
                print("Course or instructor not found.")

        elif choice=="9":
            course_code = input("Enter The code of the course: ")
            assistant_name = input("Enter full name of the assistant : ")
            course = find_course(course_code)
            assistant = find_assistant(assistant_name)
            if course and assistant:
                assistant.assign_course(course)
                print(f"Teaching Assistant {assistant} assigned to {course}")
            else:
                print("Course or assistant not found.")

        elif choice=="10":
            course_code = input("Enter course code: ")
            assistant_name = input("Enter full name of the assistant: ")
            course = find_course(course_code)
            assistant = find_assistant(assistant_name)
            if course and assistant:
                assistant.remove_course(course)
                print(f"Teaching Assistant {assistant} removed from {course}")
            else:
                print("The Course or assistant not found.")

        elif choice=="11":
            student_name=input("Enter full name of the student: ")
            course_code=input("Enter The code of the course: ")
            student=find_student(student_name)
            course=find_course(course_code)
            if student and course:
                student.unenroll_from_course(course)
                print(f"{student} unenrolled from {course}")
            else:
                print("The Student or course not found.")

        elif choice=="13": 
            first=input("The first name of the Instructor : ")
            last=input("The last name of the Instructor: ")
            instructors.append(Instructor(first,last))
            print(f"Instructor {first} {last} added.")

        elif choice=="14":  
            first=input("THE first name of The Teaching Assistant: ")
            last=input("The last name of the Teaching Assistant: ")
            assistants.append(TeachingAssistant(first,last))
            print(f"Teaching Assistant {first} {last} added.")

        elif choice=="12":
            print("Exiting our university system.")
            break
        else:
            print("Invalid option.Please Try again!!")

if __name__=="__main__":
    main()

