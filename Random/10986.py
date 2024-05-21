N,M = map(int,input().split())
A_list = list(map(int, input().split()))
S_list = []

while(len(A_list)>0):
    temp =0
    for i in range(len(A_list)):
        temp+=A_list[i]
        S_list.append(temp)
    del A_list[0]

print(S_list)

# 계산
count = 0

for i in S_list:
    if i%M==0:
        count+=1


print(count)