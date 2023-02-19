from twttr import shorten

def main():
    test_upperNlower()
    test_num()
    test_punctuation()

def test_upperNlower():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwiTTeR") == "TwTTR"

def test_num():
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten("%$&*!") == "%$&*!"


if __name__ == "__main__":
    main()