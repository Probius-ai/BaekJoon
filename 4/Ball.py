N,M = map(int,input().split())

basket = []

for f in range(N):
    basket.append(0)

for f in range(M):
    i,j,k = map(int, input().split())
    for f in range(i-1,j):
        basket[f]=k

result = str(basket[0])

for f in range(1,len(basket)):
    result = result + " " +str(basket[f])

print(result)