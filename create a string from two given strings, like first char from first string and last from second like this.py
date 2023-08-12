# create a string from two given strings, like first char from first string and last from second like this

a = "bank"
b = "money"

p = ""
j = 0

for i in a:
    p += i
    if(len(b)*-1==j):
        continue
    else:
        j -= 1
        p += b[j]

j -= 1
while(len(b)*-1<=j):
    p += b[j]
    j -= 1

print(p)
