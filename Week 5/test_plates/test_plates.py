from plates import is_valid

def test_no_digit():
    assert is_valid("12345") == False
    assert is_valid("1sdf34") == False

def test_length():
    assert is_valid("s") == False
    assert is_valid("asdfghj") == False

def test_number_placement():
    assert is_valid("a123") == False
    assert is_valid("ga34th") == False
    assert is_valid("e5H48k") == False
    assert is_valid("1sdf34") == False

def test_zero_place():
    assert is_valid("as023") == False
    assert is_valid("asd01") == False
    assert is_valid("hh805") == True

def test_alphanumeric():
    assert is_valid("dfR123") == True
    assert is_valid("bn9032") == True
    assert is_valid("io") == True
    assert is_valid("DFf30") == True

def test_no_Symptoms():
    assert is_valid("ss12%") == False
    assert is_valid("s s12@") == False
    assert is_valid("ss,12 ") == False
