import mysql.connector

def readFile(path):
    file = open(path, "r")
    file = file.read()
    return file  


def command(file):
    cmd = []
    for line in file.splitlines():
        cmd.append(line.split())
    return cmd


def book(cmd):
    i = 0
    checkin_room = []
    keycard_number = 0
    
    while i < len(cmd):
        if cmd[i][0] == "book":
            # declare variable
            keycard_number += 1
            room_number = cmd[i][1]
            name_guest = cmd[i][2]
            status = cmd[i][0]
            age = cmd[i][3]
            
            # connect database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hotel_management_system"
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO guest_list (keycard_number,room_number, name_guest,status,age) VALUES (%s,%s,%s,%s,%s)"
            val = [
                ('1', room_number, name_guest, status, age),
            ]

            mycursor.executemany(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record was inserted.")
            break
            
            
            # #เก็บตัวแปร
            # room_number = cmd[i][1]
            # name_guest = cmd[i][2]
            # age_guest = cmd[i][3]
            # keycard_number += 1
            
            # if len(checkin_room) == 0:
            #     checkin_room.append(room_number)
            #     print(f"Room {room_number} is booked by {name_guest} with keycard number {keycard_number }.")
            # elif (len(checkin_room) > 0) and (room_number in checkin_room):
            #     print(f"Cannot book room {room_number} for {name_guest}, The room is currently booked by  Thor.")
            # elif len(checkin_room) > 0:
            #     checkin_room.append(room_number)
            #     print(f"Room {room_number} is booked by {name_guest} with keycard number {keycard_number }.")
        i += 1
    return 
        

path = "input.txt"
file = readFile(path)
cmd = command(file)
book(cmd)

