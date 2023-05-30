import connectDB as db


class list_available_room():
    def list_room(self):
        sql = "SELECT room_number FROM Hotel WHERE status IS NULL OR status = %s"
        val = ["checkout"]
        obj = db.connectDB(sql)
        tup = obj.select_db(val)
        for x in tup:
            print(','.join([str(e) for e in x]))
        return

# use this class
# obj = list_available_room()
# obj.list_room()
