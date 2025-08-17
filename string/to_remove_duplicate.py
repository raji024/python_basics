a =input()
b=""
seen = set()
for char in a:
    if char not in seen:
        b+=char
        seen.add(char)

print(b)
