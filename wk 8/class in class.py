class Wizard:
    def __init__(self):
        if not name:
            raise ValueError("Invalid name")
        self.name = name

    ...


class Student(Wizard): #tells py to inherit the Wizard class, bringing in the functions in there
    def __init__(self, name, house):
        super().__init__(name) #accessing the functions and using the functions in the inherited class, in this case Wizard
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...