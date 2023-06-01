class keycard():
    def create_keycard(self,floor,room):
        keycard = []
        for i in range(0, floor*room):
            keycard.append(i*0)
        return keycard
    
    def keycard_stack(self,cmd,room_number,keycard): 
        i = 0
        if cmd == "book":
            while i < len(keycard):
                if keycard[i] == 0:
                    keycard[i] = room_number
                    return keycard
                i += 1
        elif cmd == "checkout": 
            while i < len(keycard):
                if keycard[i] == room_number:
                    keycard[i] = 0
                    return keycard
                i += 1
            return
        
        
# use this class
# obj = keycard()
# keycard = obj.create_keycard(2,3)
# print(keycard)

# # keycard_number = obj.keycard_stack("book", "203",keycard)
# keycard_1 = obj.keycard_stack("book", "203",keycard)
# # print(keycard_1)
# # print(keycard_5.index("203")+1)

# keycard_2 = obj.keycard_stack("book", "101", keycard_1)
# # print(keycard_2)
# # print(keycard_5.index("101")+1)

# keycard_3 = obj.keycard_stack("book", "102", keycard_2)
# # print(keycard_3)
# # print(keycard_5.index("102")+1)

# keycard_4 = obj.keycard_stack("book", "201", keycard_3)
# # print(keycard_4)
# # print(keycard_5.index("201")+1)

# keycard_5 = obj.keycard_stack("book", "202", keycard_4)
# # print(keycard_5)
# # print(keycard_5.index("202")+1)

# keycard_6 = obj.keycard_stack("checkout", "201", keycard_5)
# # print(keycard_6)

# keycard_7 = obj.keycard_stack("book", "103", keycard_6)
# print(keycard_7)
# print(keycard_7.index("103")+1)

