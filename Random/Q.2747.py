n = int(input())

pib = [0]*(n+1)
pib[0],pib[1]=0,1

for i in range(2,n+1):
    pib[i]= pib[i-1]+pib[i-2]

print(pib[n])