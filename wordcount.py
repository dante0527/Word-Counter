import re
from functions import *

def main():
    beatles = noPunc(WordCount("beatles.txt"))
    print(beatles)
    
if __name__ == "__main__":
    main()