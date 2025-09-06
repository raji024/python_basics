class Laptop():
    charger_type ="C type"
    def __init__(self):
        self.brand=""
        self.price=34
    def setPrice(self,price):# exmaple of instnac emthods
        self.price = price
    def getprice(self): # exmaple of instance methods
        print(self.price)
    def setChargetType(cls):# this is exmaple of class methods
        cls.charger_type="b-type"

lenovo = Laptop()
lenovo.setPrice(40000)
lenovo.getprice()
# the above all are instance methods setpirce and getprice
Laptop.charger_type