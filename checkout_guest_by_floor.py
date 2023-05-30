import connectDB as db


class checkout_guest_by_floor():
    def __init__(self, floor):
        self.floor = floor

    def checkout_guest(self):
        floor = self.floor
        sql = "SELECT room_number FROM Hotel WHERE status = %s AND floor = %s"
        val = ["book", floor]
        obj = db.connectDB(sql)
        tup = obj.select_db(val)
        list = []
        for x in tup:
            room = (str(x[0])).strip("b\'")
            
            # change status
            sql = "UPDATE Hotel SET status=%s WHERE room_number=%s"
            val = ("checkout", room)
            obj = db.connectDB(sql)
            obj.update_db(val)
            
            list.append(room)
        list = ','.join(list)
        print(f"Room {list} are checkout.")
        



# use this class
# obj = checkout_guest_by_floor("1")
# obj.checkout_guest()
