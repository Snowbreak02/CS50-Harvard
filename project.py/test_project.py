from project import get_player_names

def main():
    test_same_name()
    test_num()
    test_punctuation()

def test_Hposition(monkeypatch):
    inputs = iter(['Pavol', 'Kutaj'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = say_hello()
    assert result == "Hello Pavol Kutaj"

def test_num():
    assert value("1234") == 100

def test_punctuation():
    assert value("%$&*!") == 100


if __name__ == "__main__":
    main()