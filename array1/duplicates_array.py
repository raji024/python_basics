a = int(input())
b = list(map(int,input().split()))
c = set()
for i in range(len(b)):
    c.add(b[i])
print(c)
