
class checkAllCase:
    def __init__(self,path):
        self.path = path
    # read file : string[file]

    def readFile(self):
        file = open(self.path, "r")
        file = file.read()
        return file # String

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
        i = 0
        while i < len(cmd):
            # create_hotel
            if cmd[i][0] == "create_hotel":
                print("create_hotel")

            # booking room
            elif cmd[i][0] == "book":
                print("book")

            elif cmd[i][0] == "list_available_rooms":
                print("list_available_rooms")

            elif cmd[i][0] == "checkout":
                print("checkout")

            elif cmd[i][0] == "list_guest":
                print("list_guest")

            elif cmd[i][0] == "get_guest_in_room":
                print("get_guest_in_room")

            elif cmd[i][0] == "list_guest_by_age":
                print("list_guest_by_age ")

            elif cmd[i][0] == "list_guest_by_floor":
                print("list_guest_by_floor")

            elif cmd[i][0] == "checkout_guest_by_floor":
                print("checkout_guest_by_floor")

            elif cmd[i][0] == "book_by_floor":
                print("book_by_floor")

            else:
                break

            i += 1
        return


# path = 'input.txt'
# check = checkAllCase(path)
# print(check.readFile())
# print(check.command())
