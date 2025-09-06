#if i create a method inside the class use self for that methods
class goa:
    name="klmno" # i created empty name for both of these first if i simply print the name of hira without assignng variable to it simply print teh default nmae in it
    drink=""
    def party(self):
        print("Lets party.....")
    def  beach(self):
        print("Enjoying the beach")
raji = goa() # raji get the ticket to go to goa so it have access to full goa
hira = goa()
raji.name="raji"
hira.name ="hira"
raji.drink ="yes"
hira.drink ="no"
print(hira.name)
print("Drink:",hira.drink)
print(raji.name)#first register the name and the they go whether they going party or beach
print("Drink:",raji.drink)
raji.party()
hira.beach()
