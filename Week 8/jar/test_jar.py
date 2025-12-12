import pytest
from jar import Jar

def test_init():
    jar = Jar(capacity=10)
    assert jar.capacity == 10
    assert jar.size == 0


def test_str():
    jar = Jar(capacity=5)
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(capacity=3)
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(2)


def test_withdraw():
    jar = Jar(capacity=5)
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(5)
