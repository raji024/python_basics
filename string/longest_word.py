a = input()
word = a.split()
c =word[0]
l = len(word[0])
for i in range(1,len(word)):
    b = word[i]
    if len(b)>l:
        l = len(b)
        c = b
print(l)
print(c)

