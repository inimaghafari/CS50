from twttr import shorten

def test_str():
    assert shorten("Hello") == "Hll"

def test_equal():
    assert shorten("Twitter") == "Twttr"

def test_word():
    assert shorten("AEIOUaeiou") == ""

def test_numbers():
    assert shorten("1234567890") == "1234567890"

def test_punctuation():
    assert shorten("?!.,") == "?!.,"

def test_mix():
    assert shorten("a2e4i?!") == "24?!"
