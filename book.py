import connectDB as db
import keycard as k

class book():
    def __init__(self, command, status, age, name, room,keycard):
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
        name_in = self.name
        room_in = self.room
        keycard = self.keycard
        # print(cmd + status + age + name +room)
        
        # select data to check room_number--> status = book 
        sql = "SELECT status,room_number,name_guest FROM Hotel WHERE room_number = %s"
        val = [room_in]
        obj = db.connectDB(sql)
        tup = obj.select_db(val)
        for x in tup:
            status_db = x[0] # None
            room_db = x[1] # String
            name_db = x[2]
            
        if (name_in != name_db) and (name_db is not None):
            name_db = str(name_db).strip("b\'")
            print(f"Cannot book room  {room_in} for  {name_in}, The room is currently booked by {name_db}.")
        elif (name_db == name_in)and (room_db == room_in) :
            print(f"Room {room_in} is booked by {name_in} with keycard number keycard.")
        elif status_db is None:
            obj = k.keycard()
            keycard = obj.keycard_stack("book", room_in, keycard)
            keycard_number = keycard.index(room_in)+1
            sql = "UPDATE Hotel SET keycard_number=%s,name_guest=%s,age_guest=%s,status=%s WHERE room_number=%s"
            val = (keycard_number, name_in, age, status, room_in)
            obj = db.connectDB(sql)
            obj.update_db(val)
            print(f"Room {room_in} is booked by {name_in} with keycard number {keycard_number}.")
            
        return keycard
            
            


    
    
# use this class : book
# obj = book("book", "book", "32", "Thor", "203")
# obj = book("book", "book", "16", "PeterParker", "101")
# obj = book("book", "book", "36", "StephenStrange", "102")
# obj = book("book", "book", "48", "TonyStark", "201")
# obj = book("book", "book", "48", "TonyStark", "202")
# obj = book("book", "book", "48", "TonyStark", "203")
# obj.book_room()


