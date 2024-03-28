max = 0
num = 0
for i in range(9):
    a = int(input())
    if a > max:
        max = a
        num = i+1

print(f"{max}\n{num}")