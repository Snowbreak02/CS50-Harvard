class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid value")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceed capacity")
        if self.size + n > self.capacity:
            raise ValueError("Exceed capacity")
        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Too few cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(6)
jar.withdraw(2)
print(jar.size)