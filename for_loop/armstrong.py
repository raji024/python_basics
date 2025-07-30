import math
x= int(input())
temp =x
i =0
while(temp>0):
    digit = temp%10
    i= i+1
    temp = temp//10
b = x
s =0
while(b>0):
    d1 = b%10
    s = s+math.pow(d1,i)
    b = b//10
if(x == s):
    print("It is Armstrong")
else:
    print("it is not Armstrong")