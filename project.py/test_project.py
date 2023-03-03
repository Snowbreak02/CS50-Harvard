from project import get_player_names

def main():
    test_same_name()
    """
    test_num()
    test_punctuation()
"""
@pytest.mark.parametrize(
    'a,b,expected', [
        (Jeremy, Justin, "'Jeremy' and 'Justin' will be playing against each other!⚔️")
        (Jeremy, Thomas, "'Jeremy' and 'Thomas' will be playing against each other!⚔️")
    ]
)


def test_Hposition(monkeypatch):
    inputs = iter(['Pavol', 'Kutaj'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = get_player_names()
    assert result == "'Pavol' and 'Kutaj' will be playing against each other!⚔️"
"""
def test_num():
    assert value("1234") == 100

def test_punctuation():
    assert value("%$&*!") == 100
"""

if __name__ == "__main__":
    main()