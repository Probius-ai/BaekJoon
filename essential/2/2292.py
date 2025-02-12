def min_steps_to_n(N):
    if N == 1:
        return 1
    
    k = 1
    max_num_in_layer = 1
    while max_num_in_layer < N:
        max_num_in_layer = 1 + 3 * k * (k - 1)
        k += 1
    
    return k-1

# 테스트 코드
N = int(input())
print(f"{min_steps_to_n(N)}")