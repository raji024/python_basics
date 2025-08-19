a = input()
word = a.split()
r = ""

for i in range(len(word)):
    b = word[i]
    d = ""                        # move d outside inner loop
    for j in range(len(b)-1, -1, -1):
        ch = b[j]
        d += ch                   # build reversed word
    r += d
    if i != len(word) - 1:        # avoid extra space at the end
        r += " "

print(r)
