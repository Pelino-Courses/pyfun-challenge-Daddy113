# enrollment.py
from student import Student
from course import Course

class Enrollment:
    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course
