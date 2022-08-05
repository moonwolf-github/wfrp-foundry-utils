import sys
import json


def main(file_name):
    with open(file_name) as plik:
        for linia in plik.readlines():
            a = json.loads(linia)
            print(a["name"])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
