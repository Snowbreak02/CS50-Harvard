import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>)", s):
        url = re.search(r"(https?):\/\/(www\.)?youtube\.com\/embed\/(\w+)", s)
        if url:
            split_url = url.groups()
            return split_url

if __name__ == "__main__":
    main()