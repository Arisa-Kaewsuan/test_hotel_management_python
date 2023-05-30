import connectDB as db


class list_guest_by_floor():
    def __init__(self, floor):
        self.floor = floor

    def list_guest(self):
        floor = self.floor
        sql = "SELECT name_guest FROM Hotel WHERE floor = %s and status = %s"
        val = [floor,"book"]
        obj = db.connectDB(sql)
        tup = obj.select_db(val)
        list = []
        for x in tup:
            name = (str(x[0])).strip("b\'")
            list.append(name)
        # print(*list, sep=", ")


# use this class
obj = list_guest_by_floor("1")
obj.list_guest()
