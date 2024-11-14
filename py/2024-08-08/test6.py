# import random as r
# print("---------------- random 모듈 --------------------")

# print("random():",r.random())

# print("uniform(min,max):",r.uniform(1,10))

# print("randrange(max):",r.randrange(99))
# print("randrange(min,max):",r.randrange(90,99))

# xlist = [i for i in range(1,46)]
# print(xlist)

# print("choice(list):",r.choice(xlist))

# print("sample(list):", r.sample(xlist,k=5))

# # =======================================================================

# import random, os

# print("현재 폴더:", os.getcwd())
# print("폴더 내용:", os.listdir())

# os.system("ipconfig")
# # =======================================================

# import os

# print("현재 운영체재:", os.name)
# print("현재 폴더:",os.getcwd())
# print("현재 폴더 내부의 요소:",os.listdir())

# os.mkdir("hello")
# os.rmdir("hello")

# with open("original.txt",'w')as file:
#     file.write("hello")
# os.rename("original.txt","new.txt")

# os.remove("new.txt")

# os.system("dir")

# # ====================================================

# import datetime
# import time

# now = datetime.datetime.now()
# print("현재 시간:",now)

# after = now + datetime.timedelta(\
#     weeks=2,days=2,\
#     hours=2,minutes=10,seconds=20)
# print("이후 시간:", after)

# time.sleep(3)

# output = now.replace(year=(now.year+1))
# str = output.strftime("%Y년 %m월 %d일")
# print("교체시간:",str)

# #  ==================================================
# pip install matplotlib

import matplotlib.pyplot as plt
import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1,10))

print(numbers)
plt.plot(numbers)

plt.title("My first chart")
plt.xlabel("time")
plt.ylabel("count")
plt.grid()
plt.show()