class phone():
    def __init__(self,brand,price,chargetype):
        self.brand = brand # inside the constructor is instance vraiable
        self.price=price
        self.chargetype = chargetype
    def display(self):
        print("Brand:",self.brand)
        print("price:",self.price)
        print("chargeType:",self.chargetype)
samsung = phone("Samsung","10000","B-type")
samsung.display()