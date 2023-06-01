import connectDB as db


class list_guest():
    def list(self):
        sql = "SELECT name_guest FROM Hotel WHERE status = %s"
        val = ["book"]
        obj = db.connectDB(sql)
        tup = obj.select_db(val)
        list = []
        for x in tup:
            name = (str(x[0])).strip("b\'")
            list.append(name)
        print(*list, sep=", ")
        return

# use this class
# obj = list_guest()
# obj.list()
