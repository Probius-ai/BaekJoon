year = int(input())

a=0

if (year%4==0)&(year%100!=0):
    a=1
elif year%400==0:
    a=1
    
print(a)