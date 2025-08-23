a = int(input())
b = list(map(int,input().split()))
k = int(input())
arr = []
for i in range(0,len(b)-1):
    for j in range(i+1,len(b)):
        if(b[i] + b[j] == k):
            arr.append((b[i],b[j]))
print(arr)
