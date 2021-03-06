import re


def WordCount(rawtextfile):
    with open(rawtextfile, "r") as file:
        words = file.read()
        Replace = words.split()
        noPunc = list(map(lambda x: re.sub("[^\w]", "", x), Replace))
        noPunc2 = list(map(lambda x: re.sub(r"[\xa0]", "", x), noPunc))
        noNewline = list(map(lambda x: x.replace("\n", " "), noPunc2))
    return noNewline
