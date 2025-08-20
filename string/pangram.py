a = input()
b = set()
for char in a.lower():
    if char>='a' and char<='z':
        b.add(char)
if(len(b)== 26):
    print("it is pangram")
else:
    print("it is not pangram")