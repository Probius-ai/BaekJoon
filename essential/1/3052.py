numbers = set()

for _ in range(10):
    i = int(input())
    numbers.add(i%42)

print(len(numbers))