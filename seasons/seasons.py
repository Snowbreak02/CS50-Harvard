import sys
import inflect
from datetime import date


def main():
    p = inflect.engine()
    get_bday = input("Date of Birth: ")
    get_day_diff = days_diff()
    min_diff = p.number_to_words(int(days_diffent) * 24 * 60)
    print f"{min_diff}"


...


if __name__ == "__main__":
    main()