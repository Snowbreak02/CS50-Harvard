import sys
import inflect
import re
from datetime import date


def main():
    p = inflect.engine
    get_bday = input("Date of Birth: ")
    try:
        year, month, day = check_bday(get_bday)
    except:
        sys.exit("Invalid Date")


    get_day_diff = days_diff()
    min_diff = int(days_diffent) * 24 * 60
    formatted_diff = p.number_to_words(int(min_diff), andword = "")
    print (f"{formatted_diff}")

def check_bday(get_bday):
    if re.search(r"[0-9]{4}-[0-9]{2}-[0-9]{2}$", get_bday):
        year, month, day = get_bday.split("-")
        return year, month, day


def days_diff(get_bday):
    ...


if __name__ == "__main__":
    main()