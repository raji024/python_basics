class calculator:
    def __init__(self,a,b):
        self.num1 = a

        self.num2 = b
    def add(self):
        print(self.num1+self.num2)

obj1 = calculator(10,2)
obj1.add()

# without constructor
class calci:
    def add(self,a,b):
        print(a+b)
o = calci()
o.add(10,2)
