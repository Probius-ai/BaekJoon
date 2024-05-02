N1, N2 = map(int, input().split())
ant1,ant2 = input(),input()

ants = list(ant1[::-1] + ant2)

for _ in range(int(input())):
    i = 0
    while i < N1+N2 - 1:
        if ants[i] in ant1 and ants[i+1] in ant2:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            i += 1
        i += 1

print(''.join(ants))