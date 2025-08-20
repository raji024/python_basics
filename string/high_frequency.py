a = input()
f={}
for char in a:
    if char in f:
        f[char]+=1
    else:
        f[char]=1
k =0
d=""
for c in f.values():
    if(f.values()>k):
        k= f
        d = n.get(k)
print(k)