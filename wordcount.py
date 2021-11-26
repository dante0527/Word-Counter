wordcount = []
#wordcount = {i:wordcount.count(i) for i in wordcount}
with open("beatles.txt","r") as file:
    words = file.read()
    Replace = words.replace(". ", " ")
    Replace2 = Replace.replace(", ", " ")
    Replace3 = Replace2.replace("\"", " ")
    Replace4 = Replace3.replace(", ", " ")
    Replace5 = Replace4.replace("\)", " ")
    Replace7 = Replace6.strip()
    Replace8 = Replace7.split(" ")
   
#test
#test(tr)
for x in (Replace8):
    Replace8.count(x)
    wordcount.append(Replace8.count(x))
    print(x,Replace8.count(x))
