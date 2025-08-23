a = int(input())
b = list(map(int,input().split()))
k =int(input())
for i in range(0,k):
    num = b[0]
    for j in range(0,len(b)-1):
        b[j] = b[j+1]
    b[len(b)-1] = num
print(b)
