class Student:
    def __init__(self,first_name,last_name,student_id):
        self.first_name=first_name
        self.last_name=last_name
        self.student_id=student_id
        self.courses=[]

    def __repr__(self):
        return f"{self.first_name} {self.last_name} (ID:{self.student_id})"

    def enroll_in_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
            course.enroll(self)
    
    def unenroll_from_course(self,course):
        if course in self.courses:
            self.courses.remove(course)
            course.unenroll(self)
    
    def get_courses(self):
        return self.courses
