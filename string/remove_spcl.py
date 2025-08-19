a =input()
b=""
for i in range(len(a)):
    ch = a[i]
    if ch>="a" and ch<="z":
        b+=ch
    elif ch>="A" and ch<="Z":
        b+=ch
    elif ch>="0" and ch<="9":
        b+=ch
print(b)

