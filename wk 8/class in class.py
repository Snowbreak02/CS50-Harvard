class Wizard:
    def __init__(self):
        if not name:
            raise ValueError("Invalid name")
        self.name = name

    ...


class Student(Wizard): #tells py to inherit the Wizard class, which is the super class
    def __init__(self, name, house):
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        self.subject = subject

    ...