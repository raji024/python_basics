a =input()
b=""
for i in range(len(a)):
    ch  = a[i]
    if ch=="a" or  ch=="e" or  ch=="i" or  ch=="o" or ch=="u":
        continue
    else:
        b+=ch
print(b)


