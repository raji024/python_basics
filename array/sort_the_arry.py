x = int(input())
arr = list(map(int,input().split()))
for i in range(0,x-1):
   for j in range(i+1,x):
      if(arr[i]> arr[j]):
         arr[i],arr[j] = arr[j],arr[i]
print(arr)