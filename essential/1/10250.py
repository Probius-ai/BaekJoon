T = int(input())

for _ in range(T):
    H,W,N=map(int,input().split())
    h,w=0,1
    for n in range(N):
        h+=1
        if h>H:
            h=1
            w+=1
    
    print("{}{:02d}".format(h,w))

# ======================
# for _ in range(int(input())):
#     H,W,N=map(int,input().split())
#     B = N%H
#     if B == 0:
#         B = H
#     A = (N-1)//H +1
    
#     print(f"{B}{A:02d}")