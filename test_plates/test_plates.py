from plates import is_valid

def main():
    test_length()
    test_number_positions()
    test_punctuations()

def test_length():
    assert is_valid("Heys12") == "Valid"
    assert is_valid("Hellothere12") == "Invalid"
    assert is_valid("H") == "Invalid"
    assert is_valid("Hi12") == "Invalid"

def test_number_positions():
    assert is_valid("12hey12") == "Invalid"
    assert is_valid("he1y12") == "Invalid"
    assert is_valid("h1ey12") == "Invalid"

def test_punctuations():
    assert is_valid("hey!12") == "Invalid"
    assert is_valid("hey 12") == "Invalid"
    assert is_valid("&hey12") == "Invalid"
    assert is_valid("hey12.") == "Invalid"


if __name__ == "__main__":
    main()