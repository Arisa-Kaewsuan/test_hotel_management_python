def readFile():
    file = open("input.txt", "r")
    return file.read()  # String


def getCommand(file):
    command = []
    for line in file.splitlines():
        list = line.splitlines()
        for i in list:  # String
            arr = i.split()  # list -line
            command.append(arr[0])
    return command


def checkCase(command):
    cmd = []
    for i in command:
        cmd.append(i)  # String -list
        match cmd[i]:
            case "create_hotel":
                print("create hotel")
            

       
        


file = readFile()
command = getCommand(file)
checkCase(command)
