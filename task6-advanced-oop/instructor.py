class Instructor:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.courses=[]

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def assign_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_instructor(self)
    
    def remove_course(self,course):
        if course in self.courses:
            self.courses.remove(course)
            course.remove_instructor(self)

