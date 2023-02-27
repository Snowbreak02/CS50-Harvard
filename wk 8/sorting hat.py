import random

class Hat:
    def __init__(self):
        self.houses = ["Landed", "HDB", "Condo", "apartment"]

    def sort(self, name):
        print(name, "is gna live in a", random.choice(self.houses))


hat = Hat()
hat.sort("Harry")