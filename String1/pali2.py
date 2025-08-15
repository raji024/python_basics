a =input()
b="";
for i in range(len(a)-1,-1,-1):
    ch = a[i]
    b+=ch;
if a==b:
    print("it is pali")
else:
    print("it is not pali")