N = int(input())
N_list = list(map(int,input().split()))

count = N

for i in range(N):
    if N_list[i]== 1:
        count-=1
        continue
    for j in range(2,N_list[i]):
        if N_list[i] % j == 0:
            count -=1
            break

print(count)