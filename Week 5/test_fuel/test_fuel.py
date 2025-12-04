from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("2/4") == 50

    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("-6/7")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
