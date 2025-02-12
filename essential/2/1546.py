def change_Score(score,M):
    for i in range(len(score)):
        score[i] = score[i]/M*100

def get_mean(score):
    mean = 0
    for i in score:
        mean += i
    return mean/len(score)

N = int(input())

score = list(map(int,input().split()))

M = max(score)

change_Score(score,M)
print(get_mean(score))