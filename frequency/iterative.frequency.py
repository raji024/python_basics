a = input()
d ={}
for char in a:
    if char in d:
        d[char]+=1
    else:
        d[char]=1
for char in d:
    print(char,":",d[char])