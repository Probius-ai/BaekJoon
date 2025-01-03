def solution(mats, park):
    n = len(park)
    m = len(park[0])
    
    dp = [[0]*m for _ in range(n)]
    max_size = 0
    
    for i in range(n):
        for j in range(m):
            if park[i][j] != '-1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    if park[i][j] == park[i-1][j] == park[i][j-1] == park[i-1][j-1]:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    else:
                        dp[i][j] = 1
                max_size = max(max_size, dp[i][j])
    
    for mat in sorted(mats, reverse=True):
        if mat <= max_size:
            return mat
    
    return -1

"""
동적 프로그래밍(DP) 접근 방식
DP 테이블 정의:
공원의 각 위치에서 시작하여 돗자리를 깔 수 있는 최대 크기를 저장하는 2차원 DP 테이블을 만듭니다.
예를 들어, dp[i][j]는 (i, j) 위치에서 시작하는 가장 큰 정사각형 돗자리의 한 변 길이를 의미합니다.
초기화:
공원 배열에서 사람이 없는 곳(-1)을 기준으로 돗자리를 깔 수 있는지 확인합니다.
사람이 있는 곳은 dp 값이 0이 됩니다.
점화식:
만약 공원 배열의 (i, j) 위치에 사람이 없다면, 그 위치에서 가능한 최대 돗자리 크기는 주변의 값에 따라 결정됩니다.
dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
즉, 왼쪽, 위쪽, 왼쪽 위 대각선의 최소값에 1을 더한 값이 현재 위치에서 가능한 최대 돗자리 크기가 됩니다.
최대 크기 찾기:
DP 테이블을 모두 채운 후, 테이블에서 가장 큰 값을 찾고 그 값이 지민이가 가지고 있는 돗자리 크기 중 하나와 일치하는지 확인합니다.
시간 복잡도
시간 복잡도: 
O
(
n
×
m
)
O(n×m), 여기서 
n
n은 공원의 세로 길이, 
m
m은 가로 길이입니다.
공간 복잡도: 
O
(
n
×
m
)
O(n×m), DP 테이블을 저장하기 위한 공간입니다.
이 방식은 DFS보다 더 효율적으로 문제를 해결할 수 있으며, 특히 큰 입력에서도 중복 계산을 피할 수 있습니다.
"""