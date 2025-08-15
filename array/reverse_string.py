a = input()
x = len(a)
b=""
for i in range(x-1,-1,-1):
    ch = a[i]
    b+=ch
print(b)