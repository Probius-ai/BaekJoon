a = int(input())
time = 1
for i in range(8):
    b = int(input())
    if (a<b):
        a=b
        time = i+2

print(a)
print(time)