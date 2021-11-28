import re

with open("beatles.txt", "r") as file:
    words = file.read()
    Replace = words.split()
    noPunc = list(map(lambda x: re.sub("[^\w\s]", "", x), Replace))
    noPunc2 = list(map(lambda x: re.sub(r"[\xa0]", "", x), noPunc))
    noNewline = list(map(lambda x: x.replace("\n", " "), noPunc2))

print(noNewline)
print(len(noNewline))
