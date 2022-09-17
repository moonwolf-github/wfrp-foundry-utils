import json
import sys
from utils import read_names


# not sure if this is neccessary, maybe tables.db is enough
def main(file_name):
    skills = read_names("lang/pl/skills")
    talents = read_names("lang/pl/talents")
    careers = read_names("lang/pl/careers")
    species = ["human-reiklander", "dwarf", "halfling", "welf", "helf", "human"]
    with open(file_name) as plik:
        a = json.loads(plik.read())
        for i in a["rows"]:
            for j in species:
                try:
                    translated_name = careers[i[j]["name"]]
                except KeyError:
                    translated_name = i[j]["name"]
                i[j]["name"] = translated_name
        print(json.dumps(a, indent=4))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
