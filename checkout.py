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
            
            sql = "SELECT name_guest FROM `guest_list` WHERE keycard_number =(%s)"
            val = [(keycard_checkout)]
            mycursor.execute(sql, val)
            myresult = str(mycursor.fetchone()[0])
            name_guest = myresult.strip("b\'")
            #print(name_guest)
            if name_checkout == name_guest:
                # get room number
                sql = "SELECT room_number FROM `guest_list` WHERE keycard_number =(%s)"
                val = [(keycard_checkout)]
                mycursor.execute(sql, val)
                myresult = str(mycursor.fetchone()[0])
                room_number = myresult.strip("b\'")
                
                # change status from "book" to  checkout
                sql = "SELECT status FROM `guest_list` WHERE keycard_number =(%s)"
                val = [(keycard_checkout)]
                mycursor.execute(sql, val)
                myresult = str(mycursor.fetchone()[0])
                status = myresult.strip("\'")
                # print(status)
                print(f"Room {room_number} is checkout.")
            else:
                print(f"Only {name_guest} can checkout with keycard number {keycard_checkout}.")
                
            #print("checkout")
            #ต้องเพิ่ม case : เปลี่ยนสถานะจาก book เป็น checkout  ด้วย
        i += 1
    return


path = "input.txt"
file = readFile(path)
cmd = command(file)
checkout(cmd)
