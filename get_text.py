import sys
import json


def main(file_name, data_type):
    with open(file_name) as plik:
        for linia in plik.readlines():
            a = json.loads(linia)
            if data_type == "names":
                print(a["name"])
            if data_type == "descriptions":
                print(f'{a["name"]}={json.dumps(a["data"]["description"]["value"], ensure_ascii=False)[1:-1]}'.replace('\\"', '"'))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = "names"
        if len(sys.argv) == 3:
            data = sys.argv[2]
        main(sys.argv[1], data)
