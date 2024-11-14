# import random

# def getLotto(a,b,count):
#     numbers = []
    
#     while len(numbers)<6:
#         n= random.randint(a,b)
        
#         if n not in numbers:
#             numbers.append(n)
#             count[n-1]+=1
            
#     return numbers,count

# count =[0]*45

# for i in range(1000):
#     print("로또 번호{}: {}".format(i+1,getLotto(1,45,count)))
# for i in range(45):
#     print("{}: {}개".format(i+1,count[i-1]))
    
    
# =================================================================

# import random
# def getLotto(a,b,c=10000):
#     numbers = []

    
#     while len(numbers)<c:
#         n= random.randint(a,b)
#         numbers.append(n)
#         count[n]+=1
        
#     return count

# count = [0]*46

# print(getLotto(1,45,1000000))
# for i in range(1, 46):
#     print("{}: {}개".format(i-1,count[i]))
# sorted_getLotto = sorted(count) 
# print(sorted_getLotto[-5:])

# print("제일 많이 나온 숫자 5개")
# for i in sorted_getLotto[-5:]:
#     print(f"{count.index(i)}번 {i}개")
    
    
# ===========================================
# import random

# def getLotto(a,b):
#     numbers = []
    
#     while len(numbers)<6:
#         n= random.randint(a,b)
        
#         if n not in numbers:
#             numbers.append(n)
#             count[n] = count.get(n) +1
            
#     return numbers,count

# # 딕셔너리 키값 설정
# count = {}
# for i in range(1,46):
#     count[i] = 0
    
# for _ in range(10000):
#     getLotto(1,45)
    
# list_of_number = []

# # 제일 높은 갯수 5개 뽑기
# for key , value in count.items():
#     list_of_number.append(value)

# print(list_of_number)
    
# sort_list = sorted(list_of_number)

# top5 = sort_list[-5:]

# print(top5)

# # 딕셔너리에서 값 찾기
# for key ,value in count.items():
#     if value in top5:
#         print(f"{key}번 {value}개")
