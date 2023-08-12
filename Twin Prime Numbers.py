# twin primes
def twin():
    a = 2
    b = a
    for n in range(1,1000):
        
        for i in range(2,n):
            if(n%i==0):
                break
            elif(i==n-1):
                a = n
                break
        if(b+2 == a):
            print(b,a)
        b = a


twin()
        
