a = input()
b = a.split()  # Splits input by space (correct usage)
x = ""         # Final result

for i in range(0, len(b)):
    c = b[i]     # Current word
    r = ""       # To build the modified word

    for j in range(0, len(c)):
        if j == 0:
            if c[0] >= 'a' and c[0] <= 'z':
                r += c[0].upper()  # Already lowercase, but retained for logic
            else:
                r += c[0]
        else:
            r += c[j]

    x += r + " "   # Add the word back with a space

print(x.strip())   # .strip() removes extra space at the end
