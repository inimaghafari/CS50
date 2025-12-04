from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value(" hElLo") == 0

def test_start_h():
    assert value("hey") == 20
    assert value("hola") == 20
    assert value(" hora") == 20

def test_no_h():
    assert value("good day") == 100
    assert value("  ok ") == 100
