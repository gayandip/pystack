# append a new string in the middle of a given string

s = "st"
p = int(len(s)/2)
q = s[:p] + "igh" + s[p:]
print(q)