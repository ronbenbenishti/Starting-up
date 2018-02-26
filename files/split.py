f = open("file2.txt", "r")
list = f.readlines()              # print output: ['apples - 2\n', 'banananas - 3\n', 'potato - 5\n']
list1 = []
list2 = []
ls2 = []
for ls in list:
    ls1 = ls.strip("\n")
    ls2.append(ls1.split(" - "))         # split each line with marking saperating syntax " - "
for x in ls2:
    list1.append(x[0])
    list2.append(x[1])
print(list1)
print(list2)
f.close()
