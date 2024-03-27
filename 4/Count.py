N = int(input())
listN = list(map(int,input().split()))
v = int(input())
count = 0
for i in range(len(listN)):
    if listN[i] == v:
        count += 1
print(count)
