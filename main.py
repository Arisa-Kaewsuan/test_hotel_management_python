def readFile():
    file = open("input.txt", "r")
    return file.read()  # String


def readLine(file):
    arr = []
    for line in file.splitlines():
        list = line.splitlines()
        for i in list:  # String
            arr.append(i.split())
    return arr


def getCommand(file):
    command = []
    for line in file.splitlines():
        list = line.splitlines()
        for i in list:  # String
            arr = i.split()  # list -line
            command.append(arr[0])
    return command


def checkCase(command,line):
    # print(len(command))
    i = 0
    while i < len(command):
        cmd = command[i]
        
        if cmd == "create_hotel":
            print("Hotel created with " + line[i][i+1] + " floor(s), " + line[i][i+2] + " room(s) per floor.")
            return
           
        elif cmd == "book":
            print("book")
            return
            
        elif cmd == "list_available_rooms":
            print("list_available_rooms")
            return
           
        elif cmd == "checkout":
            print("checkout")
            return
            
        elif cmd == "list_guest":
            print("list_guest")
            return
        
        elif cmd == "get_guest_in_room":
            print("get_guest_in_room")
            return

        elif cmd == "list_guest_by_age":
            print("list_guest_by_age ")
            return
        
        elif cmd == "list_guest_by_floor":
            print("list_guest_by_floor")
            return
            
        elif cmd == "checkout_guest_by_floor":
            print("checkout_guest_by_floor")
            return
            
        elif cmd == "book_by_floor":
            print("book_by_floor")
            return
        
        i += 1
                    
                
                

file = readFile()
line = readLine(file)
command = getCommand(file)
checkCase(command,line)
