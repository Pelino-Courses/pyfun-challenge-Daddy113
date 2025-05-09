from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,first_name: str,last_name:str):
        self.first_name=first_name
        self.last_name=last_name

    @abstractmethod
    def get_role(self)->str:
        pass

    def __str__(self)->str:
        return f"{self.first_name} {self.last_name}"
