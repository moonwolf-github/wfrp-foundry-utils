import json
import sys


def main(file_name):
    skills = {}
    with open("skills") as plik:
        for skill in plik.readlines():
            try:
                skills[skill.split("=")[0]] = skill.split("=")[1][:-1]
            except IndexError:
                skills[skill.split("=")[0][:-1]] = skill.split("=")[0][:-1]
    with open(file_name) as plik:
        for linia in plik.readlines():
            a = json.loads(linia)
            try:
                translated_name = skills[a["name"]]
            except KeyError:
                translated_name = a["name"]
            a["name"] = translated_name
            print(json.dumps(a))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
