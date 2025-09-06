class grandpa():
    def phone(self):
        print("grandpa phone")
class dad(grandpa):
    def money(self):
        print("Dads money")
class son(dad):
    def laptop(self):
        print("sons money")
ram = son()
ram.laptop()
ram.money()
d1 = dad()
d1.phone()
