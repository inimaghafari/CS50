class Jar:

    def __init__(self, capacity=12):

        if not isinstance(capacity, int):
            raise ValueError("Capacity must be an integer")
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")

        self._capacity = capacity
        self._cookies = 0
    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if self._cookies + n > self._capacity:
            raise ValueError("The number cookies are skip the limit")
        else:
            self._cookies += n

    def withdraw(self, n):
        if self._cookies < n:
            raise ValueError("Not enough cookies")
        else:
            self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
