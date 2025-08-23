a =int(input())
b = list(map(int,input().split()))
sum =0;
for i in range(len(b)):
    sum = sum +b[i]
print(sum)