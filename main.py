# read file : string[file]
def readFile():
    file = open("input.txt", "r")
    return file.read()  # String

# read command : list[cmd]
def command(file):
    cmd = []
    for line in file.splitlines():
        cmd.append(line.split())
    return cmd

# check all case 
def checkCase(cmd):
    i = 0
    while i < len(cmd):
        # create_hotel
        if cmd[i][0] == "create_hotel":
           print("create_hotel")

        # booking room
        elif cmd[i][0] == "book":
            print("book")

        elif cmd[i][0] == "list_available_rooms":
            print("list_available_rooms")

        elif cmd[i][0] == "checkout":
            print("checkout")

        elif cmd[i][0] == "list_guest":
            print("list_guest")

        elif cmd[i][0] == "get_guest_in_room":
            print("get_guest_in_room")

        elif cmd[i][0] == "list_guest_by_age":
            print("list_guest_by_age ")

        elif cmd[i][0] == "list_guest_by_floor":
            print("list_guest_by_floor")

        elif cmd[i][0] == "checkout_guest_by_floor":
            print("checkout_guest_by_floor")

        elif cmd[i][0] == "book_by_floor":
            print("book_by_floor")
            
        else:
            break
        
        i += 1
    return
    

file = readFile()
cmd = command(file)
checkCase(cmd)


