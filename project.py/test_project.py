from project import get_player_names
import pytest

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


def test_same_name(a,b,expected):
    assert demo.add(a,b) == expected
"""
def test_num():
    assert value("1234") == 100

def test_punctuation():
    assert value("%$&*!") == 100
"""

if __name__ == "__main__":
    main()