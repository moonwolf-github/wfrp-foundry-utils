import json
import sys


def main(file_name):
    profesje = {}
    with open("careers") as plik:
        for profesja in plik.readlines():
            try:
                profesje[profesja.split("=")[0]] = profesja.split("=")[1][:-1]
            except IndexError:
                profesje[profesja.split("=")[0][:-1]] = profesja.split("=")[0][:-1]
    with open(file_name) as plik:
        for linia in plik.readlines():
            a = json.loads(linia)
            a["name"] = profesje[a["name"]]
            print(a)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
