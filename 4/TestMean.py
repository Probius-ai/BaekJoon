N = int(input())

score = list(map(int,input().split()))
max = score[0]
for i in score:
    if max < i:
        max = i

for i in range(len(score)):
    score[i]= score[i]/max*100
sum = 0
for i in score:
    sum += i

sum = sum/len(score)
    
print(sum)