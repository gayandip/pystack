# remove special symbols

a = "!@abqer"
b = ""
for i in a:
    if(ord(i)>32):

        if((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)):
            b += i
        elif(ord(i)>=48 and ord(i)<=57):
            b += i
    
    a = b

print(a)