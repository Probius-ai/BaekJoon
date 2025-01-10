N=int(input())
numbers = input().split()
max = int(numbers[0])
min = int(numbers[0])
numbers.pop(0)
for i in numbers:
    if max<int(i):
        max = int(i)
    if min>int(i):
        min = int(i)
print(min,max)