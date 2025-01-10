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