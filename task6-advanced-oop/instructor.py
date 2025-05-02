# instructor.py
from person import Person
from typing import List

class Instructor(Person):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.courses: List['Course'] = []

    def assign_course(self, course: 'Course'):
        self.courses.append(course)

    def get_role(self) -> str:
        return "Instructor"
