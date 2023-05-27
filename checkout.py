def readFile(path):
    file = open(path, "r")
    file = file.read()
    return file


def command(file):
    cmd = []
    for line in file.splitlines():
        cmd.append(line.split())
    return cmd


def checkout(cmd):
    i = 0
    checkin = {}
    keycard_checkin = 0
    while i < len(cmd):
        if cmd[i][0] == "book":
            room_checkin = int(cmd[i][1])
            keycard_checkin += 1

            if len(checkin) == 0:
                checkin[keycard_checkin] = {}
                checkin[keycard_checkin]["room"] = room_checkin
                checkin[keycard_checkin]["keygard"] = keycard_checkin
            elif len(checkin) > 0:
                checkin[keycard_checkin] = {}
                checkin[keycard_checkin]["room"] = room_checkin
                checkin[keycard_checkin]["keygard"] = keycard_checkin
            print(checkin["keygard_checkin"]["keygard"])

                
        # if cmd[i][0] == "checkout":
        #     keycard_checkout = int(cmd[i][1])
        #     name_checkout = cmd[i][2]
        #     if checkin[203]["keygard_checkin"] == keycard_checkout:
        #         print("")
        i += 1
    return


path = "input.txt"
file = readFile(path)
cmd = command(file)
checkout(cmd)
