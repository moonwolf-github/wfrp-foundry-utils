def read_names(file_name):
    names = {}
    with open(file_name) as plik:
        for name in plik.readlines():
            try:
                names[name.split("=")[0]] = name.split("=")[1][:-1]
            except IndexError:
                names[name.split("=")[0][:-1]] = name.split("=")[0][:-1]
    return names
