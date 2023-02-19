from plates import is_valid

def main():
    test_Hposition()
    test_num()
    test_punctuation()

def test_length():
    assert value("Heys12") == "Valid"
    assert value("hey12") == "Invalid"
    assert value("Hello12") == "Invalid"
    assert value("i") == "Invalid"

def test_num():
    assert value("1234") == 100

def test_punctuation():
    assert value("%$&*!") == 100


if __name__ == "__main__":
    main()