a = int(input())
i=0
temp =a
while(temp>0):
    digit = temp%10
    i = i+1
    temp = temp//10
print(i)