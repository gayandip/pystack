# prime factors

a = int(input("Enter number: "))

def pfact(a):
    i = 2
    while(a!=1):
        
        if(a%i == 0):
            a = int(a/i)
            print(i,end=" ")
        else:
            i += 1

pfact(a)