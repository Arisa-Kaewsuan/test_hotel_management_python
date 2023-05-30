import connectDB as db

class checkout():
    def __init__(self, keycard_checkout, name_checkout):
        self.keycard_checkout = keycard_checkout
        self.name_checkout = name_checkout
        
    def room_checkout(self):
        keycard_checkout = int(self.keycard_checkout)
        name_checkout = self.name_checkout
        sql = "SELECT name_guest,keycard_number,room_number FROM Hotel WHERE keycard_number = %s"
        val = [keycard_checkout]
        obj = db.connectDB(sql)
        tup = obj.select_db(val)
        list = []
        for x in tup:
            name_checkin = (str(x[0])).strip("b\'")
            keycard_checkin = x[1]
            room_number = x[2]

        if (keycard_checkin == keycard_checkout) and (name_checkout == name_checkin):
            print(f"Room {room_number} is checkout.")
            # change status
            sql = "UPDATE Hotel SET status=%s WHERE room_number=%s"
            val = ("chekout", room_number)
            obj = db.connectDB(sql)
            obj.update_db(val)
        else:
            print(f"Only {name_checkin} can checkout with keycard number {keycard_checkin}.")

# use this class
# obj = checkout("4", "TonyStark")
# obj.room_checkout()