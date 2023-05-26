# input  : pathfile
# output : str file
def readFile():
    file = open("input.txt", "r")
    return file.read()  # String

# input  : str file
# output : line list
def readLine(file):
    arr = []
    for line in file.splitlines():
        list = line.splitlines()
        for i in list:  # String
            arr.append(i.split())
    return arr

# input  : str file
# output : line list [0]
def getCommand(file): 
    command = []
    for line in file.splitlines():
        list = line.splitlines()
        for i in list:  # String
            arr = i.split()  # list -line
            command.append(arr[0])
    return command

# input  : line list / i (cmd)
# output : print messege creat success
def createHotel(line,i):
    floor = line[i][1]
    room = line[i][2]
    return print(f"Hotel created with {floor} floor(s), {room} room(s) per floor.")
    
# input  : line list / i (cmd)
# output : print messege book success or not
def bookRoom(line,i):
    room_list = []
    room_input = room_list.append(line[i][1])
    print(room_input)
    book_name = line[i][2]
    keycard_number = 1
    
    j = 0
    while True:
        if room_input == line[i][j]:
            print("cannot book")
            break
        else:
            room_list.append(line[i][1])
            print("book succes")
            break
    return 
#print(f"Room {room_number} is booked by {book_name} with keycard number {keycard_number}.")

def list_available_rooms():
    return






def checkCase(command, line):
    i = 0
    while i < len(command):
        cmd = command[i] 

        # create_hotel
        if cmd == "create_hotel":
           createHotel(line,i)
        
        # booking room
        elif cmd == "book":
            bookRoom(line,i)
                
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
checkCase(command, line)

