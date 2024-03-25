#첫번째, 두번째 수 입력받기
a=int(input())
b=int(input())

#세자리 정수 각 자리 숫자 나눠서 리스트로 저장
A = [a // 100, (a // 10) % 10, a % 10]
B = [b // 100, (b // 10) % 10, b % 10]

# 각각의 연산 결과를 계산
result1 = A[0]*B[0]*100 + A[1]*B[0]*10 + A[2]*B[0]
result2 = A[0]*B[1]*100 + A[1]*B[1]*10 + A[2]*B[1]
result3 = A[0]*B[2]*100 + A[1]*B[2]*10 + A[2]*B[2]

result4 = result1*100+result2*10+result3
# 결과를 출력합니다.
print(result3)
print(result2)
print(result1)
print(result4)