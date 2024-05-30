A,B = map(int,input().split())

temp_A= A
temp_B= B

a=1
b=1

for i in range(2, min(A,B)+1):
    while (A%i==0) and (B%i ==0):
        A= A//i
        B= B//i
        a=a*i
print(a)

A= temp_A
B= temp_B

for i in range(2, min(A,B)+1):
    while (A%i==0) and (B%i ==0):
        A= A//i
        B= B//i
        b=b*i

b*=A
b*=B

print(b)