a = input()
word = a.split()
l = len(word[0])
for i in range(1,len(word)):
    c = word[i]
    if len(c) < l:
        l = len(c)
print(l)