class laptop:
    def __init__(self):
       self.ram=""
       self.processor=""
    def display(self):
        print("ram:",self.ram) # for denoting the current ram
        print("processor:",self.processor) # for denoting current processor
hp = laptop()
dell = laptop()
hp.ram="8 Gb"
hp.processor="i5"
dell.ram ="16 gb"
dell.processor ="i7"
hp.display()
dell.display()
