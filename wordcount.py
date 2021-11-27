<<<<<<< HEAD
from os import closerange
=======
>>>>>>> 0fdbed38b382cfd07a3efd01711ce7c434abe64b
import re

wordcount = []
filters = [". ", ", ", "\(", "\)"]
# wordcount = {i:wordcount.count(i) for i in wordcount}
with open("beatles.txt", "r") as file:
    words = file.read()
    Replace0 = words.replace(".", ".")
    Replace = words.replace(". ", " ")
    Replace2 = Replace.replace(", ", " ")
    Replace3 = Replace2.replace('"', " ")
    Replace4 = Replace3.replace(", ", " ")
    Replace5 = Replace4.replace("\)", " ")
    Replace6 = Replace5.replace("\(", " ")
    Replace7 = Replace6.strip()
    Replace8 = Replace7.split(" ")

#test
#test(tr)

noPunc = list(map(lambda x: re.sub("[^\w\s]", '', x), Replace8))
noNewline = list(map(lambda x: x.replace('\n', ' '), noPunc))


print(noNewline)