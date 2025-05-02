# course.py
from typing import List

class Course:
    def __init__(self, name: str, code: str):
        self.name = name
        self.code = code
        self._enrollments: List['Enrollment'] = []  # Forward reference to Enrollment

    def enroll(self, student: 'Student'):  # Forward reference to Student
        # Delayed import to avoid circular import error
        from student import Student
        from enrollment import Enrollment  # Importing Enrollment here to avoid circular import
        
        if not isinstance(student, Student):
            raise TypeError("Only Student instances can be enrolled")
        enrollment = Enrollment(student, self)
        self._enrollments.append(enrollment)
        student.add_enrollment(enrollment)

    def get_students(self):
        return (en.student for en in self._enrollments)

    def __str__(self):
        return f"{self.code}: {self.name}"
