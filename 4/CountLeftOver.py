results = []
result = []
for i in range(10): # get numbers and add leftovers
    num = int(input())
    results.append(num%42)

for i in results:
    if i not in result:
        result.append(i)

print(len(result))