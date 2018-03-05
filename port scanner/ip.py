
#IP range maker (1)
def ipRange(first_ip, last_ip):
   start = list(map(int, first_ip.split(".")))  # return list of first ip as integer [0, 1, 2, 3]
   end = list(map(int, last_ip.split(".")))     # same for the last ip
   temp = start
   ip_range = []
   ip_range.append(first_ip)
   while temp != end:
      start[3] += 1
      for i in (3, 2, 1):
         if temp[i] == 256:
            temp[i] = 0
            temp[i-1] += 1
      ip_range.append(".".join(map(str, temp)))

   return ip_range

#scanning open ports on specific IP (2)
def scanports(IP):
    import socket
    IP = socket.gethostbyname(IP)
    print("-" * 60)
    print("Please wait, scanning open ports for ", IP)
    print("-" * 60)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for port in range(1,100):
            result = sock.connect_ex((IP, port))
            # print(str(port) + " ... " + str(result))
            if result == 0:
                print("Port %s: Open" % (port,))
        sock.close()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        quit()

    except socket.error:
        print("Couldn't connect to server")
        quit()


    print('Scanning Completed' + '\n')
    a=input("press any key to continue using script or 'q' to quit")
    if a == "q":
        quit()
    else:
        pass

#scannign specific port on IP's range (3)
def specificport(port):
    port = int(port)
    import socket
    file = "iprange.txt"
    f = open(file, "r")
    iplist = f.readlines()
    clearlist = []
    for x in iplist:
        clearlist.append(x.strip('\n'))
    print("-" * 60)
    print("Please wait, scanning range from " + file)
    print("-" * 60)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for ip in clearlist:
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(ip + ": Open")
    sock.close()

    print('Scanning Completed' + '\n')
    a=input("press any key to continue using script or 'q' to quit: ")
    if a == "q":
        quit()
    else:
        pass
    f.close()
#START MENU
choice = ""
while choice != "q":
    print("Welcome, please choose what do you wanna do: ('q' to quit)")
    print("1) Make full IP's list by ip range input")
    print("2) Scan open ports (1-100) for single ip:")
    print("3) Scan single open port on IP range (from iprange.txt)")
    choice=input("select menu by number: ")
    if choice == "1":
        ip_range = ipRange(input("enter first ip: "), input("enter last ip: "))
        file = "iprange.txt"
        f=open(file, "w")
        for ip in ip_range:
            f.write(ip + '\n')
        print("saved to " + file + '\n')
        f.close()
    elif choice == "2":
        scanports(input("enter ip to scan: "))
    elif choice == "3":
        specificport(input("choose port: "))
    elif choice == "q":
        print("quitting..")
    else:
        print("invalid key")
