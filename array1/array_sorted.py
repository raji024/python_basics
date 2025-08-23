x =int(input())
b =list(map(int,input().split()))
is_sort = True
for i in range(len(b)-1):
    if b[i] > b[i+1]:
        is_sort = False
        break;
if is_sort:
    print("The array is sorted")
else:
    print("the array is not sorted")
