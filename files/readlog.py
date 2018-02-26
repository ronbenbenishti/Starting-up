log = open("file2.txt", 'r')
logl = log.readlines()
list1 = []
list2 = []
list3 = []
for x in logl:
    list1.append(x.split(" - - "))

for y in list1:
    list2.append(y[0])
    list3.append(y[1])

print(list2)
print(list3)
