a = input()
f = {}
for char in a:
    if char in f:
        f[char]+=1
    else:
        f[char]=1
print(f)