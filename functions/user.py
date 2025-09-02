def n():
    name = input()
    print("hello",name)
n()

def n():
    name = input()
    return "hello",name
msg = n()
print(msg)

def m(name):
    print(name)

user_name = input("Enter your name: ")
m(user_name)
