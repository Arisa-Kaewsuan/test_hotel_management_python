import checkAllCase as ck


class createHotel(ck.checkAllCase):
    def __init__(self,path):
        super().__init__(path)
        
    # def createHotel():
    #     floor = 2
    #     room = 3
    #     message = print(f"Hotel created with {floor} floor(s), {room} room(s) per floor.")
    #     return message


path = 'input.txt'
x = createHotel(path)
print(x.command())
