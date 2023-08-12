# count the occurances of all characters

a = "abcdc"

l = len(a)

for i in a:
    c = 0
    for j in a:
        if(j==i):
            c += 1
    if(l!=0):
        print(i,":",c)
        l -= c
