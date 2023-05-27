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
            name_current_guest = myresult.strip("b\'")
            print(name_current_guest)
                
            #print("checkout")
        i += 1
    return


path = "input.txt"
file = readFile(path)
cmd = command(file)
checkout(cmd)
