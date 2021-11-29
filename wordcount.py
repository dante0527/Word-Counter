import re
from functions import *

with open("beatles.txt", "r") as beatles:
    WordCount(beatles)


#### need to reference noNewline from functions.py here
print(noNewline)
print(len(noNewline))

