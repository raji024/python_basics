a = input()
b =set()
for char in a:
    if char in b :
        print(char)
        break
    else:
        b.add(char)