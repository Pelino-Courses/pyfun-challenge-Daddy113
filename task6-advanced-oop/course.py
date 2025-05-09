class Course:
    def __init__(self,name,code):
        self.name=name
        self.code=code
        self.students=[]
        self.instructors=[]
        self.assistants=[]

    def __repr__(self):
        return f"{self.name} ({self.code})"
    
    def add_instructor(self,instructor):
        if instructor not in self.instructors:
            self.instructors.append(instructor)

    def remove_instructor(self,instructor):
        if instructor in self.instructors:
            self.instructors.remove(instructor)
    
    def add_assistant(self,assistant):
        if assistant not in self.assistants:
            self.assistants.append(assistant)

    def remove_assistant(self,assistant):
        if assistant in self.assistants:
            self.assistants.remove(assistant)

    def enroll(self,student):
        if student not in self.students:
            self.students.append(student)
    
    def unenroll(self,student):
        if student in self.students:
            self.students.remove(student)

    def get_students(self):
        return self.students
    
    def get_instructors(self):
        return self.instructors

    def get_assistants(self):
        return self.assistants
