import checkAllCase as ck

path = 'input.txt'
check = ck.checkAllCase(path)
cmd = check.command()
i = 0
keycard_number = 0
checkIn = {}

while i < len(cmd):
    keycard_number += 1
    name_guest = cmd[i][2]
    room_number = cmd[i][1]
    
    if len(checkIn) == 0:
        checkIn["room_book"]["name"] = name_guest

    # if room_number == checkIn[room_number]:
    #     print(f"Room {room_number} is booked by {name_guest} with keycard number {keycard_number}.")
    # else:
    #     print(f"Cannot book room {room_number} for {name_guest}, The room is currently booked by Thor.")
