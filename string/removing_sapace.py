a = input()
x = len(a)
r=""
for i in range(0,x):
    ch = a[i]
    if(ch==' '):
        ch=''
        r+=ch

    else:
        r+=ch
print(r)
