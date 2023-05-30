import connectDB as db

class get_guest_in_room():
    def __init__(self,room_number):
        self.room_number = room_number
        
    def get_guest(self):
        room = self.room_number
        sql = "SELECT name_guest FROM Hotel WHERE room_number = %s"
        val = [room]
        obj = db.connectDB(sql)
        tup = obj.select_db(val)
        list = []
        for x in tup:
            name = (str(x[0])).strip("b\'")
            list.append(name)
        print(*list, sep=", ")


# use this class
# obj = get_guest_in_room("203")
# obj.get_guest()