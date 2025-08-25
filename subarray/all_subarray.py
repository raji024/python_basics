n = int(input())
b =[]
for i in range(n):
    r= int(input())
    b.append(r)
for i in range(0,n):
    for j in range(i,n):
        print(b[i:j+1])