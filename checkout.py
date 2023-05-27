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
                # get age
                sql = "SELECT age FROM `guest_list` WHERE keycard_number =(%s)"
                val = [(keycard_checkout)]
                mycursor.execute(sql, val)
                myresult = str(mycursor.fetchone()[0])
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
                sql = " DELETE FROM  guest_list WHERE keycard_number_number=(%s)"
                val = [(keycard_checkout)]
                mycursor.execute(sql, val)
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
