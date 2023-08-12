# perfect numbers

def per():
    sum = 0
    for a in range(1,101):
        for i in range(1,a):
            if(a%i==0):
                sum += i
        if(sum == a):
            print(a,end=" ")
        sum = 0

per()