N = list(input().split())
X = list(map(int, input().split()))

min,max=X[0],X[1]

for i in X:
    if min > i:
        min = i
    if max < i:
        max = i

print(f"{min} {max}")