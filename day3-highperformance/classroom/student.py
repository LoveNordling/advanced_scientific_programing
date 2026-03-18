from .person import Person

class Student(Person):
    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)
        self.subject = subject


    def printNameSubject(self):
        print(self.firstname, self.lastname, self.subject)
