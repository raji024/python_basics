class phone:
    char_ty ="C-TYpe" # this object is called class varible
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def disp(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("charger type:",self.char_ty)
samsung = phone("vivo","10000")
samsung.disp()
