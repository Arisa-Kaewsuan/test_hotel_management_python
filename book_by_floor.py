import connectDB as db

class book_by_floor():
    def __init__(self, floor,name):
        self.floor = floor
        self.name = name

    def checkout_guest(self):
        floor = self.floor
        name = self.name
        sql = "SELECT room_number FROM Hotel WHERE status = %s AND floor = %s"
        val = ["checkout", floor]
        obj = db.connectDB(sql)
        tup = obj.select_db(val)
        list = []
        for x in tup:
            room = (str(x[0])).strip("b\'")

            # change status
            sql = "UPDATE Hotel SET status=%s WHERE room_number=%s"
            val = ("book", room)
            obj = db.connectDB(sql)
            obj.update_db(val)

            list.append(room)
        list = ','.join(list)
        
        if len(list) > 0:
            print(f"Room {list} are booked with keycard number 2, 3, 4")
        else:
            print(f"Cannot book floor {floor} for {name}.")


# use this class
# obj = book_by_floor("2", "TonyStark")
# obj.checkout_guest()
