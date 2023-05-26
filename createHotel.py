
def readFile(path):
    file = open(path, "r")
    file = file.read()
    return file  


def command(file):
    cmd = []
    for line in file.splitlines():
        cmd.append(line.split())
    return cmd


def createHotel(cmd):
    i = 0
    all_room = []
    while i < len(cmd):
        if cmd[i][0] == "create_hotel":
            floor = int(cmd[i][1])
            room = int(cmd[i][2])
            for i in range(1, floor+1):
                for j in range(1, room+1):
                    all_room.append(i*100+j)
            #print(all_room)
            print(f"Hotel created with {floor} floor(s), {room} room(s) per floor.")
            i += 1
            return
                
path = "input.txt" 
file = readFile(path) 
cmd = command(file) 
room = createHotel(cmd)


