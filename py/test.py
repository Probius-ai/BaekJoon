# list_a = [273,32,103,"문자열",True,False]
# print(list_a[0])

# print(list_a[1])

# print(list_a[1:3])

# print(list_a[-3:])

# univ="선문대학교"
# text="동해물과 백두산이 마르고 닳도록"
# line = text.split(" ")

# print(univ, "type: ",type(univ))
# print(univ, "type: ",type(univ[0]))
# print(univ, "type: ",type(univ[0:3]))
# print(univ, "type: ",type(univ[-1]))

# print(line[0], "type: ",type(line[0]))

# print(line, "type: ", type(line))

# # ========================

# list_a = [273,"321","선문대",  True]

# print(list_a[1], "type: ",type(list_a))
# print(list_a[0], "type: ",type(list_a))
# print(list_a[3], "type: ",type(list_a))
# # print(list_a[4], "type: ",type(list_a))

# print(list_a[1][1], "type: ",type(list_a))
# print(list_a[1][2], "type: ",type(list_a))
# # print(list_a[0][1], "type: ",type(list_a))

# # ======================

# list_a = [1,2,3]
# list_b = [4,5,6]
# text_a ="선문대"
# text_b ="대학교"
# print(list_a+list_b)
# print(text_a+text_b)

# #============================================


# list_a = [1,2,3]
# list_a.append([4,5,6])

# print(list_a)

# list_a=[0,1,2,3,4,5,6,7,8]
# del list_a[3]

# list_a.remove(2)

# #============================

# list_a =[273,32,103,57,52]

# print(273 in list_a)
# print(99 in list_a)
# print(53 not in list_a)

# #==================

# list_a = [1,2,3]

# print("# 리스트 뒤에 요소 추가하기")
# list_a.append(4)
# list_a.append(5)
# print(list_a)
# print()

# print("리스트 중간에 요소 추가하기")
# list_a.insert(0,10)
# print(list_a)
# print()

# number = [273, 32, 103,57,52]
# aaa = [1,"선문대",2,"서울대",3,"하버드"]
# aaa.insert(2,"좋아요")
# aaa.pop(-1)
# del aaa[-1]

# for i in number:
#     print("i:",i,end=" ")
# print()
# for j in aaa:
#     print("j:",j,end=" ")

# # ====================================

# list_a = [3,2,1,5,7,6]

# list_a.sort()

# print(list_a)

# # =====================================

# print(list(range(1,6)))

# list_a = list(range(1,6))

# # =======================================

# for i in "선문대학교":
#     print("{} = 반복변수".format(i))

# array = [273,32,103,57,52]

# for i in range(len(array)):
    
#     print("{}번째 반복: {}".format(i,array[i]))
    
    
# list_of_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for element in list_of_list:
#     print(element)
    
# for items in list_of_list:
#     for item in items:
#         print(item)

# # ===========================================

# a=[1,2,3,4]
# b=[*a,*a]
# print(b)

# # ========================================
# for i in reversed(range(5)):
#     print(f"현재 반복 변수: {i}")
# # ===============================
# list_test = [1,2,1,2]
# value = 2

# while value in list_test:
#     list_test.remove(value)
    
# print(list_test)

# # =============================

# import time
# print(time.time())

# # # =============================

# number = 0 
# target_tick = time.time() + 5
# while time.time() < target_tick:
#     number+=1
    
# print("5초 동안 {}번 반복했습니다.".format(number))

# #===========================================
# i = 0

# while True:
#     print("{}번째 반복문입니다.".format(i))
#     i+=1
    
#     input_text = input(">종료하시겠습니까?(y): ")
#     if input_text in ["y", "Y"]:
#         print("반복을 종료합니다.")
#         break
    
# # ===========================================
    
# numbers = [5,15,6,20,7,25]

# for number in numbers:
#     if number <10:
#         continue
#     print(number)
    
# # ===============================================

dict_a = {
    
    "name":"어벤져스 엔드게임",
    "type":"히어로 무비"
    
}

print(dict_a["name"])

dict_b = {
    "director":["안소니 루소","조 루소"],
    "cast":["아이언맨","타노스","토르","닥터스트레인지","헐크"]
}

print(dict_b)

print(dict_b["director"][1])


dict_a["price"] = 7000

print(dict_a)

del dict_a["price"]

print(dict_a)