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
            try:
                translated_name = profesje[a["name"]]
            except KeyError:
                translated_name = a["name"]
            try:
                translated_group = profesje[a["data"]["careergroup"]["value"]]
            except KeyError:
                translated_group = a["data"]["careergroup"]["value"]
            a["name"] = translated_name
            a["data"]["careergroup"]["value"] = translated_group
            desc = a["data"]["description"]["value"].split("{")
            link = desc[1].split("}")
            link[0] = translated_group
            desc[1] = "}".join(link)
            a["data"]["description"]["value"] = "{".join(desc)
            print(json.dumps(a))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
