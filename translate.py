import json
import os.path
import sys
from utils import read_names, read_descriptions


def main(file_name, translate_type):
    names = read_names(os.path.join("lang/pl", translate_type))
    desc = read_descriptions(f"lang/pl/{translate_type}_desc")
    with open(file_name) as plik:
        for linia in plik.readlines():
            a = json.loads(linia)
            try:
                translated_name = names[a["name"]]
            except KeyError:
                translated_name = a["name"]
            try:
                translated_desc = desc[a["name"]]
            except KeyError:
                translated_desc = a["data"]["description"]["value"]
            a["name"] = translated_name
            a["data"]["description"]["value"] = translated_desc
            print(json.dumps(a, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
