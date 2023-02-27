import sys
import inflect
from datetime import date


def main():
    p = inflect.engine
    get_bday = bday()
    get_day_diff = days_diff()
    min_diff = int(days_diffent) * 24 * 60
    formatted_diff = p.number_to_words(int(min_diff), andword = "")
    print (f"{formatted_diff}")

def bday():
    


def days_diff(get_bday):
    ...


if __name__ == "__main__":
    main()