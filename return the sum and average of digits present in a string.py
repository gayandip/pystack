# return the sum and average of digits present in a string

a = "a12364b"

def sum_avg(a):
    t = 0
    sum = 0
    avg = 0
    for i in a:
        if(ord(i)>=48 and ord(i)<=57):
            sum += int(i)
            t += 1
    if(t!=0):
        avg = sum/t
    
    return sum,avg


sum,avg = sum_avg(a)
print("Sum:",sum)
print("Average",avg)
