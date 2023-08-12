# amstrong number

a = int(input("Enter number: "))

def ams(a):
    b = a
    c = 0
    co = 0
    while(b!=0):
        b = int(b/10)
        co +=1
    
    b = a
    while(b!=0):
        rem = b%10
        c += rem**co
        b = int(b/10)
    
    if(c == a):
        print("Amstrong")
    else:
        print("Not an amstrong")

ams(a)