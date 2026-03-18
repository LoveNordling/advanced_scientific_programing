class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_names(self):
        return self.firstname, self.lastname
    
