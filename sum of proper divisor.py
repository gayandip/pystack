# sum of proper divisor

a = int(input("Enter number: "))

def pdiv(a):
    sum = 0
    for i in range(1,a):
        if(a%i==0):
            sum += i
    
    print(sum)

pdiv(a)