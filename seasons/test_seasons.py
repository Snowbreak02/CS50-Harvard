from seasons import check_bday

def main():
    test_format()


def test_format():
    assert check_bday("1998-02-11") == ("1998", "02", "11")
    assert check_bday("1998-02-1") == None
    assert check_bday("July 3, 1998") == None
    assert check_bday("1998 july 2") == None
    assert check_bday("July-3-1998") == None



if __name__ == "__main__":
    main()