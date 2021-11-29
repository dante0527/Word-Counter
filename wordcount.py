import re
from functions import *

with open("beatles.txt", "r") as beatles:
    WordCount(beatles)

# resolve FileNotFoundError ??? to get code working
# then work on output