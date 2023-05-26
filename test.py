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

# input  : str file
# output : line list [0]
def guestList(file):
    command = []
    guest = []
    room_booked = set()
    keygard_number = 0
    j = 0
    for line in file.splitlines():
        list = line.splitlines() # list
        for i in list:  # i = String : "book 203 Thor 32", ...
            arr = i.split()  # list -line : [['book', '203', 'Thor', '32'], ...]
            if arr[0] == "book" :
                # print(arr[1])
                room_booked.add(arr[1])
        #         # print("add data")
        #         # keygard_number += 1
        #         # guest.append(arr)
        #         # guest[j].append(keygard_number)  # add keycard_number : [['book', '203', 'Thor', '32', 1], ...]
        #         # j += 1  
    print(room_booked)
    return guest


file = readFile()
line = readLine(file)
command = getCommand(file)
# print(command)
guest = guestList(file)
# print(guest)


