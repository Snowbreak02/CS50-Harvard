class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid value")
        self.capactity = capacity
        self.size = 0


    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceed capacity")
        if self.size + n > self.capacity:
            raise ValueError("Exceed capacity")

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Too few cookies")
        self.size -= n
        
    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

jar = Jar()
