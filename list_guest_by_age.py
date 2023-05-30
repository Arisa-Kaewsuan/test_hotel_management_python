import connectDB as db


class list_guest_by_age():
    def __init__(self, symbol,age):
        self.symbol = symbol
        self.age = age

    def list_guest(self):
        symbol = self.symbol
        age= int(self.age)
        
        if symbol == '<':
            sql = "SELECT name_guest FROM Hotel WHERE age_guest < %s"
            val = [age]
            obj = db.connectDB(sql)
            tup = obj.select_db(val)
            list = []
            for x in tup:
                name = (str(x[0])).strip("b\'")
                list.append(name)
            print(*list, sep=", ")


# use this class
# obj = list_guest_by_age("<","18")
# obj.list_guest()
