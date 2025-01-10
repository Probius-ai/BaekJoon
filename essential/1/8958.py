T = int(input())

for _ in range(T):
    streak = 0
    score = 0
    usr_input = input()
    for i in usr_input:
        if i == "O":
            streak+=1
            score += streak
        else:
            streak = 0

    print(score)
