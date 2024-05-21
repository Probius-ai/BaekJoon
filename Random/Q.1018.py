N,M = map(int, input().split())

chess=[]
for _ in range(N):
    chess.append(input())

min_chan = float('inf')

for i in range(N-7):
    for j in range(M-7):
        Black = 0
        White = 0

        for a in range (i,i+8):
            for b in range(j,j+8):
                if(a+b)%2 ==0:
                    if chess [a][b] != 'B':
                        Black += 1
                    else:
                        White += 1
                else:
                    if chess[a][b] != 'W':
                        Black +=1
                    else:
                        White +=1

        min_chan = min(min_chan,Black,White)

print(min_chan)