a = input("Enter a string: ")
b = ""

for i in range(len(a)):
    ch = a[i]
    if "a" <= ch <= "z":  # already lowercase
        b += ch
    elif "A" <= ch <= "Z":  # uppercase → convert to lowercase
        b += chr(ord(ch) + 32)
    else:
        b += ch  # handle non-letters too (optional)

print(b)
