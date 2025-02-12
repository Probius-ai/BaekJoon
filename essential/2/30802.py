N = int(input())

size=list(map(int, input().split()))
T,P= map(int,input().split())
times = 0
# 티셔츠 주문 묶음 세기
for i in size:
    if i == 0: #티셔츠 해당 사이즈 갯수 0일떄
        continue
    else:
        if i%T == 0: # 티셔츠 해당 갯수가 알맞게 나눠질때
            times += i//T
        else:
            times += i//T + 1

# 출력
print(times)
print("{} {}".format(N//P, N%P)) 