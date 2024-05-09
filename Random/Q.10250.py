for _ in range(int(input())):
    H,W,N=map(int,input().split())
    B = N%H
    if B == 0:
        B = H
    A = (N-1)//H +1
    
    print(f"{B}{A:02d}")