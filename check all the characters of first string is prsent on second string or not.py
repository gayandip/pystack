# check all the characters of first string is prsent on second string or not

a = "welcome"
b = "welcom"

flag = 0

for i in a:
    for j in b:
        if(j==i):
            flag = 1
            break
        flag = 0
    
    if(flag==0):
        break

if(flag==1):
    print("Present")
else:
    print("Not present")