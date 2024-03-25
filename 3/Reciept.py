# 입력 받기
X= int(input())
N= int(input())
Total = 0

for _ in range(N):
    a, b = map(int, input().split())
    Total = Total + a*b

#금액 확인
if X==Total:
    print("Yes")
else :
    print("No")