import json
import sys


def main(file_name, translate_type):
    names = {}
    with open(translate_type) as plik:
        for name in plik.readlines():
            try:
                names[name.split("=")[0]] = name.split("=")[1][:-1]
            except IndexError:
                names[name.split("=")[0][:-1]] = name.split("=")[0][:-1]
    with open(file_name) as plik:
        for linia in plik.readlines():
            a = json.loads(linia)
            try:
                translated_name = names[a["name"]]
            except KeyError:
                translated_name = a["name"]
            a["name"] = translated_name
            print(json.dumps(a))


if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
