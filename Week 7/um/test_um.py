from um import count

def test_count_true():
    assert count("um") == 1
    assert count("hello um world um") == 2
    assert count("hello ,um ,teacher") == 1

def test_count_false():
    assert count("humy") == 0
    assert count("hum ok") == 0

def test_combine():
    assert count("album um is um good") == 2
    assert count("humm this um food is yummy") == 1

def test_case_insensitive():
    assert count("Um") == 1
    assert count("UM... hello um") == 2
    assert count("uM? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2

