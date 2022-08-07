import json
import sys
from utils import read_names


def main(file_name):
    skills = read_names("skills")
    talents = read_names("talents")
    careers = read_names("careers")
    with open(file_name) as plik:
        for linia in plik.readlines():
            a = json.loads(linia)
            for i in a["results"]:
                try:
                    translated_name = careers[i["text"]]
                except KeyError:
                    translated_name = i["text"]
                i["text"] = translated_name
            print(json.dumps(a))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
