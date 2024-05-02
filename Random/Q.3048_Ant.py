# 스택 대열 길이
N1, N2 = map(int, input().split())

#ant1 과 ant2로 개미 대열 입력받기
ant1 = list(input())
ant2 = list(input())

# 움직일 횟수
T = int(input())

# 대열에 개미 엮어 넣기
ants = ant1[::-1] + ant2

# T초 진행
for _ in range(T):
    # 개미가 만나 점프하는 경우
    i = 0
    while i < len(ants) - 1:
        if ants[i] in ant1 and ants[i+1] in ant2:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            i += 1
        i += 1

# 결과 출력
print(''.join(ants))