from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.4") == False
    assert validate(r"4") == False
    assert validate(r"cat") == False


def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.2.1.2") == False
    assert validate(r"1.512.3.4") == False
    assert validate(r"1.2.512.4") == False
    assert validate(r"1.2.3.512") == False
    
if __name__ == "__main__":
    main()