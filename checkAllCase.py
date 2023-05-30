import createHotel as ch
import book as b
import list_available_room as ls
import checkout as cho
import list_guest as lg
import get_guest_in_room as gg
import list_guest_by_age as la
import list_guest_by_floor as lf
import checkout_guest_by_floor as chof
import book_by_floor as bf


class checkAllCase:
    def __init__(self, path):
        self.path = path
    # read file : string[file]

    def readFile(self):
        file = open(self.path, "r")
        file = file.read()
        return file  # String

    # read command : list[cmd]
    def command(self):
        cmd = []
        f = self.readFile()
        for line in f.splitlines():
            cmd.append(line.split())
        return cmd

    # check all case
    def checkCase(self):
        cmd = self.command()
        keycard = 0
        i = 0

        while i < len(cmd):
            # create_hotel
            if cmd[i][0] == "create_hotel":
                command = cmd[i][0]
                floor = int(cmd[i][1])
                room = int(cmd[i][2])

                obj = ch.createHotel(command, floor, room)
                obj.create_hotel()

            # booking room
            elif cmd[i][0] == "book":
                command = cmd[i][0]
                status = cmd[i][0]
                age = cmd[i][3]
                name = cmd[i][2]
                room = cmd[i][1]
                keycard += 1

                obj = b.book(command, status, age, name, room, keycard)
                obj.book_room()

            # list available room
            elif cmd[i][0] == "list_available_rooms":
                obj = ls.list_available_room()

            elif cmd[i][0] == "checkout":
                keycard_checkout = cmd[i][1]
                name_checkout = cmd[i][2]
                obj = cho.checkout(keycard_checkout, name_checkout)
                obj.room_checkout()

            elif cmd[i][0] == "list_guest":
                obj = lg.list_guest()

            elif cmd[i][0] == "get_guest_in_room":
                room = cmd[i][1]
                obj = gg.get_guest_in_room(room)
                obj.get_guest()

            elif cmd[i][0] == "list_guest_by_age":
                symbol = cmd[i][1]
                age = cmd[i][2]
                obj = la.list_guest_by_age(symbol,age)
                obj.list_guest()

            elif cmd[i][0] == "list_guest_by_floor":
                floor = cmd[i][1]
                obj = lf.list_guest_by_floor(floor)
                obj.list_guest()

            elif cmd[i][0] == "checkout_guest_by_floor":
                floor = cmd[i][1]
                obj = chof.checkout_guest_by_floor(floor)
                obj.checkout_guest()

            elif cmd[i][0] == "book_by_floor":
                floor = cmd[i][1]
                name = cmd[i][2]
                obj = bf.book_by_floor(floor, name)
                obj.checkout_guest()

            i += 1
        return


# path = 'input.txt'
# check = checkAllCase(path)
# check.checkCase()
# # print(check.readFile())
# print(check.command())
