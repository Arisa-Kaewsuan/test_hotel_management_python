def readFile(path):
    file = open(path, "r")
    file = file.read()
    return file


def command(file):
    cmd = []
    for line in file.splitlines():
        cmd.append(line.split())
    return cmd


def availableRoom(cmd):
    i = 0
    checkin_room = []
    all_room = []

    while i < len(cmd):
        if cmd[i][0] == "create_hotel":
            floor = int(cmd[i][1])
            room = int(cmd[i][2])
            for i in range(1, floor+1):
                for j in range(1, room+1):
                    all_room.append(i*100+j)
            #print(all_room)
            
        if cmd[i][0] == "book":
            room_number = int(cmd[i][1])
            if len(checkin_room) == 0:
                checkin_room.append(room_number)
                all_room.remove(room_number)
                #print(all_room)
                
            elif len(checkin_room) > 0:
                checkin_room.append(room_number)
                all_room.remove(room_number)
                #print(all_room)
                
            
        elif cmd[i][0] == "list_available_rooms":
            return all_room
        
        i += 1



path = "input.txt"
file = readFile(path)
cmd = command(file)
av_room = availableRoom(cmd) #list

f1 = ""
for i in av_room:
    f1 += str(i) + " "
print(f1)
