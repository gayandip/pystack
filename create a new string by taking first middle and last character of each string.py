# create a new string by taking first middle and last character of each string

a = "board"
b = "money"

l1 = int(len(a)/2)
l2 = int(len(b)/2)

c = a[0] + b[0] + a[l1] + b[l2] + a[-1] + b[-1]
print(c)