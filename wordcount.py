wordcount = []
#wordcount = {i:wordcount.count(i) for i in wordcount}
with open("beatles.txt","r") as file:
    words = file.read()
    Replace = words.replace(". ", " ")
    Replace2 = Replace.replace(", ", " ")
    Replace3 = Replace2.replace("\"", " ")
    Replace4 = Replace3.replace(", ", " ")
    Replace5 = Replace4.replace("\)", " ")
    Replace6 = Replace5.strip()
    Replace7 = Replace6.split(" ")
   
#test
#test(tr)
for x in (Replace7):
    Replace7.count(x)
    wordcount.append(Replace7.count(x))
    print(x,Replace7.count(x))
