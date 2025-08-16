
a = input()
b = ""
for i in range(len(a)):
    ch = a[i]
    if ch == " ":       # If space
        b += "*"        # Add star instead
    else:
        b += ch         # Otherwise, keep character as is
print(b)

