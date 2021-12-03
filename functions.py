import re


def makeArray(rawtextfile):
    with open(rawtextfile, "r") as file:
        words = file.read()
        Replace = words.split()
    return Replace


def noPunc(rawText):
    return list(map(lambda x: re.sub("[^\w]", "", x), rawText))


def noRogueChars(arrayofwords):
    return list(map(lambda x: re.sub(r"[\xa0]", "", x), arrayofwords))
