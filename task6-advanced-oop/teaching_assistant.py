# teaching_assistant.py
from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
    def __init__(self, first_name: str, last_name: str):
        Student.__init__(self, first_name, last_name)
        Instructor.__init__(self, first_name, last_name)

    def get_role(self) -> str:
        return "Teaching Assistant"
