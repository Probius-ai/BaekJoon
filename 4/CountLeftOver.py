# 입력받은 숫자의 나머지를 저장할 집합
remainders = set()

# 10번 반복하여 숫자를 입력받고 나머지를 집합에 추가
for _ in range(10):
    num = int(input())
    remainders.add(num % 42)

# 집합에 저장된 나머지의 개수 출력
print(len(remainders))
