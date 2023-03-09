def main():
    student = Student.get()
    #student.house = "Landed yo" -> use this to try break code, which is defended by the getter and setter function
    print(student)


class Student: #invents a new data type to be used later on
    def __init__(self, name, house):
        self.name = name
        self.house = house # _ is not in here as we still want it to go through the getter and setter functions to defend it from problems

    def __str__(self):
        return f"{self.name} lives in {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    @property #indicates to python this is a getter function
    def house(self):
        return self._house # _ is needed to seperate the variable name from the function name from line 8

    @house.setter #setter function, to use the input from user. must use the same name as getter
    def house(self, house):
        if house not in ["Landed", "HDB", "Condo", "apartment"]:
            raise ValueError("Invalid House")
        self._house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid Name")
        self._name = name
        

if __name__ == "__main__":
    main()