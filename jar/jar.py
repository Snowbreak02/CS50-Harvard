def main():
    cookies = Jar.get()
    print(cookies)

class Jar:
    def __init__(self, capacity=12):
        self.capactity = capacity


    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...