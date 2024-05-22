N = int(input())

p1,p2= 1,1

sum=0
count = 1
while(p2<=N):

    if sum == N:
        count+=1
    if sum>=N:
        sum-=p1
        p1+=1
    if sum<N:
        sum+=p2
        p2+=1

print(count)