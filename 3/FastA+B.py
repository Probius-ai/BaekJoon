import sys

T = int(sys.stdin.readline())

for i in range(T):
    Number = sys.stdin.readline().split()
    Number[0],Number[1]=int(Number[0]),int(Number[1])
    print(Number[0]+Number[1])