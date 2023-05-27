# still have error!!!!
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
    count = 0
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
            
            # add condition : จะ book ได้ก่อต่อเมือ  room_number ไม่ซ้ำ คือก่อน insert ต้อง selectมาดูก่อนว่ามีค่านี้มั้ย
            sql = "SELECT room_number FROM `guest_list` WHERE room_number=(%s)"
            val = [(room_number)]
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            for x in myresult:
                count += 1
            if count > 0:

                # ดึง name_guest ที่ค่าตรงกับ room_number มาแสดง
                sql = "SELECT name_guest FROM `guest_list` WHERE room_number=(%s)"
                val = [(room_number)]
                mycursor.execute(sql, val)
                myresult = str(mycursor.fetchone()[0])
                name_current_guest = myresult.strip("b\'")
                print(
                    f"Cannot book room {room_number} for {name_guest}, The room is currently booked by {name_current_guest}.")
            else:
                # add data in DB
                sql = "INSERT INTO guest_list (keycard_number,room_number, name_guest,status,age) VALUES (%s,%s,%s,%s,%s)"
                val = [
                    (keycard_number, room_number, name_guest, status, age),
                ]
                mycursor.executemany(sql, val)
                mydb.commit()
                print(mycursor.rowcount, f"Room {room_number} is booked by {name_guest} with keycard number {keycard_number}.")
            
            
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

