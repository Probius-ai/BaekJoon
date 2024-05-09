total = 1
for _ in range(3):
    total *= int(input())

total = str(total)

numList = list(range(1,10))

result = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    for j in range(len(total)):
        if str(i)== total[j]:
            result[i]+=1

for i in result:
    print(i)