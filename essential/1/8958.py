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

# ===========
# N=int(input())

# for _ in range(N):
#     streak = 0
#     score = 0
#     Questions = input()
#     for i in range(len(Questions)):
#         if Questions[i] =='O':
#             score += 1+streak
#             streak+=1
#         else:
#             streak = 0
#     print(score)