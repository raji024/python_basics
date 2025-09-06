class teacher:
    def __init__(self,name,reg):
        self.name = name
        self.r = reg
    def display(self):
        print("the name is",self.name)
        print("the register number is",self.r)
t1 = teacher("raji","123")
t2 = teacher("raj","77")
t1.display()
t2.display()
