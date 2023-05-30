import connectDB as db

class book():
    def __init__(self, command, status, age, name, room, keycard):
        self.command = command
        self.status = status
        self.age = age
        self.name = name
        self.room = room
        self.keycard = keycard
        
    def book_room(self):
        # create variable
        cmd = self.command
        status = self.status
        age = self.age
        name = self.name
        room = self.room
        keycard = self.keycard
        # print(cmd + status + age + name +room)
        
        # add data into database
        sql = "SELECT name_guest FROM Hotel WHERE room_number = %s"
        val = [room]
        obj = db.connectDB(sql)
        result = obj.select_db(val)
        result = ' '.join(str(e) for e in result)
        name_guest = result.strip("b(),\'")
        
        if (name_guest != "None" and name_guest != name):
            print(f"Cannot book room  {room} for  {name}, The room is currently booked by {name_guest}.")
        elif name_guest == name:
            print(f"Room {room} is booked by {name} with keycard number {keycard}.")
        elif name_guest == "None":
            sql = "UPDATE Hotel SET keycard_number=%s,name_guest=%s,age_guest=%s,status=%s WHERE room_number=%s"
            val = (keycard, name, age, status, room)
            obj = db.connectDB(sql)
            obj.update_db(val)
            print(f"Room {room} is booked by {name} with keycard number {keycard}.")
            
            


    
    
# use this class : book
# obj = book("book", "book", "32", "Thor", "203")
# obj.book_room()


