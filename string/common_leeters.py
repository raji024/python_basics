a = input()
b = input()
c = set()
d = set()
for char in a:
    c.add(char)
for be in b:
    if be in c:
        d.add(be)

print(d)

