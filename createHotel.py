import connectDB as db
import keycard as k

class createHotel():
    def __init__(self, command, floor, room):
        self.command = command
        self.floor = floor
        self.room = room

    def create_hotel(self):
        # Declare variable
        cmd = self.command
        floor = self.floor
        room = self.room
        
        # create keycard and return
        obj = k.keycard()
        keycard = obj.create_keycard(floor, room)
        
        # Creat table name "Hotel"
        sql = "CREATE TABLE Hotel (keycard_number INT(200), room_number VARCHAR(20) UNIQUE, name_guest TEXT(30) , floor INT(30), age_guest INT(200), status VARCHAR(30))"
        obj = db.connectDB(sql)
        obj.create_db(floor, room)

        # Insert data : room number
        for i in range(1, floor+1):
            for j in range(1, room+1):
                room_number = i*100+j
                #print(room_number)
                sql = "INSERT INTO Hotel (room_number,floor) VALUES (%s,%s)"
                val = (room_number,i)
                obj = db.connectDB(sql)
                obj.insert_db(val)
        
        print(f"Hotel created with {floor} floor(s), {room} room(s) per floor.")
        return keycard


# use this class : createHotel
# obj = createHotel("create_hotel", 2, 3)
# print(obj.create_hotel())

