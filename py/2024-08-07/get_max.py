def getMax(list_number):
    
    largest = list_number[0]
    
    for i in list_number:
        if largest < i:
            largest = i
            
    return largest

x = int(input("숫자 x:"))

y = int(input("숫자 y:"))

z = int(input("숫자 z:"))

u = int(input("숫자 u:"))

i = int(input("숫자 i:"))

list_number=[x,y,z,u,i]

print("가장 큰 값은:",getMax(list_number))