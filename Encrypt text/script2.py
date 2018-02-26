off=1
while off != 0:
    ans=input("'en' - encode | 'de' - decode | 'q' - quit: ")
    if ans == "en":
        enfile=open("encode.txt", "w")
        str=input("enter text:\n")
        temp=0
        result=""
        a= len(str)
        for x in range(0,a):
            temp= ord(str[x]) +1
            result=result+chr(temp)
        print(result)
        enfile.write(result)
        enfile.close()
    elif ans == "de":
        print("reading from 'encode.txt'...")
        enfile=open("encode.txt", "r")
        defile=open("decode.txt", "w")
        temp1=0
        result1=""
        str1=enfile.read()
        enfile.close()
        a= len(str1)
        for x in range(0,a):
            temp1= ord(str1[x]) -1
            result1=result1+chr(temp1)
        print(result1)
        defile.write(result1)
        defile.close()
    elif ans == "q":
        print("Quiting..")
        off = 0
    else:
        print("invalid key")




