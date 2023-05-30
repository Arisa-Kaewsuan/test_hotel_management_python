import connectDB as db


class list_available_room():
    sql = "SELECT room_number FROM Hotel WHERE status = %s"
    val = ["book"]
    obj = db.connectDB(sql)
    list = obj.select_db(val)
    room = []
    for x in list:
        room.append(''.join(x))

    room = ' '.join(str(e) for e in room)
    print(room)

# use this class
# obj = list_available_room()
