class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid value")
        self._capactity = capacity
        self._size = 0


    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self._capacity:
            raise ValueError("Exceed capacity")
        if self._size + n > self._capacity:
            raise ValueError("Exceed capacity")

    def withdraw(self, n):
        if self._size < n:
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
