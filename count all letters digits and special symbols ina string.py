# count all letters digits and special symbols ina string

s = "Aab23@!~"

char = 0
spsym = 0
num = 0

for i in s:
    if((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)):
        char +=1
    elif(ord(i)>=48 and ord(i)<=57):
        num += 1
    elif(ord(i)<33):
        continue
    else:
        spsym +=1

print("Characters:",char)
print("Number:",num)
print("Special Symbols:",spsym)