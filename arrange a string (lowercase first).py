# arrange a string (lowercase first)
s = "BUSIness"
lwr = ""
upr = ""
for i in s:
    
    if(ord(i)>=97 and ord(i)<=122):
        lwr += i
    elif(ord(i)>=65 and ord(i)<=90):
        upr += i
        
p = lwr + upr
print(p)