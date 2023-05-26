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
    keycard_number = 0
    all_room = []

    while i < len(cmd):
        if cmd[i][0] == "list_available_rooms":
            floor = int(cmd[i][1])
            room = int(cmd[i][2])
            for i in range(1, floor+1):
                for j in range(1, room+1):
                    all_room.append(i*100+j)
            print(all_room)

        elif cmd[i][0] == "book":
            # เก็บตัวแปร
            room_number = cmd[i][1]
            name_guest = cmd[i][2]
            age_guest = cmd[i][3]
            keycard_number += 1

            if len(checkin_room) == 0:
                checkin_room.append(room_number)
                #print(f"Room {room_number} is booked by {name_guest} with keycard number {keycard_number }.")
            elif len(checkin_room) > 0:
                checkin_room.append(room_number)
                #print(f"Room {room_number} is booked by {name_guest} with keycard number {keycard_number }.")
        i += 1
    return


path = "input.txt"
file = readFile(path)
cmd = command(file)
availableRoom(cmd)
