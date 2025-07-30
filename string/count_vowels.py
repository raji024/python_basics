a = input()
x = len(a)
c =0
v=0
for i in range(0,x):
    ch = a[i]
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        v= v+1
    else:
        c= c+1
print(c)
print(v)
