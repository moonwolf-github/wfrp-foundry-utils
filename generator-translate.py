import sys
from utils import read_names


def main(file_name):
    skills = read_names("skills")
    talents = read_names("talents")
    weapon_groups = read_names("weapon_groups")
    collecting = False
    names = False
    with open(file_name) as plik:
        for linia in plik.readlines():
            if collecting:
                if names:
                    if "]" in linia:
                        names = False
                    else:
                        tokens = linia.split('"')
                        if what == "skills":
                            tokens[1] = skills[tokens[1]]
                        else:
                            try:
                                talents_choose = tokens[1].split(",")
                                talents_translated = []
                                for i in talents_choose:
                                    talents_translated.append(talents[i.strip()])
                                # print(", ".join(talents_translated))
                                tokens[1] = ", ".join(talents_translated)
                            except IndexError:
                                pass
                        linia = '"'.join(tokens)
                if "[" in linia:
                    names = True
                if "}" in linia:
                    collecting = False
                elif what == "weapon_groups":
                    tokens = linia.split('"')
                    try:
                        tokens[3] = weapon_groups[tokens[3]]
                    except KeyError:
                        pass
                    linia = '"'.join(tokens)
            if "speciesSkills" in linia:
                collecting = True
                what = "skills"
            if "speciesTalents" in linia:
                collecting = True
                what = "talents"
            if "weaponGroupDescriptions" in linia:
                collecting = True
                what = "weapon_groups"
            print(linia, end="")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
