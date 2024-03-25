T = int(input())

for i in range(T):
    Number = input().split()
    Number[0],Number[1]=int(Number[0]),int(Number[1])
    print(Number[0]+Number[1])