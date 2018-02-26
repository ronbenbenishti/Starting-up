#read file, split by spacing, strip \n and replace shmoopie.5
f=open("text.txt","r")
f1=f.read()
f2=f1.split(" ")
ls=[]
z=0
for x in f2:
    try:
        if "the" in x:
            b=f2[z].strip("\n").replace("the","shmoopie")
            ls.append(b)
        else:
            ls.append(x)
        z+=1
    except:
        pass
str=""
for x in ls:
    str=str+" "+x
print(str)
