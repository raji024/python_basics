a = input()
x = len(a)
b=""
for i in range(x-1,-1,-1):
    ch = a[i];
    b = b+ch
print(b)
if(a == b):
    print("pali")
else:
    print("Not pali")


