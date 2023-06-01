import connectDB as db
import keycard as k

class checkout_guest_by_floor():
    def __init__(self, floor,keycard_stack):
        self.floor = floor
        self.keycard_stack = keycard_stack

    def checkout_guest(self):
        floor = self.floor
        keycard_stack = self.keycard_stack
        
        sql = "SELECT room_number FROM Hotel WHERE status = %s AND floor = %s"
        val = ["book", floor]
        obj = db.connectDB(sql)
        tup = obj.select_db(val)
        list = []
        for x in tup:
            room = (str(x[0])).strip("b\'")
            
            # update keycard
            obj = k.keycard()
            keycard = obj.keycard_stack("checkout", room, keycard_stack)
            
            # change status
            sql = "UPDATE Hotel SET status=%s, keycard_number=%s WHERE room_number=%s"
            val = ("checkout",0, room)
            obj = db.connectDB(sql)
            obj.update_db(val)
            
            list.append(room)
        list = ','.join(list)
        

        print(f"Room {list} are checkout.")
        return keycard
    
        



# use this class
# obj = checkout_guest_by_floor("1")
# obj.checkout_guest()
