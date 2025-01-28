melody = list(map(int,input().split()))

buffer = melody.pop(0)
streak = 0

for i in melody:
    if buffer<i:
        streak+=1
    else:
        streak-=1
    buffer = i

if streak == 7:
    print("ascending")
elif streak == -7:
    print("descending")
else:
    print("mixed")


# =================
# N = list(map(int, input().split()))

# if N[0] < N[1]:
#         direction = 1
# else:
#         direction = -1

# for i in range(len(N)-1):
#     if N[i] < N[i+1] and direction == 1:
#         direction = 1
#     elif N[i] > N[i+1] and direction == -1:
#         direction = -1
#     else:
#         direction = 0

# if direction == 0: print("mixed")
# elif direction == 1: print("ascending")
# elif direction == -1: print("descending")