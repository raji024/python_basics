a =int(input())
temp =a
f =0
while(temp>0):
    digit = temp %10
    f = f * 10 + digit
    temp = temp//10
if(a == f):
    print("it is pali")
else:
    print("it is not pali")
