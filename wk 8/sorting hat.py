import random

class Hat:
#dont need self as self is referring to a specific objects. There is only once copy of this variable and we want to use it throughout this entire class
    houses = ["Landed", "HDB", "Condo", "apartment"]

    @classmethod
    def sort(cls, name): # class wld conflict with class keyword
        print(name, "is gna live in a", random.choice(cls.houses))


hat = Hat()
hat.sort("Harry")