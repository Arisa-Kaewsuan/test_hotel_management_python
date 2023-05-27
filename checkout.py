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


def checkout(cmd):
    i = 0
    keycard_number = 0
    count = 0
    
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
                count += 1 # มีค่าซ้ำ
            if count > 0:
                # ดึง name_guest ที่ค่าตรงกับ room_number มาแสดง
                sql = "SELECT name_guest FROM `guest_list` WHERE room_number=(%s)"
                val = [(room_number)]
                mycursor.execute(sql, val)
                myresult = str(mycursor.fetchone())
                name_current_guest = myresult.strip("b(),\'")
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
                print(f"Room {room_number} is booked by {name_guest} with keycard number {keycard_number}.")
                
        if cmd[i][0] == "checkout":
            # declare variables
            keycard_checkout = cmd[i][1]
            name_checkout = cmd[i][2]
            
            # connect database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hotel_management_system"
            )
            mycursor = mydb.cursor()
            
            # get name_guest
            sql = "SELECT name_guest FROM `guest_list` WHERE keycard_number =(%s)"
            val = [(keycard_checkout)]
            mycursor.execute(sql, val)
            myresult = str(mycursor.fetchone())
            name_guest = myresult.strip("b\'(),")
            #print(name_guest)
            
            # เช็คว่า name_checkout == name_guest มั้ย ถ้าเท่าจะได้ checkout ได้
            if name_checkout == name_guest:
                # get room number เพื่อ add ข้อมูลลง ตาราง checkout
                sql = "SELECT room_number FROM `guest_list` WHERE keycard_number =(%s)"
                val = [(keycard_checkout)]
                mycursor.execute(sql, val)
                myresult = str(mycursor.fetchone())
                room_number = myresult.strip("b\'")
                # get age เพื่อ add ข้อมูลลง ตาราง checkout 
                sql = "SELECT age FROM `guest_list` WHERE keycard_number =(%s)"
                val = [(keycard_checkout)]
                mycursor.execute(sql, val)
                myresult = str(mycursor.fetchone())
                age = myresult.strip("b\'")
                #print(age)
                
                # add data in checkout table
                room_checkout = room_number
                status_checkout = "checkout"
                age_checkout = age
                sql = "INSERT INTO guest_checkout_list (keycard_number,room_number, name_guest,status,age) VALUES (%s,%s,%s,%s,%s)"
                val = [
                    (keycard_checkout, room_checkout, name_checkout, status_checkout, age_checkout),
                ]
                mycursor.executemany(sql, val)
                mydb.commit()
                #print("add data to checkout table success")
                
                # delete data from guest_list table
                sql = "DELETE FROM guest_list WHERE keycard_number = (%s)"
                val = [(keycard_checkout)]
                mycursor.executemany(sql, val)
                mydb.commit()
                print("delete data from guest_list success")
                
                # print(status)
                print(f"Room {room_number} is checkout.")
            else:
                print(f"Only {name_guest} can checkout with keycard number {keycard_checkout}.")

        i += 1
    return


path = "input.txt"
file = readFile(path)
cmd = command(file)
checkout(cmd)
