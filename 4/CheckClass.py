students=[]
for i in range(28):
    students.append(int(input()))

for i in range(1,31):
    if i not in students:
        print(i)