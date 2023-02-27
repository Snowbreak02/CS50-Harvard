import random

class Hat:
#dont need self as self is referring to a specific objects. There is only once copy of this variable and we want to use it throughout this entire class
    houses = ["Landed", "HDB", "Condo", "apartment"]

    @classmethod # only used if u only want there to be one of this function
    def sort(cls, name): # reference to the class but class wld conflict with class keyword
        print(name, "is gna live in a", random.choice(cls.houses))


# hat = Hat() dont need this due to class method
hat.sort("Harry")