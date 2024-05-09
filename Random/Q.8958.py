N=int(input())

for _ in range(N):
    streak = 0
    score = 0
    Questions = input()
    for i in range(len(Questions)):
        if Questions[i] =='O':
            score += 1+streak
            streak+=1
        else:
            streak = 0
    print(score)