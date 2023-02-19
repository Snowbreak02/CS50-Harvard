from plates import is_valid

def main():
    test_Hposition()
    test_num()
    test_punctuation()

def test_Hposition():
    assert value("Hey") == 20
    assert value("cheers") == 100
    assert value("Hello") == 0
    assert value("hello") == 0

def test_num():
    assert value("1234") == 100

def test_punctuation():
    assert value("%$&*!") == 100


if __name__ == "__main__":
    main()