import connectDB as db
import keycard as k

class checkout():
    def __init__(self, keycard_checkout, name_checkout,keycard_stack):
        self.keycard_checkout = keycard_checkout
        self.name_checkout = name_checkout
        self.keycard_stack = keycard_stack
        
    def room_checkout(self):
        keycard_checkout = int(self.keycard_checkout)
        name_checkout = self.name_checkout
        keycard_stack = self.keycard_stack
        
        sql = "SELECT name_guest,keycard_number,room_number FROM Hotel WHERE keycard_number = %s"
        val = [keycard_checkout]
        obj = db.connectDB(sql)
        tup = obj.select_db(val)
        list = []
        for x in tup:
            name_checkin = (str(x[0])).strip("b\'")
            keycard_checkin = x[1]
            room_number = x[2]

        if keycard_checkin == keycard_checkout and name_checkin == name_checkout:
            print(f"Room {room_number} is checkout.")
            
            # change status
            sql = "UPDATE Hotel SET status=%s ,keycard_number=%s WHERE room_number=%s"
            val = ("checkout", 0,room_number)
            obj = db.connectDB(sql)
            obj.update_db(val)
            
            # update keycard
            obj = k.keycard()
            keycard = obj.keycard_stack("checkout", room_number, keycard_stack)
            return  keycard
            
        elif keycard_checkin != keycard_checkout or name_checkin != name_checkout:
            print(f"Only {name_checkin} can checkout with keycard number {keycard_checkin}.")
            # update keycard
            obj = k.keycard()
            keycard = keycard_stack
            return keycard
        

# use this class
# keycard_stack = []
# obj = checkout("4", "TonyStark",  keycard_stack)
# obj.room_checkout()