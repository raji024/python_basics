a = int(input())
b = list(map(int,input().split()))
max = b[0]
for i in range(len(b)):
    if(b[i]>max):
        max = b[i]

print(max)
