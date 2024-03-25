# 입력받고 입력값 정수로 변환
dice = input().split()

for i in range(len(dice)):
    dice[i]=int(dice[i])

# 같은 눈 나온 개수 확인

if dice[0]==dice[1]==dice[2] :
    print(10000+dice[0]*1000)
elif dice[0]==dice[1] :
    print(1000+dice[0]*100)
elif dice[0]==dice[2] :
    print(1000+dice[0]*100)
elif dice[1]==dice[2] :
    print(1000+dice[1]*100)
else :
    print(max(dice)*100)