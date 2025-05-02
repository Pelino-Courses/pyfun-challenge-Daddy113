# student.py
from person import Person
from typing import List, Iterator

class Student(Person):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self._enrollments: List['Enrollment'] = []

    def add_enrollment(self, enrollment: 'Enrollment'):
        self._enrollments.append(enrollment)

    def get_courses(self) -> Iterator['Course']:
        return (en.course for en in self._enrollments)

    def get_role(self) -> str:
        return "Student"

    def __add__(self, other: 'Student') -> List['Course']:
        if not isinstance(other, Student):
            raise TypeError("Can only add another Student")
        return list(set(self.get_courses()) | set(other.get_courses()))
