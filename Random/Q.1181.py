N=int(input())

S_list =[0]*N

for i in range(N):
    S_list[i] = input()

for i in sorted(set(S_list), key=lambda x: (len(x), x)):
    print(i)