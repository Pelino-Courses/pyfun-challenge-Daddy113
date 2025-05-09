class Enrollment:
    def __init__(self,student,course):
       
        from student import Student
        if not isinstance(student,Student):
            raise ValueError("It Must be an instance of Student")
        self.student=student
        self.course=course
