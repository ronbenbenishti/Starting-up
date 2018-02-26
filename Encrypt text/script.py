str="yossi loves bacon"
a=0
x=""
ls=[]
textlen=len(str)
while a != int(textlen):
    try:
        x = str[a]
        if "s" in x:
            b= chr(ord(str[a]) +3)
            ls.append(b)
        else:
            ls.append(x)
        a+=1
    except:
        pass

string=""
for x in ls:
    string=string+x
print(string)
