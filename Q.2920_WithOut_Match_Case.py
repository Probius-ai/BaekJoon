N = list(map(int, input().split()))

if N[0] < N[1]:
        direction = 1
else:
        direction = -1

for i in range(len(N)-1):
    if N[i] < N[i+1] and direction == 1:
        direction = 1
    elif N[i] > N[i+1] and direction == -1:
        direction = -1
    else:
        direction = 0

if direction == 0: print("mixed")
elif direction == 1: print("ascending")
elif direction == -1: print("descending")