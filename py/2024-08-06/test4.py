dictionary = {
    "name":"7D 건조 망고",
    "type":"당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin":"필리핀"
}

# key = input("> 접근하고자 하는 키: ")

# if key in dictionary:
#     print(dictionary[key])
# else:
#     print("존재하지 않는 키에 접근하고 있습니다.")
    
# value = dictionary.get(key)
# print("값:",value)

# if value == None:
#     print("존재하지 않는 키에 접근하고 있습니다.")
# # ========================================================
# for key in dictionary:
#     print(key,":",dictionary[key])
# # ==========================================================
# list_a = [1,2,3,4,5]
# list_reversed = reversed(list_a)

# print("# reversed() 함수")
# print("reversed([1,2,3,4,5]):",list_reversed)
# print("list(reversed([1,2,3,4,5])):",list(list_reversed))
# print()

# print("# reversed()  함수와 반복문")
# print("for i in reversed([1,2,3,4,5]):")
# for i in reversed(list_a):
#     print("-",i)

# temp = reversed([1,2,3,4,5,6])

# for i in temp:
#     print("첫 번째 반복문: {}".format(i))
    
# for i in temp:
#     print("두 번째 반복문: {}".format(i))
# # ==========================================================

# example_list = ["요소A","요소B","요소C"]
# i = 0
# for item in example_list:
#     print("{}번째 요소는 {}입니다.".format(i, item))
#     i+=1
    
# for i in range(len(example_list)):
#     print(f"{i}번째 요소는 {example_list[i]}입니다.")
# # ========================================
# print("# 단순 출력")
# print(example_list)
# print()

# print("# enumerate() 함수 적용 출력")
# print(enumerate(example_list))
# print()

# print("# 반복문과 조합하기")
# for i, value in enumerate(example_list):
#     print("{}번째 요소는 {}입니다.".format(i,value))
    
# # =====================================

# example_dictionary = {
#     "keyA":"valueA",
#     "keyB":"valueB",
#     "keyC":"valueC"
# }


# print("딕셔너리의 items() 함수")
# print("items():",example_dictionary.items())
# print()

# print("# 딕셔너리의 items() 함수와 반복문 조합하기")

# for key, element in example_dictionary.items():
#     print("dictionary[{}] = {}".format(key, element))
#     print(f"dictionary[{key}] = {element}")
    
# # ================================================
    
# array = [i*i for i in range(0,20,2)]

# print(array)
    
# array = ["사과", "자두", "초콜릿", "바나나", "체리"]
# output = [fruit for fruit in array if fruit != "초콜릿"]

# print(output)

# # =============================================================

# def print_3_times():
    
#     print("안녕하세요.")
#     print("안녕하세요.")
#     print("안녕하세요.")
    
# print_3_times()

# # ==========================================

# def print_n_times(value,n):
#     for i in range(n):
#         print(value)
        
# print_n_times("안녕하세요",5)

# # ==========================================

# def print_n_times(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
        
# print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

# # ==================================================

# def print_n_times( *values, n =2):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
        
# print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍")

# # ============================================================

# def test(a,b=10,c=100):
#     print(a+b+c)
    
# test(10,20,30)
# test(a=10,b=100,c=200)
# test(c=10,a=100,b=200)
# test(10,c=200)

# # ============================

# def sum_all(start, end):
#     output = 0
    
#     for i in range(start,end+1):
#         output+=i
        
#     return output

# print("0 to 100:", sum_all(0,100))
# print("0 to 1000:", sum_all(0,1000))
# print("50 to 100:", sum_all(50,100))
# print("500 to 1000:", sum_all(500,1000))

# # =========================================

# def sum_all(start = 0,end=100,step=1):
    
#     output=0
#     for i in range(start,end+1,step):
#         output += i
#     return output

# print("A.", sum_all(0,100,10))
# print("B.",sum_all(end=100))
# print("B.",sum_all(end=100,step=2))
# print("D.",sum_all())

# # ==========================================
