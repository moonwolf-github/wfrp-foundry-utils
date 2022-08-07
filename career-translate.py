import json
import sys
from utils import read_names


def translate(what, where):
    translated_names = []
    for name in where:
        try:
            translated_name = what[name]
        except KeyError:
            translated_name = name
        translated_names.append(translated_name)
    return translated_names


def main(file_name):
    profesje = read_names("careers")
    skills = read_names("skills")
    talents = read_names("talents")
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

            a["data"]["skills"] = translate(skills, a["data"]["skills"])
            a["data"]["talents"] = translate(talents, a["data"]["talents"])
            print(json.dumps(a))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
