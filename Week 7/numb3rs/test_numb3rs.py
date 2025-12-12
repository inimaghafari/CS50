from numb3rs import validate

def test_ip():
    assert validate("1.1.1.0") == True
    assert validate("0.137.51.70") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("3.345.456.567") == False
    assert validate("261.41.41.0") == False
    assert validate("sdf.fgh.hj.k") == False
    assert validate(".4.5.6") == False
