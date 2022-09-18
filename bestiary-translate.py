import json
import sys
from utils import read_names


def main(file_name):
    names = read_names("lang/pl/bestiary_names")
    with open(file_name) as plik:
        for linia in plik.readlines():
            a = json.loads(linia)
            try:
                translated_name = names[a["name"]]
            except KeyError:
                translated_name = a["name"]
            a["name"] = translated_name
            a["token"]["name"] = translated_name
            print(json.dumps(a))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
