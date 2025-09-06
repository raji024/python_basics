class laptop:
    
    def __init__(self):
        self.price =0;
        self.ram=""
        self.processor=""
        print("demo")
        
    def display(self):
        print("Display")
hp = laptop()
hp.price=50000
hp.ram ="5 GB"
hp.processor='i5'



# the main purpose of constructor is to inialtize or assign values to data memebrs of class