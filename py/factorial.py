n= int(input("정수를 입력하시오: "))
fact =1

for i in range(n,0,-1):
    fact = fact*i
    if(i == 1):
        print("{}".format(i),end=" = ")
    else:
        print("{}".format(i),end="*")
    
print(f"{n}! 은 {fact}이다.")