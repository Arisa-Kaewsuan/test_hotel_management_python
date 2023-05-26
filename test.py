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
    keycard_number = 0
    for line in file.splitlines():
        list = line.splitlines()
        for i in list:  # String
            arr = i.split()  # list -line
            if arr[0] == "book":
                #print("add data")
                guest[i][0]
    return


file = readFile()
line = readLine(file)
command = getCommand(file)
guestList(file)
#print(command)

