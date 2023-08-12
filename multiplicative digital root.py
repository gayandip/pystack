# multiplicative digital root

a = int(input("Enter number: "))
def digroot(a):
    b = 1
    while(a!=0):
        rem = a%10
        b = b*rem
        a = int(a/10)

        if(a==0 and b>9):
            a = b
            b = 1
    print(b)

digroot(a)