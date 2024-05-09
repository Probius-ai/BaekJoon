def calc(num):
    number = num
    while(num != 0):
      number+=(num%10)
      num=int(num/10)
    return number

a=[]
b=[]
for i in range(1,10001):
  a.append(i)
  b.append(calc(i))

c = [x for x in a if x not in b]

for i in c:
   print(i)