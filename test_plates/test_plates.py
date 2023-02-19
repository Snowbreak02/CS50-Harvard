from plates import is_valid

def main():
    test_length()
    test_number_positions()
    test_punctuations()

def test_length():
    assert is_valid("Heys12") == True
    assert is_valid("Hellothere12") == False
    assert is_valid("H") == False
    assert is_valid("Hi12") == False

def test_number_positions():
    assert is_valid("12hey12") == False
    assert is_valid("he1y12") == False
    assert is_valid("h1ey12") == False

def test_punctuations():
    assert is_valid("hey!12") == False
    assert is_valid("hey 12") == False
    assert is_valid("&hey12") == False
    assert is_valid("hey12.") == False


if __name__ == "__main__":
    main()