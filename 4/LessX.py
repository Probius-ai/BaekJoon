N = list(map(int, input().split()))
listN = list(map(int,input().split()))
result = []

for i in range(len(listN)):
    if listN[i] < N[1]:
        result.append(listN[i])
resultlist = str(result[0])
for i in range(1,len(result)):
    resultlist = resultlist + " " + str(result[i])
print(resultlist)