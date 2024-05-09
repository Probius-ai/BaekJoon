a = list(map(int, input().split()))

for i in range(len(a)):
    a[i]=a[i]*a[i]

c=0

for i in a:
    c += i

print(c%10)