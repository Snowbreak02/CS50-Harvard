from working import convert
import pytest

def main():
    test_format()
    test_time()
    test_min()


def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")