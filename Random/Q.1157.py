a = input()
a= a.upper()
b= set(a)
b= list(b)

c = []

for i in b:
    c.append(a.count(i))

ma = max(c)
count=0

for i in range(len(c)):
    if ma == c[i]:
        count+=1

if count != 1:
    print("?")
else:
    print(b[c.index(max(c))])