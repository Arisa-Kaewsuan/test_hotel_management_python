import connectDB as db


class list_guest():
    sql = "SELECT name_guest FROM Hotel WHERE status = %s"
    val = ["book"]
    obj = db.connectDB(sql)
    tup = obj.select_db(val)
    list = []
    for x in tup:
        name = (str(x[0])).strip("b\'")
        list.append(name)
    # print(*list, sep=", ")

# use this class
# obj = list_guest()
