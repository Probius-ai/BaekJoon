# 2번 문제풀이===========================================
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if(number>=100):
        print("- 100 이상의 수:",number)
        
# 3번 문제풀이===========================================
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if(number%2==0):
        print(f"{number} 는 짝수입니다.")
    else:
        print("{} 는 홀수입니다.".format(number))
        
for number in numbers:
    print(f"{number} 는 {len(str(number))} 자릿수입니다.")
        
# 4번 문제풀이=======================
numbers = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]

for number in numbers:
    output[number%3-1].append(number)
    
print(output)

# 5번 문제풀이=================================
numbers = [1,2,3,4,5,6,7,8,9]

for i in range(0, len(numbers) // 2):
    # j가 1, 3, 5, 7이 나오려면
    # 어떤 식을 사용해야 할까요?
    j = i*2+1
    print(f"i = {i}, j = {j}")
    numbers[j] = numbers[j] ** 2
    
print(numbers)