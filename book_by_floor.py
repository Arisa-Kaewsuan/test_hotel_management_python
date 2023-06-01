import connectDB as db
import keycard as k

class book_by_floor():
    def __init__(self, floor,name,keycard_stack):
        self.floor = floor
        self.name = name
        self.keycard_stack = keycard_stack

    def checkout_guest(self):
        floor = self.floor
        name = self.name
        keycard = self.keycard_stack
        key_num = []
        
        sql = "SELECT room_number FROM Hotel WHERE status = %s AND floor = %s"
        val = ["checkout", floor]
        obj = db.connectDB(sql)
        tup = obj.select_db(val)
        list = []
        for x in tup:
            room = (str(x[0])).strip("b\'")
            list.append(room)
            
        if len(list) == 3:
            for x in tup:
                room = (str(x[0])).strip("b\'")
                
                # update keycard_stack
                obj = k.keycard()
                keycard = obj.keycard_stack("book", room, keycard)
                keycard_number = keycard.index(room)+1
                key_num.append(str(keycard_number))

                # change status
                sql = "UPDATE Hotel SET status=%s keycard_number=%s WHERE room_number=%s"
                val = ("book", keycard_number, room)
                obj = db.connectDB(sql)
                obj.update_db(val)
                    
            # print list by format 
            list = ','.join(list)
            key_num = ','.join(key_num)
            print(f"Room {list} are booked with keycard number {key_num}")
            return keycard
        
        else:
            obj = k.keycard()
            keycard = obj.keycard_stack("checkout", room, keycard)
            print(f"Cannot book floor {floor} for {name}.")
            return keycard

# test 1
# keycard_stack = ['203',0,0,0,0,0]
# obj = book_by_floor("1", "TonyStark", keycard_stack)
# obj.checkout_guest()

# test 2
# keycard_stack = ['203','101','102','103',0,0]
# obj = book_by_floor("2", "TonyStark",keycard_stack)
# obj.checkout_guest()
