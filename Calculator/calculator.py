f=open("calclog.txt", "w")
start=""
while start != "q":
    start=input("Press 's' to start calculate or 'q' to quit and save log file: ")
    if start == "s":
        num1=int(input("1st number: "))
        op=input("select operator (+ - * / ^ %): ")
        num2=int(input("2nd number: "))
        if op == "+":
            resualt=str(num1+num2)
            fprint=str(num1) + str(op) + str(num2) + "=" + resualt + "\n"
            print(fprint)
            f.write(fprint)
        if op == "-":
            resualt=str(num1-num2)
            fprint=str(num1) + str(op) + str(num2) + "=" + resualt + "\n"
            print(fprint)
            f.write(fprint)
        if op == "*":
            resualt=str(num1*num2)
            fprint=str(num1) + str(op) + str(num2) + "=" + resualt + "\n"
            print(fprint)
            f.write(fprint)
        if op == "/":
            resualt=str(num1/num2)
            fprint=str(num1) + str(op) + str(num2) + "=" + resualt + "\n"
            print(fprint)
            f.write(fprint)
        if op == "^":
            resualt=str(num1**num2)
            fprint=str(num1) + str(op) + str(num2) + "=" + resualt + "\n"
            print(fprint)
            f.write(fprint)
        if op == "%":
            resualt=str(num1%num2)
            fprint=str(num1) + str(op) + str(num2) + "=" + resualt + "\n"
            print(fprint)
            f.write(fprint)
    elif start == "q":
        print("Quiting..")
    else:
        print("invalid key, try again.")

f.close()
