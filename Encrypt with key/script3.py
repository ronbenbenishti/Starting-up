#This is simple script for encoding and decoding text by special key
key=input("Enter key: ")
k=""
for x in key:
    k=str(k)+str(ord(x))
key=int(k)
separate=chr(0)
def encode():
    file = open("hiden.txt","w")
    enlist=[]
    text=input("enter text to encrypt:\n")
    for x in text:
        x= ord(x)+key
        enlist.append(str(x))
    fulltext = ""
    for x in enlist:
        fulltext = fulltext + separate + x
    print(fulltext)
    file.write(fulltext)
    file.close()

def decode():
    choice=input("'r' - read from 'hiden.txt' file | 'm' - manual input: ")
    if choice == "r":
        file = open("hiden.txt","r")
        text = file.read()
        file.close()
        text = text.split(separate)
        text.remove("")
        delist = []
        for x in text:
            x = int(x)-key
            x = chr(x)
            delist.append(x)
        fulltext = ""
        for x in delist:
            fulltext = fulltext + x
        print(fulltext)
    elif choice == "m":
        text = input("enter crypted text:\n")
        text = text.split(separate)
        text.remove("")
        delist = []
        for x in text:
            x = int(x)-key
            x = chr(x)
            delist.append(x)
        fulltext = ""
        for x in delist:
            fulltext = fulltext + x
        print(fulltext)
    else:
        print("invalid key")

while True:
    start=input("'e' - encode | 'd' - decode | 'q' - quit: ")
    if start == "e":
        encode()
    elif start == "d":
        decode()
    elif start == "q":
        quit()
    else:
        print("invalid key")
