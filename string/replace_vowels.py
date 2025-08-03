a = input()
x = len(a)
b=""
for i in range(0,x):
    ch = a[i]
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch =='u'):
        ch='*'
        b+=ch
    else:
        b+=ch

print(b)
