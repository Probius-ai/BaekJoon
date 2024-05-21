N,M = map(int,input().split())
A_list = list(map(int, input().split()))
S_list = []
C=[0]*M

temp =0
for i in A_list:
    temp+=i
    S_list.append(temp)

count = 0

for i in range(N):
    remainder = S_list[i] %M
    if remainder==0:
        count+=1
    C[remainder]+=1

for i in range(M):
    if C[i]>1:
        count+=(C[i]*(C[i]-1)//2)

print(count)