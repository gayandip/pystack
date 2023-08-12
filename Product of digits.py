# take input and returns the product of digits of that number

a = int(input("Enter number: "))
def prod(a):
    b = 1
    while(a!=0):
        rem = a%10
        b = b*rem
        a = int(a/10)
    
    print(b)

prod(a)