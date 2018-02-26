f = open("file.txt", "r")   # "r" means read-only

var1 = f.readlines()        # print output: ['First line\n', 'second line\n', 'third line\n']
for x in var1:              # for loop in 'var1[ ]'
    print(x)                # print each item (line)
f.close()
