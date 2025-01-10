times = [0]*10
A = int(input())
B = int(input())
C = int(input())

number = A*B*C

for i in str(number):
    times[int(i)]+=1

for i in times:
    print(i)