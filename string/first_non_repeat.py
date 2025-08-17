a =input()
b=""
seen = set()
for char in a:
    if char not in seen:
        print(char)
        break