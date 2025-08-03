x = int(input())
arr = list(map(int,input().split()))
d ={}
for num in arr:
    if num in d:
        d[num]+=1
    else:
        d[num]=1
for key,value in d.items():
    print(key,":",value)
