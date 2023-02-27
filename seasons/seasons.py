import sys
import inflect
import re
from datetime import date


def main():
    p = inflect.engine()
    get_bday = input("Date of Birth: ")
    try:
        year, month, day = check_bday(get_bday)
    except:
        sys.exit("Invalid Date")

    DOB = date(int(year), int(month), int(day))
    tdy_date = date.today()
    d_diff = tdy_date - DOB
    t_diff = d_diff.days * 24 * 60
    formatted_diff = p.number_to_words((t_diff), andword = "")
    print (formatted_diff.capitalize() + "minutes")

def check_bday(get_bday):
    if re.search(r"[0-9]{4}-[0-9]{2}-[0-9]{2}$", get_bday):
        year, month, day = get_bday.split("-")
        return year, month, day


if __name__ == "__main__":
    main()