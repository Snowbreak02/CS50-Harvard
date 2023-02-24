import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    iscorrectformat = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if iscorrectformat:
        pieces = iscorrectformat.groups()
        if int(pieces[1]) > 12 or int(pieces[5]) > 12:
            raise ValueError
        time_1 = formatting(pieces[1], pieces[2], pieces[3])
        time_2 = formatting(pieces[5], pieces[6], pieces[7])
        return time_1 + " to " + time_2
    else:
        raise ValueError

def formatting(hour, min, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if min == None:
        new_min = ":00"
        new_time = f"{new_hour}" + new_min
    else:
        new_time = f"{new_hour}" + ":" + min
    return new_time


if __name__ == "__main__":
    main()