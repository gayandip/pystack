# amicable numbers

def ami():
    for a in range(1,1001):
        sum = sdiv(a)
        sum2 = sdiv(sum)
        if(a == sum2 and sum!= a):
             print(a,sum)

def sdiv(a):
    sum = 0
    for i in range(1,a):
            if(a%i==0):
                sum += i
    return sum           

ami()