import sys
from utils import read_names

def main(file_name):
    profesje = {}
    skills = read_names("skills")
    talents = read_names("talents")
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
                                #print(", ".join(talents_translated))
                                tokens[1] = ", ".join(talents_translated)
                            except IndexError:
                                pass
                        linia = '"'.join(tokens)
                if "[" in linia:
                    names = True
                if "}" in linia:
                    collecting = False
            if "speciesSkills" in linia:
                collecting = True
                what = "skills"
            if "speciesTalents" in linia:
                collecting = True
                what = "talents"
            print(linia, end="")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])


"""        for linia in plik.readlines():
            for skill_en, skill_translated in skills.items():
                if skill_en in linia:
                    linia = linia.replace(skill_en, skill_translated)
            for talent_en, talent_translated in talents.items():
                if talent_en in linia:
                    linia = linia.replace(talent_en, talent_translated)
            print(linia, end="")"""