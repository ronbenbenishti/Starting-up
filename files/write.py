linetoadd = " "
f2 = open("slutfile.txt", "a")      # "a" means append / "w" means write
print("enter \"q\" to stop writing..")
while linetoadd is not "q":
        linetoadd = input("Enter line to write: ")
        if linetoadd != "q":
            f2.write(linetoadd + "\n")
        else:
            print("Quiting..")
f2.close()
