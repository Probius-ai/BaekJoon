N,X=map(int,input().split())

a = input().split()

for i in range(N):
    if X > int(a[i]):
        print(a[i],end=' ')