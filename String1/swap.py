a = input()
b=""
for i in range(len(a)):
    ch = a[i]
    if ch>="a" and  ch<="z":
        ch = chr(ord(ch)-32)
        b+=ch
    elif ch>="A" and ch<="Z":
        ch =chr(ord(ch)+32)
        b+=ch
    else:
        b+=ch
print(b)
