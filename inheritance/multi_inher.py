class dad():
    def phone(self):
        print("Dads phone")
class mom():
    def sweet(self):
        print("mom sweet are yummy")
class son(dad,mom):
    def laptop(self):
        print("son's laptop")
ram = son()
ram.phone()
ram.sweet()