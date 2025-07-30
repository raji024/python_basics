a = int(input())
temp =a
f =0
while(temp>0):
    digit = temp %10
    f = f * 10 + digit
    temp = temp //10
print(f)
