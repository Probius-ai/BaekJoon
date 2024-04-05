T = int(input())
for i in range(T):
    times = 0
    S = input().split()
    times = S.pop(0)
    S = str(S[0])
    for j in range(len(S)):
        print(S[j]*int(times),end="")
    print("\n",end="")
