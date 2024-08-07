# def factorial(n):
#     output = 1
    
#     for i in range(1,n+1):
#         output*=i
#     return output

# print("1!:",factorial(1))
# print("2!:",factorial(2))
# print("3!:",factorial(3))
# print("4!:",factorial(4))

# def factorial(n):
#     output = 1
    
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)

# print("1!:",factorial(1))
# print("2!:",factorial(2))
# print("3!:",factorial(3))
# print("4!:",factorial(4))
# # ============================== 
# def fibonacci(n):
#     if n ==1:
#         return 1
#     if n ==2:
#         return n
#     else:
#         return fibonacci(n-1) +fibonacci(n-2)
    
# print(fibonacci(10))
# print(fibonacci(20))
# print(fibonacci(30))
# print(fibonacci(40))

# # =====================================

# dictionary = {
#     1:1,
#     2:2
# }

# def fibonacci(n):
#     if n in dictionary:
#         return dictionary[n]
#     else:
#         output = fibonacci(n -1) + fibonacci(n-2)
#         dictionary[n] = output
#         return output
    
# print(fibonacci(10))    
# print(fibonacci(20))    
# print(fibonacci(30))    
# print(fibonacci(40)) 
# print(fibonacci(50)) 
# print(fibonacci(60))

# #===========================
# list_test = [10,20,30]
# tuple_test = (10,20,30)

# print(list_test,type(list_test))
# print(tuple_test,type(tuple_test))

# tuple_test =(10,)
# print(tuple_test,type(tuple_test))
# tuple_test =100
# print(tuple_test, type(tuple_test))

# #================================

# def sunmoon():
#     return (11,12,13,14)

# aaa = sunmoon()
# print(sunmoon(), type(sunmoon()))
# print(aaa[0], type(aaa[0]))

# #===============================

# power = lambda x: x*x
# under_3 = lambda x: x<3

# list_input_a = [nums 
#                 for nums in range(1,6)]

# output_a = map(power, list_input_a)
# print("# map() 함수의 실행결과")
# print("map(power, list_input_a):", output_a)
# print("map(power, list_input_a):",list(output_a))
# print()

# output_b = filter(under_3, list_input_a)
# print("#filter() 함수의 실행결과")
# print("filter(under_3, output_b):",output_b)
# print("filter(under_3, output_b):",list(output_b))

# # ================================================

# def test():
#     print("함수가 호출되었습니다.")
#     yield "test"
    
# print("A 지점 통과")
# test()

# print("B 지점 통과")
# test()
# print(test())

# # ===========================

# def test():
#     print("A 지점 통과")
#     yield 1
#     print("B 지점 통과")
#     yield 2
#     print("C 지점 통과")
#     yield
    
# output = test()

# print("D 지점 통과")
# a = next(output)
# print(a)
# print("E 지점 통과")
# b= next(output)
# print(b)
# print("F 지점 통과")
# c= next(output)
# print(c)

# next(output)

# # =========================================

# file = open("basic.txt","w", encoding= "UTF-8")

# file.write("안녕하세요")

# file.close()

# #  ====================================

# with open("basic.txt","r", encoding="UTF-8") as file:
#     contents = file.read()
# print(contents)

# # ======================================================

# num_a = int(input("반지름 입력(정수):"))

# print("원의 반지름:", num_a)
# print("원의 둘레: ", 2*3.14*num_a)
# print("원의 넓이: ", 3.14*num_a*num_a)
# # ======================================
# input_a = input("반지름 입력(정수):")

# if input_a.isdigit():
#     num_a = int(input_a)
#     print("원의 반지름:", num_a)
#     print("원의 둘레: ", 2*3.14*num_a)
#     print("원의 넓이: ", 3.14*num_a*num_a)
# else:
#     print("정수로 정확하게 입력하세요.")
    
# # ========================================================

# try:
#     number_input_a = int(input("정수 입력> "))
    
#     print("원의 반지름:",number_input_a)
#     print("원의 둘레: {}".format(2*3.14*number_input_a))
#     print(f"원의 넓이: {3.14*number_input_a*number_input_a}")
# except:
#     print("정수로 정확하게 입력하세요.")
    
# # ====================================================================

# list_input_a = ["52", "273", "32", "스파이", "103"]

# list_number = []
# for item in list_input_a:
#     try:
#         float(item)
#         list_number.append(item)
#     except:
#         pass
    
# print("{} 내부에 있는 숫자는".format(list_number))

# # ================================================

# try:
#     num_a = int(input("정수 입력> "))
# except:
#     print("정수를 입력하지 않았습니다.")
# else:
#     print("원의 반지름: {}".format(num_a))
#     print("원의 둘레: {}".format(2*3.14*num_a))
#     print("원의 넓이: {}".format(3.14*num_a*num_a))
# finally:
#     print("프로그램이 종료했습니다.")

# # ===============================================================

list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력>"))
    
    print("{}번째 요소: {}".format(number_input,list_number[number_input]))
    예외.발생해주세요()
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print(type(exception),exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print(type(exception),exception)
except Exception as exception:
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(type(exception),exception)