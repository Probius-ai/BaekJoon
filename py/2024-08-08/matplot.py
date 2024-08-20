# import matplotlib.pyplot as plt

# xlist = []
# for i in range(-100,100):
#     xlist.append(i/10.0)
    
# a= int(input("a: "))
# b= int(input("b: "))
# c= int(input("c: "))

# ylist = []
# for i in xlist:
#     ylist.append(a*i**2 + b*i + c)
    
# plt.title("Graphing Parabola")
# plt.xlabel("X name")
# plt.ylabel("Y name")
# plt.plot(xlist, ylist)
# plt.show()

# # ===========================
# 서울 부산의 기온 표시

import matplotlib.pyplot as plt

X = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
Y1 = [15.6,14.2,16.3,18.2,17.1,20.2,22.4]
Y2 = [20.1,23.1,23.8,25.9,23.4,25.1,26.3]

# # ==================================
# 선형 그래프
# plt.figure(figsize=(16,9))
# plt.plot(X,Y1,label="Seoul")
# plt.plot(X,Y2,label="Busan")
# plt.xlabel("day")
# plt.ylabel("temperature")
# plt.legend(loc = "upper left")
# plt.title("Temperature of Cities")
# plt.show()

# # =====================================
# 막대 그래프
# plt.bar(X,Y1)
# plt.show()

# # =====================================
# 파이 차트
# Y3 = [40,20,10,30]
# Y3_labels=["Eating Out","Shopping","Groceries","Housing"]

# explode = [0.1,0,0,0]
# plt.pie(Y3, labels=Y3_labels,explode=explode)

# plt.show()
# =========================================
# 산점도 그래프
plt.figure(figsize=(16,9))
plt.scatter(X,Y1,label="Seoul")
plt.scatter(X,Y2,label="Busan")
plt.xlabel("day")
plt.ylabel("temperature")
plt.legend(loc = "upper left")
plt.title("Temperature of Cities")
plt.show()