x = int(input())
arr = list(map(int,input().split()))
sum =0
for i in range(0,x):
    sum+= arr[i]
print(sum)