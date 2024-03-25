score = int(input())

# 등급 결정
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score <= 89:
    grade = 'B'
elif 70 <= score <= 79:
    grade = 'C'
elif 60 <= score <= 69:
    grade = 'D'
else:
    grade = 'F'

# 결과 출력
print(grade)