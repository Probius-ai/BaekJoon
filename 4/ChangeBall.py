N,M = map(int,input().split())

basket = []

for f in range(1,N+1):
    basket.append(f)

for f in range(M):
    i,j = map(int, input().split())
    save = basket[j-1]
    basket[j-1] = basket[i-1]
    basket[i-1] = save

result = ' '.join(str(item) for item in basket)
print(result)